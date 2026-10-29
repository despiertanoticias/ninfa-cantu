"""Genera las 30 notas iniciales del sitio (content/noticias/*.md).

Cada nota resume, con redacción propia, información publicada por medios de
comunicación. La fuente original queda enlazada al pie de cada nota.
Uso: python3 herramientas/notas_iniciales.py
"""
import os, json

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "content", "noticias")

N = []
def nota(slug, fecha, categoria, titulo, resumen, cuerpo, fuente, url, portada, destacada=False):
    N.append(dict(slug=slug, fecha=fecha, categoria=categoria, titulo=titulo, resumen=resumen,
                  cuerpo=cuerpo.strip(), fuente=fuente, url=url, portada=portada, destacada=destacada))

# ---------------------------------------------------------------- 2026
nota("superissste-y-microcreditos-para-mipymes", "2026-09-05", "MiPyMEs",
 "Empresas tamaulipecas llegan a SuperISSSTE y microcréditos alcanzan a 36 municipios",
 "Once empresas del estado presentaron sus productos a SuperISSSTE, mientras los programas de microcrédito superaron los 31.9 millones de pesos en el primer semestre.",
 """
La estrategia económica del Gobierno de Tamaulipas, en la que participa la Secretaría de Economía encabezada por Ninfa Cantú Deándar, se ha enfocado en generar confianza entre el sector empresarial y en respaldar a las micro, pequeñas y medianas empresas.

Como parte de ese trabajo, once empresas tamaulipecas participaron en un proceso de vinculación con SuperISSSTE para ofrecer productos elaborados en el estado, entre ellos alimentos, artículos de limpieza, miel, quesos y salsas.

En el primer semestre de 2026 se destinaron más de 31.9 millones de pesos a través de los programas de Microcrédito y Financiamiento, que beneficiaron a 1,265 emprendedores y dueños de negocios en 36 municipios.
""", "La Crónica de Hoy", "https://www.cronica.com.mx/estados/2026/09/05/estrategia-de-americo-villarreal-impulsa-el-crecimiento-economico-de-tamaulipas",
 dict(icono="tienda", cifra="1,265", etiqueta="emprendedores apoyados en 36 municipios"))

nota("tamaulipas-mayor-contribucion-crecimiento-nacional", "2026-07-30", "Economía",
 "Tamaulipas, el estado que más aportó al crecimiento nacional en el primer trimestre",
 "Con un avance de 5.2%, la economía tamaulipeca encabezó la contribución al crecimiento del país, según el indicador estatal del INEGI.",
 """
La economía de Tamaulipas creció 5.2% durante el primer trimestre de 2026, de acuerdo con el Indicador Trimestral de la Actividad Económica Estatal (ITAEE) del INEGI. Con ese resultado, el estado se colocó como el de mayor contribución al crecimiento económico nacional en el periodo.

La secretaria de Economía, Ninfa Cantú Deándar, afirmó que la cifra confirma la solidez de la economía estatal y atribuyó el resultado al esfuerzo conjunto de los sectores productivos, de las y los trabajadores y a la estrategia de desarrollo impulsada por el gobernador Américo Villarreal Anaya.

Por sectores, las actividades primarias avanzaron 16.5%, las secundarias 9.4% y las terciarias 1.1%.

En lo que va de la administración, la inversión suma alrededor de 21 mil millones de dólares en 174 proyectos confirmados. Entre las obras estratégicas destacan el Puerto Norte de Matamoros, el Puerto del Interior en Victoria y el Polo de Desarrollo para el Bienestar en Altamira, este último en coordinación con el Gobierno de México.
""", "La Crónica de Hoy", "https://www.cronica.com.mx/estados/2026/07/30/tamaulipas-se-coloca-como-el-estado-de-mayor-contribucion-al-crecimiento-de-la-economia-nacional-en-el-primer-trimestre-de-2026/",
 dict(icono="grafica", cifra="5.2%", etiqueta="crecimiento en el primer trimestre de 2026"), destacada=True)

nota("nafin-y-bancomext-consejo-consultivo-tamaulipas", "2026-07-10", "MiPyMEs",
 "Alianza con Nafin y Bancomext: 910 créditos y cerca de 20 mil empleos conservados",
 "En la primera sesión del Consejo Consultivo de Nafin y Bancomext en Tamaulipas se presentaron los resultados de Crédito Impulso y Fondo Tamaulipas.",
 """
Ninfa Cantú Deándar participó en la Primera Sesión del Consejo Consultivo de Nacional Financiera (Nafin) y Bancomext en Tamaulipas, realizada en el Palacio de Gobierno de Ciudad Victoria.

Ahí destacó que la colaboración con Nafin ya muestra resultados: desde agosto de 2023, el programa Crédito Impulso ha otorgado 910 financiamientos a empresas comerciales, industriales y de servicios en 19 municipios, lo que ha ayudado a conservar cerca de 20 mil empleos.

Además, en los últimos tres años Fondo Tamaulipas ha colocado cerca de 2 mil millones de pesos en créditos productivos, un monto equivalente a lo que entregaron en conjunto las dos administraciones estatales anteriores.
""", "La Crónica de Hoy", "https://www.cronica.com.mx/estados/2026/07/10/nafin-y-tamaulipas-fortalecen-alianza-para-impulsar-empresas-y-proyectos-estrategicos/",
 dict(icono="monedas", cifra="910", etiqueta="créditos de Crédito Impulso en 19 municipios"))

