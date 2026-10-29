"""Compila el sitio de ninfacantu.com en la carpeta _site/.

  python3 build.py          -> genera _site/
  python3 build.py --zip    -> además crea ninfacantu-sitio.zip listo para Netlify Drop

Contenido editable (también desde /admin):
  content/datos/*.json      perfil, trayectoria, ejes y ajustes del sitio
  content/noticias/*.md     una nota por archivo
"""
import datetime as dt
import glob, json, math, os, re, shutil, sys, unicodedata, zipfile
from email.utils import format_datetime
from xml.sax.saxutils import escape

import jinja2, markdown, yaml

RAIZ = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(RAIZ, "_site")
POR_PAGINA = 12
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
from iconos import svg as icono_svg  # noqa: E402


class Obj(dict):
    """Diccionario con acceso por atributo (perfil.nombre)."""
    def __getattr__(self, k):
        return self.get(k)


def a_obj(d):
    return json.loads(json.dumps(d, default=str), object_hook=Obj)


def slugify(t):
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def a_fecha(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    return dt.date.fromisoformat(str(v)[:10])


def md(texto):
    return markdown.markdown(str(texto or ""), extensions=["extra", "sane_lists"])


def leer_md(ruta):
    s = open(ruta, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", s, re.S)
    if not m:
        return {}, s
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


# ------------------------------------------------------------------ datos
def cargar():
    datos = {}
    for ruta in glob.glob(os.path.join(RAIZ, "content", "datos", "*.json")):
        datos[os.path.basename(ruta)[:-5]] = a_obj(json.load(open(ruta, encoding="utf-8")))
    notas = []
    for ruta in glob.glob(os.path.join(RAIZ, "content", "noticias", "*.md")):
        fm, cuerpo = leer_md(ruta)
        if fm.get("borrador"):
            continue
        slug = os.path.basename(ruta)[:-3]
        fecha = a_fecha(fm.get("date", dt.date.today()))
        html = md(cuerpo)
        palabras = len(re.sub(r"<[^>]+>", " ", html).split())
        cat = fm.get("categoria") or "Noticias"
        notas.append(Obj(
            slug=slug, url=f"/noticias/{slug}/", fecha=fecha, titulo=fm.get("title", slug),
            categoria=cat, cat_slug=slugify(cat), imagen=fm.get("imagen") or "/assets/img/og.jpg",
            pie_imagen=fm.get("pie_imagen") or "", resumen=fm.get("resumen") or "",
            destacada=bool(fm.get("destacada")), autor=fm.get("autor") or "",
            fuente_nombre=fm.get("fuente_nombre") or "", fuente_url=fm.get("fuente_url") or "",
            html=html, lectura=max(1, round(palabras / 220)),
        ))
    notas.sort(key=lambda n: (n.fecha, n.slug), reverse=True)
    return datos, notas


# ------------------------------------------------------------------ plantillas
def entorno():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(RAIZ, "templates")),
                             autoescape=jinja2.select_autoescape(["html", "xml"]),
                             trim_blocks=True, lstrip_blocks=True)
    env.filters.update(
        fecha=lambda d: f"{a_fecha(d).day} de {MESES[a_fecha(d).month - 1]} de {a_fecha(d).year}",
        fecha_corta=lambda d: f"{a_fecha(d).day} {MESES[a_fecha(d).month - 1][:3]} {a_fecha(d).year}",
        iso=lambda d: a_fecha(d).isoformat(),
        md=lambda s: jinja2.utils.markupsafe.Markup(md(s)),
        slug=slugify,
    )
    env.globals.update(icono=lambda n, c="": jinja2.utils.markupsafe.Markup(icono_svg(n, c)),
                       anio=dt.date.today().year)
    return env


