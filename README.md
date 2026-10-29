# ninfacantu.com

Sitio oficial de Ninfa Cantú de Andar. Hecho con [Eleventy](https://www.11ty.dev/) y editable desde **/admin** con [Decap CMS](https://decapcms.org/).

## Qué se edita desde /admin

| Sección del panel | Qué cambia en el sitio | Archivo |
|---|---|---|
| Noticias | Notas, agenda, comunicados y opinión | `src/noticias/*.md` |
| Información de Ninfa › Perfil y biografía | Cargo actual, lema, foto, biografía, datos destacados, correo y redes | `src/_data/perfil.json` |
| Información de Ninfa › Trayectoria y cargos | Línea de tiempo de cargos | `src/_data/trayectoria.json` |
| Información de Ninfa › Ajustes del sitio | Título y descripción para buscadores | `src/_data/sitio.json` |

Cada cambio guardado en el panel se convierte en un commit en `main`, y Netlify vuelve a publicar el sitio en uno o dos minutos.

## Puesta en marcha en Netlify (una sola vez)

1. **Conectar el repositorio:** en Netlify, *Add new project › Import an existing project › GitHub* y elige `despiertanoticias/ninfa-cantu`. La configuración de compilación ya está en `netlify.toml` (comando `npm run build`, carpeta `_site`).
2. **Dominio:** *Domain management › Add a domain* › `ninfacantu.com`. Apunta el DNS como indique Netlify y espera a que se active HTTPS.
3. **Activar Identity:** *Project configuration › Identity › Enable Identity*.
   - *Registration preferences* › **Invite only** (para que nadie más pueda registrarse).
   - *Services › Git Gateway* › **Enable Git Gateway**.
4. **Invitar editores:** *Identity › Invite users* con el correo de quien va a editar. Al abrir el correo de invitación se crea la contraseña.
5. Entra a **https://ninfacantu.com/admin/** e inicia sesión.

## Trabajar en local

```bash
npm install
npm start   # http://localhost:8080
```

## Estructura

```
src/
  _data/        perfil, trayectoria y ajustes (JSON editables)
  _includes/    plantilla base, nota y componentes
  noticias/     una nota por archivo .md
  admin/        panel Decap CMS (config.yml)
  assets/       estilos, logo, foto e imágenes subidas
```