nota("tamaulipas-y-espana-agenda-de-inversion", "2026-06-16", "Internacional",
 "Tamaulipas y España construyen una agenda conjunta de inversión y cooperación",
 "La secretaria se reunió con el embajador de España en México, Juan Duarte Cuadrado, en el marco del Acuerdo Global Modernizado entre México y la Unión Europea.",
 """
Ninfa Cantú Deándar sostuvo una reunión de trabajo con el embajador de España en México, Juan Duarte Cuadrado, para fortalecer la cooperación económica, comercial y tecnológica entre Tamaulipas y España.

Durante el encuentro, la secretaria expuso las oportunidades del estado en los sectores agroindustrial y agroalimentario, en innovación y transferencia tecnológica, en gestión del agua y en economía circular. También se habló de los clústeres automotriz y de tecnologías de la información.

Ambas partes acordaron integrar una agenda conjunta para promover inversiones y colaboraciones, y dar seguimiento a los temas en una próxima visita del embajador a la entidad.

En la reunión participaron también Anabell Flores Garza, subsecretaria de Inversión; Luis Armando Cantú, subsecretario de Desarrollo Sostenible, Competitividad y Comercio Exterior; Víctor Landa Ríos, director general de Planeación, e Iris Franciolli, representante en la Ciudad de México.
""", "La Crónica de Hoy", "https://www.cronica.com.mx/estados/2026/06/16/tamaulipas-busca-fortalecer-lazos-de-inversion-y-cooperacion-con-espana/",
 dict(icono="apreton", cifra="España", etiqueta="agenda conjunta de inversión"))

nota("europa-pone-la-mirada-en-tamaulipas", "2026-05-27", "Internacional",
 "Europa pone la mirada en Tamaulipas: 89 empresas y más de 12 mil millones de dólares",
 "Ninfa Cantú Deándar destacó las ventajas del estado ante el nuevo Acuerdo Global Modernizado entre México y la Unión Europea.",
 """
La secretaria de Economía de Tamaulipas señaló que el Acuerdo Global Modernizado entre México y la Unión Europea abre una oportunidad para estrechar los lazos comerciales y de cooperación con Europa, una relación que, dijo, se ha fortalecido en los últimos años.

En Tamaulipas operan 89 empresas originarias de 10 países de la Unión Europea, con una inversión acumulada que supera los 12 mil millones de dólares. Europa aporta el 16% de la inversión extranjera directa que recibe el estado, con Alemania y Francia a la cabeza.

Entre las ventajas de la entidad, Cantú Deándar mencionó las energías limpias, la movilidad, la industria farmacéutica, la digitalización y su ubicación logística para el comercio internacional.

Recientemente, una comisión de 18 embajadores y representantes de la Unión Europea visitó el estado para dialogar sobre energía, medio ambiente, comercio, agua, educación, seguridad y desarrollo económico.
""", "El Mañana", "https://www.elmanana.com.mx/estado/2026/5/27/europa-pone-la-mirada-en-tamaulipas-destaca-ninfa-cantu-deandar-ventajas-para-nuevas-inversiones-177157.html",
 dict(icono="globo", cifra="89", etiqueta="empresas europeas operan en Tamaulipas"))

nota("cumbre-empresarial-mexico-union-europea", "2026-05-26", "Internacional",
 "Tamaulipas presenta 180 proyectos de inversión en la Cumbre Empresarial México–UE",
 "La Secretaría de Economía promovió al estado como destino de inversión y anunció la creación de los clústeres automotriz y eléctrico-electrónico.",
 """
La Secretaría de Economía de Tamaulipas, que encabeza Ninfa Cantú Deándar, participó en la Cumbre Empresarial México–Unión Europea celebrada en la Ciudad de México, con el objetivo de posicionar al estado como destino de inversión y ampliar sus alianzas comerciales. La subsecretaria de Inversión, Anabell Flores Garza, acudió en representación de la secretaria.

En el encuentro se informó que Tamaulipas cuenta con 180 proyectos de inversión privada confirmados, entre nuevas inversiones y ampliaciones de empresas ya establecidas.

Se presentaron como proyectos estratégicos el Puerto Interior de Ciudad Victoria, concebido como polo industrial y logístico, y el fortalecimiento del puerto de Altamira. También se anunció la creación del Clúster Automotriz de Tamaulipas y del Clúster Eléctrico-Electrónico.
""", "Cluster Industrial", "https://clusterindustrial.com.mx/tamaulipas-impulsa-180-proyectos-de-inversion-y-fortalece-alianzas-con-europa/",
 dict(icono="fabrica", cifra="180", etiqueta="proyectos de inversión confirmados"))

