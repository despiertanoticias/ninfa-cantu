import markdownIt from "markdown-it";

const md = markdownIt({ html: true, linkify: true, typographer: true });

const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
  "agosto", "septiembre", "octubre", "noviembre", "diciembre"];

export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/admin": "admin" });

  // Noticias: más recientes primero
  eleventyConfig.addCollection("noticias", (api) =>
    api.getFilteredByGlob("src/noticias/*.md")
      .filter((p) => !p.data.borrador)
      .sort((a, b) => b.date - a.date)
  );

  eleventyConfig.addFilter("fecha", (d) => {
    const f = new Date(d);
    return `${f.getUTCDate()} de ${MESES[f.getUTCMonth()]} de ${f.getUTCFullYear()}`;
  });
  eleventyConfig.addFilter("fechaCorta", (d) => {
    const f = new Date(d);
    return `${f.getUTCDate()} ${MESES[f.getUTCMonth()].slice(0, 3)} ${f.getUTCFullYear()}`;
  });
  eleventyConfig.addFilter("iso", (d) => new Date(d).toISOString());
  eleventyConfig.addFilter("md", (s) => (s ? md.render(String(s)) : ""));
  eleventyConfig.addFilter("mdInline", (s) => (s ? md.renderInline(String(s)) : ""));
  eleventyConfig.addFilter("limite", (arr, n) => (arr || []).slice(0, n));
  eleventyConfig.addFilter("desde", (arr, n) => (arr || []).slice(n));
  eleventyConfig.addFilter("lectura", (s) => {
    const palabras = String(s || "").replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(palabras / 220));
  });
  eleventyConfig.addFilter("anio", () => new Date().getFullYear());
  eleventyConfig.addFilter("porCategoria", (arr, cat) => (arr || []).filter((p) => p.data.categoria === cat));
  // Enlace activo del menú
  eleventyConfig.addFilter("activo", (url, ruta) => url === ruta || (ruta !== "/" && String(url).startsWith(ruta)));
  // Nota principal de la portada: la destacada más reciente, o la más reciente
  eleventyConfig.addFilter("principal", (arr) => (arr || []).find((p) => p.data.destacada) || (arr || [])[0]);
  // Notas excepto una URL, limitadas a n
  eleventyConfig.addFilter("excepto", (arr, url, n) => (arr || []).filter((p) => p.url !== url).slice(0, n));

  return {
    dir: { input: "src", includes: "_includes", data: "_data", output: "_site" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
}
