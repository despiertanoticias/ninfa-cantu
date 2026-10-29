# ninfacantu.com

Sitio oficial de Ninfa Cantú Deándar, secretaria de Economía de Tamaulipas. Se compila con Python (`build.py`) y se edita desde **/admin** con [Decap CMS](https://decapcms.org/).

## Publicar

**Opción A: arrastrar el .zip (rápido).** Ejecuta `python3 build.py --zip` y arrastra `ninfacantu-sitio.zip` a https://app.netlify.com/drop o, en un sitio existente, a *Deploys › Deploy manually*. Con esta opción el sitio se ve completo, pero **/admin no puede guardar cambios** porque no hay repositorio conectado.

**Opción B: conectar este repositorio (recomendada para usar /admin).**
1. En Netlify: *Add new project › Import an existing project › GitHub* › `despiertanoticias/ninfa-cantu`. La compilación ya está configurada en `netlify.toml`. Si ya subiste el .zip, puedes conectar el repositorio a ese mismo sitio en *Project configuration › Build & deploy › Link repository*.
2. *Domain management* › agrega `ninfacantu.com`.
3. *Identity* › **Enable Identity** › registro **Invite only** › *Services* › **Enable Git Gateway**.
4. *Identity › Invite users* con tu correo, acepta la invitación y entra a https://ninfacantu.com/admin/.

Cada cambio guardado en /admin se publica solo en uno o dos minutos.

## Qué se edita desde /admin

| Panel | Qué cambia | Archivo |
|---|---|---|
| Noticias | Notas, portada, categoría, fuente | `content/noticias/*.md` |
| Información de Ninfa › Perfil y biografía | Cargo, lema, foto, biografía, cifras, mensaje, correo y redes | `content/datos/perfil.json` |
| Información de Ninfa › Trayectoria y cargos | Línea de tiempo | `content/datos/trayectoria.json` |
| Información de Ninfa › Ejes de trabajo y proyectos | Ejes e íconos, proyectos estratégicos | `content/datos/ejes.json` |
| Información de Ninfa › Ajustes del sitio | Título, descripción y orden de temas | `content/datos/sitio.json` |

## Trabajar en local

```bash
pip install -r requirements.txt
python3 build.py            # genera _site/
python3 -m http.server -d _site 8000
```

## Herramientas

- `herramientas/notas_iniciales.py`: las 30 notas iniciales, redactadas a partir de notas de prensa (cada una enlaza a su fuente).
- `herramientas/portadas.py`: genera las portadas con cifra clave (requiere Playwright).