nota("hecho-en-tamaulipas-y-reactivacion-spelman", "2026-04-21", "MiPyMEs",
 "Hecho en Tamaulipas supera 3,300 solicitudes y se gestiona la reactivación de Spelman",
 "La secretaria informó sobre la recuperación de empleos tras el incendio en Spelman y los avances de los programas de apoyo a productores locales.",
 """
Ninfa Cantú Deándar, originaria de Nuevo Laredo, informó que se obtuvieron los permisos federales para reactivar a la empresa Spelman tras el incendio que afectó sus instalaciones, lo que permitiría recuperar alrededor de 300 empleos en el corto plazo.

También detalló que el programa Hecho en Tamaulipas superó este año las 3,300 solicitudes y ha otorgado más de 100 distintivos a productores locales.

Por su parte, los programas de microcrédito y financiamiento han canalizado cerca de 700 millones de pesos a pequeñas y medianas empresas del estado.

La secretaria reiteró que su prioridad es el trabajo al frente de la Secretaría de Economía estatal.
""", "POSTA México", "https://www.posta.com.mx/tamaulipas/buscara-ninfa-cantu-la-alcaldia-de-nuevo-laredo/vl2193053",
 dict(icono="sello", cifra="3,300", etiqueta="solicitudes a Hecho en Tamaulipas"))

nota("mipymes-ruta-para-la-formalidad", "2026-04-13", "MiPyMEs",
 "Las MiPyMEs, la vía para combatir la informalidad en Tamaulipas",
 "La secretaria planteó incentivos financieros a través de Fondo Tamaulipas para que más negocios se sumen a la economía formal.",
 """
La transición hacia la formalidad es una tarea pendiente para Tamaulipas, reconoció Ninfa Cantú Deándar, quien explicó que la estrategia estatal se centra en fortalecer a las micro, pequeñas y medianas empresas como principal vía para reducir la actividad informal.

Para ello, el gobierno estatal ofrece incentivos financieros a través de Fondo Tamaulipas, que este año ha entregado más de 6 millones de pesos en microcréditos, a los que se sumarán recursos del proyecto Impulso.

La secretaria destacó que en lo que va del año se han generado casi 2,500 empleos en Ciudad Victoria y que se observan tendencias positivas en Tampico y Reynosa.
""", "POSTA México", "https://www.posta.com.mx/tamaulipas/tamaulipas-enfrenta-informalidad-y-rezago-en-comercio-y-servicios/vl2189580",
 dict(icono="tienda", cifra="2,500", etiqueta="empleos en Ciudad Victoria en 2026"))

# ---------------------------------------------------------------- 2025
nota("crecimiento-economico-segundo-trimestre-2025", "2025-10-29", "Economía",
 "La economía de Tamaulipas crece 3.3% en el segundo trimestre de 2025",
 "Los sectores primario y secundario impulsaron el resultado, que la secretaria atribuyó a la confianza de las empresas en el estado.",
 """
Tamaulipas registró un crecimiento anual de 3.3% en su actividad económica durante el segundo trimestre de 2025, según el Indicador Trimestral de la Actividad Económica Estatal del INEGI.

El sector primario creció 6.8% y el secundario 5.8%. Ninfa Cantú Deándar explicó que el resultado es fruto de la política económica estatal, basada en la confianza, el apoyo y el impulso a la inversión.

La secretaria señaló que el gobierno estatal respalda a la industria establecida y financia a micro, pequeñas y medianas empresas para fortalecer el empleo. Durante la administración se han confirmado 151 proyectos de inversión por alrededor de 20 mil millones de dólares.
""", "POSTA México", "https://www.posta.com.mx/tamaulipas/crecimiento-economico-de-tamaulipas-2025-alcanza-33/vl2117574",
 dict(icono="grafica", cifra="3.3%", etiqueta="crecimiento en el segundo trimestre de 2025"))

nota("visita-del-embajador-de-la-union-europea", "2025-09-26", "Internacional",
 "Visita del embajador de la Unión Europea confirma el interés europeo en Tamaulipas",
 "Durante la visita de tres días del embajador Francisco André, la secretaria presentó las cifras de inversión europea en el estado.",
 """
El embajador de la Unión Europea en México, Francisco André, realizó una visita de tres días a Tamaulipas. Durante su estancia, Ninfa Cantú Deándar expuso que en el estado operan 89 empresas de 10 países europeos, con inversiones que superan los 12 mil millones de dólares.

La secretaria informó además que las inversiones de la Unión Europea concretadas durante la administración del gobernador Américo Villarreal suman 151 millones de dólares y han generado más de 1,100 empleos, principalmente en los sectores eléctrico, electrónico y automotriz.
""", "MEXICONOW", "https://mexico-now.com/?p=33991",
 dict(icono="globo", cifra="US$151 M", etiqueta="inversión europea en la administración"))

