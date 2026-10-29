"""Genera las portadas editoriales (1200x750) de las notas a partir de herramientas/portadas.json.

Requiere Playwright con Chromium. Uso:
  python3 herramientas/portadas.py [ruta-a-chromium]
"""
import base64, json, os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iconos import svg

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "static", "assets", "uploads", "portadas")
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

def b64(ruta, tipo):
    return f"data:{tipo};base64," + base64.b64encode(open(ruta, "rb").read()).decode()

MONO = b64(os.path.join(RAIZ, "static/assets/img/monograma.png"), "image/png")
LOGO = b64(os.path.join(RAIZ, "static/assets/img/logo-ninfa-cantu-sm.png"), "image/png")
FOTO = b64(os.path.join(RAIZ, "static/assets/img/ninfa-cantu.jpg"), "image/jpeg")

FONDOS = {
    "Inversión": "linear-gradient(135deg,#6e0f26 0%,#4a0716 55%,#2b030c 100%)",
    "Economía": "linear-gradient(160deg,#5e0b1e 0%,#3a0512 60%,#22020a 100%)",
    "Internacional": "radial-gradient(circle at 78% 45%,#7a1430 0%,#480617 45%,#25020b 100%)",
    "MiPyMEs": "linear-gradient(120deg,#7a1430 0%,#55091d 50%,#300410 100%)",
    "Gestión": "linear-gradient(135deg,#4a0716 0%,#2b030c 100%)",
}

PLANTILLA = """<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0}
body{width:1200px;height:750px;overflow:hidden;font-family:'Inter Display','Inter',sans-serif;color:#fff;background:%(fondo)s;position:relative}
.patron{position:absolute;inset:0;opacity:.5;%(patron)s}
.marca{position:absolute;right:-70px;bottom:-60px;width:560px;opacity:.10}
.marco{position:absolute;inset:30px;border:1.5px solid rgba(201,164,106,.55)}
.icono{position:absolute;right:120px;top:170px;width:330px;height:330px;color:#c9a46a;opacity:.95}
.foto{position:absolute;right:30px;top:30px;bottom:30px;width:470px;background:url(%(foto)s) center 25%%/cover;filter:grayscale(1) contrast(1.05);mix-blend-mode:luminosity}
.foto::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#3a0512 0%%,rgba(94,11,30,.35) 45%%,rgba(94,11,30,.15) 100%%)}
.txt{position:absolute;left:90px;top:96px;width:%(ancho)spx}
.cat{display:inline-flex;align-items:center;gap:14px;font-weight:700;font-size:26px;color:#e2c79a;letter-spacing:.04em}
.cat::before{content:"";width:44px;height:4px;background:#c9a46a}
.cifra{font-weight:900;font-size:%(tam)spx;line-height:.95;letter-spacing:-.03em;margin:46px 0 22px;color:#fff}
.etq{font-family:'DejaVu Serif',Georgia,serif;font-size:36px;line-height:1.25;color:#f1e3c8;max-width:560px}
.pie{position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;align-items:center}
.pie img{height:40px}
.pie span{font-size:22px;color:rgba(255,255,255,.7);font-weight:600}
</style></head><body>
<div class="patron"></div>
%(visual)s
<div class="marco"></div>
<div class="txt"><div class="cat">%(categoria)s</div><div class="cifra">%(cifra)s</div><div class="etq">%(etiqueta)s</div></div>
<div class="pie"><img src="%(logo)s" alt=""><span>%(fecha)s</span></div>
</body></html>"""

PATRONES = {
    "Economía": "background-image:linear-gradient(rgba(201,164,106,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(201,164,106,.10) 1px,transparent 1px);background-size:60px 60px",
    "Internacional": "background-image:repeating-radial-gradient(circle at 78% 45%,transparent 0 58px,rgba(201,164,106,.10) 58px 60px)",
    "Inversión": "background-image:repeating-linear-gradient(115deg,transparent 0 70px,rgba(201,164,106,.10) 70px 72px)",
    "MiPyMEs": "background-image:radial-gradient(rgba(201,164,106,.18) 1.5px,transparent 1.5px);background-size:28px 28px",
    "Gestión": "",
}

def fecha_larga(iso):
    a, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m)-1]} de {a}"

def html(p):
    retrato = p["icono"] == "retrato"
    cifra = p["cifra"]
    tam = 170 if len(cifra) <= 6 else 130 if len(cifra) <= 9 else 96
    visual = ('<div class="foto"></div>' if retrato else
              f'<img class="marca" src="{MONO}" alt="">' + svg(p["icono"], "icono", 1.6))
    return PLANTILLA % dict(fondo=FONDOS.get(p["categoria"], FONDOS["Economía"]), patron=PATRONES.get(p["categoria"], ""),
                            foto=FOTO, visual=visual, ancho=620 if retrato else 640, categoria=p["categoria"],
                            cifra=cifra, tam=tam, etiqueta=p["etiqueta"], logo=LOGO, fecha=fecha_larga(p["fecha"]))

def main():
    chrome = sys.argv[1] if len(sys.argv) > 1 else None
    datos = json.load(open(os.path.join(RAIZ, "herramientas", "portadas.json"), encoding="utf-8"))
    os.makedirs(SALIDA, exist_ok=True)
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=chrome) if chrome else pw.chromium.launch()
        pag = nav.new_page(viewport={"width": 1200, "height": 750})
        for slug, p in datos.items():
            pag.set_content(html(p))
            pag.screenshot(path=os.path.join(SALIDA, slug + ".jpg"), type="jpeg", quality=84)
        nav.close()
    print(len(datos), "portadas")

if __name__ == "__main__":
    main()
