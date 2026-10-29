"""Iconos de línea (viewBox 0 0 48 48) usados en portadas y en la sección de ejes de trabajo."""

ICONOS = {
    "fabrica": '<path d="M4 42V22l10 6v-6l10 6v-6l10 6V8h8v34z"/><path d="M4 42h40"/><path d="M12 35h4M22 35h4M32 35h4"/>',
    "grafica": '<path d="M6 42h36"/><path d="M10 42V30M19 42V22M28 42V26M37 42V14"/><path d="M8 24l10-8 9 5 14-12"/><path d="M34 9h7v7"/>',
    "globo": '<circle cx="24" cy="24" r="18"/><path d="M6 24h36"/><path d="M24 6c5 5 7.5 11 7.5 18S29 37 24 42c-5-5-7.5-11-7.5-18S19 11 24 6z"/><path d="M9 14h30M9 34h30"/>',
    "apreton": '<path d="M4 20l8-8 9 3 6-3 7 1 10 7"/><path d="M4 20l8 10"/><path d="M44 20l-8 10"/><path d="M14 31l4 4a2.5 2.5 0 0 0 4-3l-2-2"/><path d="M20 30l4 4a2.5 2.5 0 0 0 4-3l-3-3"/><path d="M25 28l3 3a2.5 2.5 0 0 0 4-3l-9-8-4 3a3 3 0 0 1-4-4l5-4"/>',
    "barco": '<path d="M6 34l4 8h28l4-8z"/><path d="M12 34V22h24v12"/><path d="M18 22v-8h12v8"/><path d="M24 14V6"/><path d="M4 44c3 0 3-2 6-2s3 2 6 2 3-2 6-2 3 2 6 2 3-2 6-2 3 2 6 2"/>',
    "monedas": '<ellipse cx="18" cy="12" rx="12" ry="5"/><path d="M6 12v8c0 2.8 5.4 5 12 5s12-2.2 12-5v-8"/><path d="M6 20v8c0 2.8 5.4 5 12 5"/><ellipse cx="30" cy="30" rx="12" ry="5"/><path d="M18 30v8c0 2.8 5.4 5 12 5s12-2.2 12-5v-8"/>',
    "tienda": '<path d="M6 18l4-10h28l4 10"/><path d="M6 18c0 3 2.5 5 6 5s6-2 6-5c0 3 2.5 5 6 5s6-2 6-5c0 3 2.5 5 6 5s6-2 6-5"/><path d="M9 23v19h30V23"/><path d="M20 42V31h8v11"/>',
    "sello": '<circle cx="24" cy="20" r="13"/><path d="M24 12l2.4 5 5.4.6-4 3.7 1.1 5.3L24 24l-4.9 2.6 1.1-5.3-4-3.7 5.4-.6z"/><path d="M16 30l-4 13 7-3 4 6 3-11"/><path d="M32 30l4 13-7-3-4 6"/>',
    "avion": '<path d="M44 8L4 22l14 5 5 15 6-11 9 6z"/><path d="M18 27L44 8"/>',
    "rayo": '<path d="M27 4L9 27h13l-3 17 18-23H24z"/>',
    "retrato": '<circle cx="24" cy="16" r="9"/><path d="M8 44c0-9 7-15 16-15s16 6 16 15"/>',
}

def svg(nombre, clase="", trazo=2.0):
    cuerpo = ICONOS.get(nombre, ICONOS["grafica"])
    return (f'<svg class="{clase}" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
            f'stroke-width="{trazo}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{cuerpo}</svg>')