nota("mision-comercial-estados-unidos-y-canada", "2025-08-28", "Internacional",
 "Misión comercial reúne a más de 100 empresas de Estados Unidos y Canadá",
 "La secretaria encabezó un encuentro para posicionar a Tamaulipas como destino de inversión y comercio en Norteamérica.",
 """
Ninfa Cantú Deándar encabezó una misión comercial con más de 100 empresas de Estados Unidos y Canadá de los sectores de energía, salud, minería, tecnologías de la información, manufactura, telecomunicaciones y consultoría.

El encuentro se organizó junto con la Secretaría de Economía federal y los gobiernos municipales de Altamira y Nuevo Laredo, con el respaldo de sus alcaldes, Armando Martínez y Carmen Lilia Canturosas.

A los participantes se les presentaron los proyectos de Puerto Norte, Puerto Seco, Puerto Altamira y el Programa Energético de Tamaulipas. La secretaria reiteró el compromiso del estado con la atracción de inversión productiva y la cooperación internacional.
""", "La Crónica de Hoy", "https://www.cronica.com.mx/estados/2025/08/28/tamaulipas-impulsa-inversion-con-empresas-de-eu-y-canada/",
 dict(icono="globo", cifra="+100", etiqueta="empresas de EUA y Canadá"))

nota("crecimiento-sin-cancelacion-de-proyectos", "2025-08-07", "Economía",
 "Tamaulipas crece 2.3% en 2025 sin cancelación de proyectos de inversión",
 "La secretaria destacó la creación de 1,400 empleos formales y el papel de Reynosa como el municipio con mayor inversión captada.",
 """
Tamaulipas mantiene un crecimiento de 2.3% en 2025, impulsado por capital nacional y extranjero y sin cancelaciones de proyectos, informó Ninfa Cantú Deándar.

De acuerdo con el INEGI, el estado ocupó el cuarto lugar nacional por crecimiento económico en el primer trimestre del año, con 239 millones de dólares en inversiones. Reynosa fue el municipio que más inversión captó en el último año.

La secretaria reportó la creación de 1,400 empleos formales en Reynosa, Altamira, Nuevo Laredo y Ciudad Victoria, y recordó los apoyos de Fondo Tamaulipas y del plan Impulso para las MiPyMEs. Sobre la inseguridad, sostuvo que se trata de una percepción que no se refleja en los datos económicos.
""", "POSTA México", "https://www.posta.com.mx/tamaulipas/tamaulipas-registra-un-crecimiento-economico-del-23-en-el-ano-a-pesar-de-la-percepcion-de-seguridad/vl2077822",
 dict(icono="grafica", cifra="1,400", etiqueta="empleos formales en cuatro municipios"))

nota("inteva-amplia-planta-en-matamoros", "2025-07-10", "Inversión",
 "INTEVA invertirá 8 millones de dólares en Matamoros y creará 500 empleos",
 "La empresa automotriz anunció la ampliación de su planta con el acompañamiento de la Secretaría de Economía estatal.",
 """
La empresa automotriz INTEVA anunció una inversión de 8 millones de dólares para ampliar su planta en Matamoros, con la que se prevé generar 500 empleos directos.

En el anuncio, al que asistió el alcalde Alberto Granados, Ninfa Cantú Deándar calificó la inversión como un voto de confianza en el potencial productivo y el talento de Matamoros, y como muestra de que Tamaulipas sigue siendo atractivo para la industria global.
""", "MEXICONOW", "https://mexico-now.com/?p=33327",
 dict(icono="fabrica", cifra="500", etiqueta="empleos directos en Matamoros"))

nota("altamira-polo-de-desarrollo-economico", "2025-05-24", "Inversión",
 "Altamira, designado Polo de Desarrollo Económico para el Bienestar",
 "Para la secretaria, la designación federal del puerto de Altamira confirma el papel estratégico de Tamaulipas en el desarrollo nacional.",
 """
El secretario de Economía federal, Marcelo Ebrard, anunció la designación del puerto de Altamira como Polo de Desarrollo Económico para el Bienestar (PODECOBI), una de las zonas del Plan México que ofrecen infraestructura estratégica, beneficios fiscales y facilidades administrativas para atraer inversión.

Ninfa Cantú Deándar señaló que la decisión reconoce el enorme potencial del puerto y confirma el papel estratégico de Tamaulipas en el desarrollo económico del país.

La secretaria explicó que el estado trabaja en coordinación con la Secretaría de Economía federal y los municipios, y que se preparan incentivos para la inversión en maquinaria y equipo, capacitación técnica en modelo dual y programas de innovación.
""", "Mexico Daily Post", "https://mexicodailypost.news/2025/05/24/tamaulipas-strengthens-its-industrial-leadership-with-altamira-as-a-development-hub-ninfa-cantu",
 dict(icono="barco", cifra="Altamira", etiqueta="Polo de Desarrollo para el Bienestar"))