def escribir(ruta_url, html):
    destino = os.path.join(SALIDA, ruta_url.strip("/"))
    if not ruta_url.endswith((".html", ".xml", ".txt")):
        destino = os.path.join(destino, "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(html)


def paginar(lista, base):
    total = max(1, math.ceil(len(lista) / POR_PAGINA))
    for i in range(total):
        url = base if i == 0 else f"{base}pagina/{i + 1}/"
        prev = None if i == 0 else (base if i == 1 else f"{base}pagina/{i}/")
        sig = f"{base}pagina/{i + 2}/" if i + 1 < total else None
        yield url, lista[i * POR_PAGINA:(i + 1) * POR_PAGINA], Obj(actual=i + 1, total=total, anterior=prev, siguiente=sig)


def compilar():
    datos, notas = cargar()
    sitio = datos["sitio"]
    env = entorno()
    if os.path.isdir(SALIDA):
        shutil.rmtree(SALIDA)
    shutil.copytree(os.path.join(RAIZ, "static"), SALIDA)
    # El nombre del apartado informativo aparece también en el menú de /admin
    ap = datos.get("apartado") or {}
    cfg = os.path.join(SALIDA, "admin", "config.yml")
    texto = open(cfg, encoding="utf-8").read()
    nombre_ap = str(ap.get("nombre") or "Apartado informativo").replace('"', "'")
    texto = texto.replace("__NOMBRE_APARTADO__", nombre_ap).replace("__RUTA_APARTADO__", "/" + slugify(ap.get("ruta") or "archivo") + "/")
    open(cfg, "w", encoding="utf-8").write(texto)

    cats_orden = list(sitio.get("categorias") or [])
    for n in notas:
        if n.categoria not in cats_orden:
            cats_orden.append(n.categoria)
    categorias = [Obj(nombre=c, slug=slugify(c), total=sum(1 for n in notas if n.categoria == c)) for c in cats_orden]
    categorias = [c for c in categorias if c.total]
    principal = next((n for n in notas if n.destacada), notas[0] if notas else None)
    resto = [n for n in notas if n is not principal]

    base = dict(datos, sitio=sitio, notas=notas, categorias=categorias, recientes=notas[:6])

    indexar_todo = bool(sitio.get("indexar_sitio"))
    ruta_ap = "/" + slugify((datos.get("apartado") or {}).get("ruta") or "archivo") + "/"

    def pag(plantilla, url, **extra):
        ctx = dict(base, url=url, indexable=indexar_todo or url.startswith(ruta_ap), **extra)
        escribir(url, env.get_template(plantilla).render(**ctx))

    porcat = {c.nombre: [n for n in notas if n.categoria == c.nombre] for c in categorias}
    pag("inicio.html", "/", principal=principal, secundarias=resto[:4], mas=resto[4:10], porcat=porcat,
        ticker=notas[:8])
    pag("biografia.html", "/biografia/", titulo="Biografía")
    pag("trayectoria.html", "/trayectoria/", titulo="Trayectoria")
    pag("contacto.html", "/contacto/", titulo="Contacto")
    pag("gracias.html", "/gracias/", titulo="Mensaje enviado")
    pag("404.html", "/404.html", titulo="Página no encontrada")

    for url, lista, p in paginar(notas, "/noticias/"):
        pag("noticias.html", url, titulo="Noticias", lista=lista, paginacion=p, cat_actual=None)
    for c in categorias:
        for url, lista, p in paginar(porcat[c.nombre], f"/noticias/{c.slug}/"):
            pag("noticias.html", url, titulo=c.nombre, lista=lista, paginacion=p, cat_actual=c)

    for i, n in enumerate(notas):
        relacionadas = [x for x in notas if x.categoria == n.categoria and x is not n][:3]
        if len(relacionadas) < 3:
            relacionadas += [x for x in notas if x is not n and x not in relacionadas][:3 - len(relacionadas)]
        pag("nota.html", n.url, titulo=n.titulo, nota=n, relacionadas=relacionadas,
            anterior=notas[i + 1] if i + 1 < len(notas) else None, siguiente=notas[i - 1] if i > 0 else None)

    # Apartado informativo: no se enlaza desde el menú ni desde ninguna página,
    # pero se publica, se incluye en el sitemap y en llms.txt para buscadores e IA.
    url_sitio = sitio.url.rstrip("/")
    apartado = datos.get("apartado") or Obj()
    ap_notas = cargar_apartado() if apartado.get("activo", True) else []
    ap_base = "/" + slugify(apartado.get("ruta") or "archivo") + "/"
    if ap_notas:
        for x in ap_notas:
            x.url = ap_base + x.slug + "/"
        pag("apartado.html", ap_base, titulo=apartado.get("nombre") or "Archivo informativo",
            descripcion=apartado.get("descripcion") or sitio.descripcion, apartado=apartado, ap_notas=ap_notas)
        for x in ap_notas:
            pag("apartado_nota.html", x.url, titulo=x.titulo, descripcion=x.resumen or x.titulo,
                apartado=apartado, ap_base=ap_base, ap_nota=x, ap_notas=ap_notas)
    escribir_llms(url_sitio, datos, notas if indexar_todo else [], apartado, ap_base, ap_notas, indexar_todo)

    # RSS, sitemap y robots
    items = "".join(
        f"<item><title>{escape(n.titulo)}</title><link>{url_sitio}{n.url}</link><guid>{url_sitio}{n.url}</guid>"
        f"<pubDate>{format_datetime(dt.datetime.combine(n.fecha, dt.time(12), dt.timezone.utc))}</pubDate>"
        f"<description>{escape(n.resumen)}</description></item>" for n in notas[:30])
    escribir("/feed.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{escape(sitio.titulo)}</title>'
                          f"<link>{url_sitio}/</link><description>{escape(sitio.descripcion)}</description><language>es-MX</language>{items}</channel></rss>")
    urls = ["/", "/biografia/", "/trayectoria/", "/noticias/", "/contacto/"] + [f"/noticias/{c.slug}/" for c in categorias] + [n.url for n in notas]
    if not indexar_todo:
        urls = []  # mientras el sitio esté en noindex, el sitemap solo lista el apartado
    if ap_notas:
        urls += [ap_base] + [x.url for x in ap_notas]
    escribir("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
             + "".join(f"<url><loc>{url_sitio}{u}</loc></url>" for u in urls) + "</urlset>")
    escribir("/robots.txt", f"User-agent: *\nDisallow: /admin/\nSitemap: {url_sitio}/sitemap.xml\n")
    print(f"Sitio compilado en _site/ con {len(notas)} notas y {len(categorias)} categorías.")


def cargar_apartado():
    """Notas del apartado informativo (content/apartado/*.md)."""
    lista = []
    for ruta in glob.glob(os.path.join(RAIZ, "content", "apartado", "*.md")):
        fm, cuerpo = leer_md(ruta)
        if fm.get("borrador"):
            continue
        lista.append(Obj(slug=os.path.basename(ruta)[:-3], titulo=fm.get("title", ""),
                         fecha=a_fecha(fm.get("date", dt.date.today())), resumen=fm.get("resumen") or "",
                         etiquetas=fm.get("etiquetas") or [], texto=cuerpo.strip(), html=md(cuerpo),
                         orden=fm.get("orden") or 100))
    lista.sort(key=lambda x: (x.orden, -x.fecha.toordinal()))
    return lista


def escribir_llms(url_sitio, datos, notas, apartado, ap_base, ap_notas, indexar_todo=True):
    """llms.txt (índice) y llms-full.txt (texto completo) para asistentes de IA."""
    p, t = datos["perfil"], datos.get("trayectoria") or Obj(cargos=[])
    cab = [f"# {p.nombre}", "", f"> {p.cargo_actual}. {p.bio_corta}", ""]
    idx = list(cab)
    if indexar_todo:
        idx += ["## Páginas principales",
                f"- [Biografía]({url_sitio}/biografia/): trayectoria personal y profesional",
                f"- [Trayectoria]({url_sitio}/trayectoria/): cargos ocupados",
                f"- [Noticias]({url_sitio}/noticias/): {len(notas)} notas con fuente enlazada", ""]
    if ap_notas:
        idx += [f"## {apartado.get('nombre') or 'Archivo informativo'}"]
        idx += [f"- [{x.titulo}]({url_sitio}{x.url}): {x.resumen}" for x in ap_notas] + [""]
    if notas:
        idx += ["## Noticias"] + [f"- [{n.titulo}]({url_sitio}{n.url}) ({n.fecha.isoformat()}): {n.resumen}" for n in notas]
    idx += ["", "## Opcional", f"- [Texto completo]({url_sitio}/llms-full.txt)"]
    escribir("/llms.txt", "\n".join(idx) + "\n")

    sin_md = lambda h: re.sub(r"\n{3,}", "\n\n", re.sub(r"<[^>]+>", "", h)).strip()
    full = list(cab)
    if indexar_todo:
        full += ["## Biografía", "", str(p.biografia or ""), "", "## Cargos"]
    for c in (t.cargos if indexar_todo else []):
        periodo = " ".join(x for x in [c.inicio, "a la fecha" if c.actual else (f"a {c.fin}" if c.fin else "")] if x)
        full.append(f"- {c.cargo}, {c.institucion}" + (f" ({periodo})" if periodo else ""))
    if ap_notas:
        full += ["", f"## {apartado.get('nombre') or 'Archivo informativo'}"]
        for x in ap_notas:
            full += ["", f"### {x.titulo}", f"URL: {url_sitio}{x.url}", "", x.texto]
    if notas:
        full += ["", "## Noticias"]
    for n in notas:
        full += ["", f"### {n.titulo}", f"Fecha: {n.fecha.isoformat()} | Tema: {n.categoria} | URL: {url_sitio}{n.url}",
                 f"Fuente: {n.fuente_nombre} {n.fuente_url}".rstrip(), "", sin_md(n.html)]
    escribir("/llms-full.txt", "\n".join(full) + "\n")


def empaquetar():
    destino = os.path.join(RAIZ, "ninfacantu-sitio.zip")
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for carpeta, _, archivos in os.walk(SALIDA):
            for a in archivos:
                ruta = os.path.join(carpeta, a)
                z.write(ruta, os.path.relpath(ruta, SALIDA))
    print("Paquete:", destino)


if __name__ == "__main__":
    compilar()
    if "--zip" in sys.argv:
        empaquetar()