nota("tamaulipas-en-famex-2025", "2025-04-28", "Internacional",
 "Tamaulipas lleva su oferta industrial a la Feria Aeroespacial México 2025",
 "La Secretaría de Economía encabezó el pabellón del estado con participación de los sectores público, privado y académico.",
 """
La Secretaría de Economía de Tamaulipas encabezó la participación del estado en la Feria Aeroespacial México (FAMEX) 2025, celebrada del 23 al 26 de abril en la Base Aérea Militar No. 1 de Santa Lucía.

Ninfa Cantú Deándar explicó que la presencia conjunta de los sectores público, privado y académico forma parte de una estrategia para promover la inversión en la región. La feria reunió a 337 empresas y a representantes de 48 países.
""", "MEXICONOW", "https://mexico-now.com/?p=32683",
 dict(icono="avion", cifra="48", etiqueta="países presentes en FAMEX 2025"))

nota("comparecencia-tercer-informe", "2025-04-04", "Gestión",
 "Comparecencia ante el Congreso por el Tercer Informe de Gobierno",
 "La secretaria presentó ante las y los diputados los avances económicos del estado y reiteró su compromiso con la transparencia.",
 """
Ninfa Cantú Deándar compareció ante el Congreso de Tamaulipas para exponer el apartado económico del Tercer Informe de Gobierno.

Ante las y los legisladores, presentó los principales avances de la estrategia económica estatal y reafirmó su compromiso con la transparencia y con el trabajo coordinado con los sectores productivos del estado.
""", "Sentido Común (vía Ground News)", "https://groundnews.lakegeneva.lib.wi.us/article/we-build-a-stronger-more-competitive-tamaulipas-with-a-more-promising-future-secretariat-of-economy",
 dict(icono="retrato", cifra="3er Informe", etiqueta="comparecencia ante el Congreso"))

nota("walmart-anuncia-inversion-en-tamaulipas", "2025-03-10", "Inversión",
 "Walmart de México invertirá 2,500 millones de pesos en más de 20 tiendas",
 "La secretaria acompañó al gobernador en la reunión donde la empresa presentó su plan, que generará más de 1,300 empleos directos.",
 """
Walmart de México anunció una inversión de 2,500 millones de pesos para abrir más de 20 nuevas tiendas en Tamaulipas, con las que se generarán más de 1,300 empleos directos.

Ninfa Cantú Deándar acompañó al gobernador Américo Villarreal en la reunión en la que directivos de la empresa presentaron el plan. La secretaria agradeció la confianza en el estado y aseguró que el gobierno estatal seguirá facilitando su crecimiento.

El proyecto contempla además un programa de apoyo a pequeños productores agrícolas y acciones para desarrollar proveedores locales. Walmart cuenta hoy con 77 unidades en el estado, donde emplea a más de 3,800 personas.
""", "La Razón", "https://www.razon.com.mx/estados/2025/03/10/walmart-de-mexico-anuncia-inversion-de-2-mil-500-mdp-en-tamaulipas/",
 dict(icono="tienda", cifra="$2,500 M", etiqueta="pesos de inversión en más de 20 tiendas"))

nota("primer-lugar-nacional-en-crecimiento-industrial", "2025-02-13", "Economía",
 "Tamaulipas, primer lugar nacional en crecimiento industrial",
 "El indicador mensual del INEGI registró un aumento anual de 12.7%, impulsado por la manufactura y la minería.",
 """
Tamaulipas se colocó en el primer lugar nacional en crecimiento industrial, con un aumento anual de 12.7% según el Indicador Mensual de la Actividad Industrial del INEGI.

Ninfa Cantú Deándar explicó que el avance se debe al dinamismo de la manufactura y la minería, al aumento de pedidos de mercados internacionales, a la expansión de empresas establecidas y a nuevos proyectos de inversión.

La secretaria precisó que el 60% de los proyectos de inversión confirmados en el estado está ligado a la actividad industrial, que emplea a cerca de 465 mil personas, el 28% de la población ocupada.
""", "Mexico Daily Post", "https://mexicodailypost.news/2025/02/13/tamaulipas-ranks-first-in-industrial-growth-in-the-entire-country",
 dict(icono="fabrica", cifra="12.7%", etiqueta="crecimiento industrial anual"))

nota("nidec-inaugura-ampliacion-en-reynosa", "2025-01-20", "Inversión",
 "NIDEC inaugura ampliación en Reynosa con 23 millones de dólares",
 "La empresa celebró 20 años de operaciones en Reynosa con una ampliación que suma 384 nuevos empleos.",
 """
NIDEC inauguró la ampliación de su planta en Reynosa, con una inversión de 23 millones de dólares y 384 nuevos empleos, en el marco de sus 20 años de operaciones en la ciudad.

La Secretaría de Economía de Tamaulipas, encabezada por Ninfa Cantú Deándar, estuvo representada en la ceremonia por la subsecretaria de Inversión, Anabell Flores Garza. La inversión había sido anunciada en julio de 2024.
""", "MEXICONOW", "https://mexico-now.com/?p=31745",
 dict(icono="fabrica", cifra="US$23 M", etiqueta="ampliación de NIDEC en Reynosa"))

# ---------------------------------------------------------------- 2024
nota("corredores-y-sectores-del-bienestar", "2024-12-05", "Inversión",
 "Tamaulipas presenta 128 proyectos de inversión en reunión con Marcelo Ebrard",
 "En la Primera Reunión Institucional de Corredores y Sectores del Bienestar, la secretaria expuso los proyectos prioritarios del estado.",
 """
Ninfa Cantú Deándar participó en la Primera Reunión Institucional de Corredores y Sectores del Bienestar, junto al secretario de Economía federal, Marcelo Ebrard, para coordinar esfuerzos en desarrollo económico y generación de empleo.

La secretaria presentó los proyectos prioritarios del gobierno del estado: la modernización de los puentes internacionales, la infraestructura hidráulica y de conectividad, y la modernización del Puerto Norte en Matamoros y del Puerto Seco en Ciudad Victoria.

Tamaulipas cuenta con 128 proyectos de inversión confirmados en sectores como el automotriz, eléctrico, electrónico, semiconductores y energía, por casi 19,584 millones de dólares y 36,750 empleos. Además, hay 129 proyectos potenciales con capital de Norteamérica, Europa, Asia y Sudamérica.
""", "EL CEO", "https://elceo.com/politica/tamaulipas-apunta-a-consolidarse-como-polo-industrial-del-pais/",
 dict(icono="fabrica", cifra="128", etiqueta="proyectos confirmados, 36,750 empleos"))

nota("ciudad-victoria-suma-unidades-economicas", "2024-12-05", "Economía",
 "Ciudad Victoria suma 2,682 nuevas unidades económicas desde 2022",
 "La capital del estado llega a 15,624 establecimientos y siete proyectos industriales prevén 63 millones de dólares de inversión.",
 """
Con datos del Directorio Estadístico Nacional de Unidades Económicas del INEGI, Ninfa Cantú Deándar informó que Ciudad Victoria cuenta con 15,624 unidades económicas, 2,682 más que en 2022.

La secretaria atribuyó el aumento a la confianza y el optimismo de las y los emprendedores, y destacó la llegada de nuevas sucursales de cadenas comerciales a la capital.

En la zona centro del estado, siete proyectos industriales representan alrededor de 63 millones de dólares de inversión en los próximos años. A nivel estatal, la población ocupada creció en 29,708 personas en un año, hasta sumar 1,658,004.
""", "MEXICONOW", "https://mexico-now.com/?p=31482",
 dict(icono="grafica", cifra="15,624", etiqueta="unidades económicas en Ciudad Victoria"))

nota("mision-empresarial-brasil-y-colombia", "2024-11-26", "Internacional",
 "Misión empresarial de Brasil y Colombia llega a la región de Los Dos Laredos",
 "La secretaria invitó a empresas sudamericanas a aprovechar el nearshoring desde Tamaulipas.",
 """
Ninfa Cantú Deándar participó en la Misión Empresarial de Brasil y Colombia a la región de Los Dos Laredos, con el objetivo de fortalecer los lazos comerciales y establecer acuerdos para nuevas misiones de negocios en 2025.

La secretaria destacó a Nuevo Laredo como la aduana más importante de América Latina e invitó a las empresas brasileñas y colombianas a invertir en Tamaulipas, por su ubicación, infraestructura y mano de obra industrial.

Participaron la Confederación de Asociaciones Comerciales y Empresariales de Brasil, el municipio de Mogi das Cruzes, organismos de Colombia y Brasil, instituciones financieras y la Laredo Development Corporation.
""", "Mexico Daily Post", "https://mexicodailypost.news/2024/11/26/tamaulipas-strengthens-trade-ties-with-brazil-and-colombia/",
 dict(icono="apreton", cifra="Brasil y Colombia", etiqueta="misión empresarial en Los Dos Laredos"))

nota("coordinadora-region-noreste-amsde", "2024-11-20", "Gestión",
 "Ninfa Cantú, coordinadora de la Región Noreste de la AMSDE",
 "La Asociación Mexicana de Secretarios de Desarrollo Económico la nombró coordinadora de la región que integran cinco estados.",
 """
La Asociación Mexicana de Secretarios de Desarrollo Económico (AMSDE) nombró a Ninfa Cantú Deándar coordinadora de su Región Noreste, integrada por Coahuila, Durango, Nuevo León, Sinaloa y Tamaulipas.

El nombramiento se dio a conocer durante una sesión ordinaria de la asociación, en la que también hubo un encuentro con el secretario de Economía federal, Marcelo Ebrard.

La secretaria expresó que asumir esta responsabilidad es un honor en un momento crucial para la región, y que impulsará proyectos conjuntos de conectividad, infraestructura y desarrollo económico para elevar la competitividad, el desarrollo industrial y la inversión.
""", "MEXICONOW", "https://mexico-now.com/?p=31326",
 dict(icono="retrato", cifra="AMSDE", etiqueta="coordinadora de la Región Noreste"))

nota("expansiones-nidec-y-erika-en-reynosa", "2024-08-13", "Inversión",
 "Expansiones de NIDEC y Erika en Reynosa suman 33 millones de dólares",
 "La secretaria atribuyó el crecimiento industrial a la cooperación entre sectores productivos, asociaciones maquiladoras y el gobierno estatal.",
 """
La industria de Tamaulipas creció 2.6% anual en abril, según el Indicador Mensual de la Actividad Industrial del INEGI. Ninfa Cantú Deándar atribuyó el avance a la cooperación entre los sectores productivos, las asociaciones de la industria maquiladora (INDEX) de Reynosa, Nuevo Laredo y Matamoros, y el gobierno estatal.

La secretaria señaló que la industria establecida está creciendo y que más empresas llegan al estado. Como ejemplo, citó las expansiones de NIDEC y Erika en Reynosa, con una inversión conjunta de 33 millones de dólares y más de 1,500 empleos.
""", "MEXICONOW", "https://mexico-now.com/?p=30339",
 dict(icono="fabrica", cifra="1,500", etiqueta="empleos por expansiones en Reynosa"))

nota("crece-economia-primer-trimestre-2024", "2024-07-31", "Economía",
 "Crece la economía de Tamaulipas en el primer trimestre de 2024",
 "El sector primario avanzó 5.2% y el de comercio y servicios 2.6%, impulsados por el apoyo a MiPyMEs.",
 """
La economía de Tamaulipas creció 1.4% en el primer trimestre de 2024, de acuerdo con el ITAEE del INEGI. El sector primario se expandió 5.2% y el terciario, de comercio y servicios, 2.6%.

Ninfa Cantú Deándar señaló que estos incrementos reflejan la confianza en el desarrollo económico del estado, y atribuyó parte del avance en comercio y servicios al financiamiento, la capacitación y el acompañamiento técnico que el gobierno estatal brinda a las MiPyMEs, a través de Fondo Tamaulipas y del programa Hecho en Tamaulipas.
""", "POSTA México", "https://www.posta.com.mx/mexico/crece-economia-de-tamaulipas-en-primer-trimestre-de-2024/vl1598344",
 dict(icono="grafica", cifra="5.2%", etiqueta="crecimiento del sector primario"))

nota("medline-inaugura-planta-en-nuevo-laredo", "2024-02-23", "Inversión",
 "Medline inaugura planta en Nuevo Laredo con 930 empleos",
 "La nueva planta Medline Hudson RCI, en el Parque Industrial Oradel, representa una inversión de 16.2 millones de dólares.",
 """
Ninfa Cantú Deándar participó en la inauguración de la planta Medline Hudson RCI en el Parque Industrial Oradel de Nuevo Laredo, con una inversión de 16.2 millones de dólares y empleo para 930 personas.

La secretaria presentó el proyecto como resultado de la política estatal para crear condiciones favorables al crecimiento empresarial, y como muestra de la confianza de los inversionistas en la región. Medline opera en Tamaulipas desde 1988.
""", "POSTA México", "https://www.posta.com.mx/mexico/medline-invierte-16-2-millones-de-dolares-en-tamaulipas/vl1546990",
 dict(icono="fabrica", cifra="930", etiqueta="empleos en Nuevo Laredo"))

nota("electromovilidad-industria-estrategica", "2024-02-13", "Inversión",
 "La electromovilidad, industria estratégica para Tamaulipas",
 "En la North America Mobility & Net Zero Summit 2024, la secretaria habló de nearshoring sustentable junto a cónsules de Estados Unidos y Canadá.",
 """
En la North America Mobility & Net Zero Summit 2024, Ninfa Cantú Deándar afirmó que la electromovilidad es una industria estratégica para Tamaulipas, capaz de atraer inversión extranjera, impulsar la transferencia de tecnología y fortalecer los lazos comerciales.

La secretaria participó en el panel inaugural sobre nearshoring sustentable, junto a los cónsules generales de Estados Unidos y Canadá en Monterrey. Ahí destacó los beneficios del nearshoring en crecimiento, empleo, infraestructura y diversificación económica, y reconoció retos como la competitividad laboral, la protección ambiental y el desarrollo regional equitativo.
""", "MEXICONOW", "https://mexico-now.com/?p=28377",
 dict(icono="rayo", cifra="Net Zero", etiqueta="nearshoring sustentable"))

# ---------------------------------------------------------------- 2023 y 2022
nota("balance-primer-ano-inversiones", "2023-11-23", "Inversión",
 "Primer año de gestión: 82 proyectos de inversión y más de 20 mil empleos",
 "La secretaria presentó el balance de inversiones por región y anunció la llegada de nuevas sucursales de Farmacias del Ahorro.",
 """
Ninfa Cantú Deándar informó que en el último año se registraron alrededor de 18,336 millones de dólares de inversión en 82 proyectos, que generaron 20,048 empleos en los sectores automotriz, electrónico, químico, aeroespacial, logístico, médico, de semiconductores y de alimentos.

Por región, Matamoros sumó 17 proyectos, principalmente en hidrocarburos; Reynosa, 27 proyectos por 583 millones de dólares; Nuevo Laredo, 18 proyectos por 224 millones; Altamira, 13 proyectos por 5,300 millones, y Victoria, seis proyectos por 63 millones.

La secretaria también dio a conocer la apertura de once sucursales de Farmacias del Ahorro, con 14 más previstas para los primeros meses de 2024.
""", "POSTA México", "https://www.posta.com.mx/mexico/suma-tamaulipas-inversiones-por-mas-de-18-millones-de-dolares/v-vl1521625",
 dict(icono="grafica", cifra="20,048", etiqueta="empleos en el primer año"))

nota("mision-empresarial-asia-time-interconnect", "2023-11-08", "Internacional",
 "Desde China, anuncia inversión de 40 millones de dólares para Reynosa",
 "Durante la Misión Empresarial Asia 2023, la secretaria anunció la llegada de Time Interconnect Technology con más de 500 empleos.",
 """
En el marco de la Misión Empresarial Asia 2023 en China, Ninfa Cantú Deándar anunció que la empresa Time Interconnect Technology se instalará en Reynosa con una inversión de 40 millones de dólares.

La planta producirá cables y accesorios para las industrias automotriz, de telecomunicaciones, centros de datos y equipo médico, y generará más de 500 empleos en su fase final.

Durante la gira, la secretaria participó en la Cumbre China–América Latina en Pekín y en un encuentro de importadores en Shanghái. También refrendó el trabajo conjunto con la McAllen Economic Development Corporation para atraer inversiones.
""", "Cluster Industrial", "https://clusterindustrial.com.mx/time-interconnect-technology-invertira-40-mdd-en-tamaulipas/",
 dict(icono="globo", cifra="US$40 M", etiqueta="inversión para Reynosa"))

nota("designada-secretaria-de-desarrollo-economico", "2022-09-26", "Gestión",
 "Designada titular de Desarrollo Económico en el gabinete de Américo Villarreal",
 "El gobernador electo presentó a la neolaredense como responsable de la política económica del estado a partir de octubre de 2022.",
 """
El entonces gobernador electo Américo Villarreal Anaya presentó a su gabinete, en el que designó a Ninfa Cantú Deándar como titular de la Secretaría de Desarrollo Económico de Tamaulipas, hoy Secretaría de Economía.

Originaria de Nuevo Laredo, Cantú Deándar es licenciada en Ciencias de la Comunicación y empresaria. Antes de su nombramiento dirigió el Instituto Municipal de la Mujer de Nuevo Laredo y fue coordinadora estatal de Cofinece Tamaulipas.
""", "El Mañana", "https://elmanana.com.mx/estado/2022/9/27/anuncia-americo-su-gabinete-83513.html",
 dict(icono="retrato", cifra="2022", etiqueta="inicia su gestión al frente de la economía estatal"))


def escribir():
    os.makedirs(DESTINO, exist_ok=True)
    portadas = {}
    for n in N:
        img = f"/assets/uploads/portadas/{n['slug']}.jpg"
        fm = [
            "---",
            f"title: {json.dumps(n['titulo'], ensure_ascii=False)}",
            f"date: {n['fecha']}",
            f"categoria: {n['categoria']}",
            f"imagen: {img}",
            f"resumen: {json.dumps(n['resumen'], ensure_ascii=False)}",
            f"destacada: {'true' if n['destacada'] else 'false'}",
            f"fuente_nombre: {json.dumps(n['fuente'], ensure_ascii=False)}",
            f"fuente_url: {n['url']}",
            "---",
            "",
        ]
        with open(os.path.join(DESTINO, n["slug"] + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + n["cuerpo"] + "\n")
        portadas[n["slug"]] = dict(n["portada"], categoria=n["categoria"], fecha=n["fecha"])
    with open(os.path.join(RAIZ, "herramientas", "portadas.json"), "w", encoding="utf-8") as f:
        json.dump(portadas, f, ensure_ascii=False, indent=1)
    print(len(N), "notas")

if __name__ == "__main__":
    escribir()
