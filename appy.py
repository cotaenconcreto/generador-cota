import streamlit as st
import google.generativeai as genai

# 1. CONFIGURACIÓN VISUAL INTEGRAL - ESTÉTICA COTA CLARA Y PREMIUM
st.set_page_config(page_title="Cota en Concreto - Escuela de Emprendedoras", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600;700&display=swap');
    
    /* Fondo Tono Crema Claro de Cota (#F6F1CE) */
    .stApp {
        background-color: #F6F1CE !important; 
        color: #2F3161 !important; 
        font-family: 'Inter', sans-serif;
    }
    
    /* Título: Magenta Corporativo (#BA007C) */
    h1 {
        color: #BA007C !important;
        font-family: 'Archivo Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: -1px;
        margin-bottom: 5px !important;
        font-size: 32px !important;
    }
    
    /* Subtítulo: Naranja/Siena (#D4803F) */
    h3, .highlight {
        color: #D4803F !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        margin-top: 0px !important;
    }
    
    /* Inputs y Selectores limpios (Fondo blanco liso, borde Siena) */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important; 
        color: #2F3161 !important; 
        border: 1px solid #D4803F !important; 
        border-radius: 6px !important;
        box-shadow: none !important; 
    }

    /* Etiquetas de los campos */
    label p {
        color: #2F3161 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    
    /* Botón Principal Sólido Magenta */
    div.stButton > button:first-child {
        background-color: #BA007C !important; 
        color: #FFFFFF !important;
        border-radius: 6px;
        border: none !important;
        padding: 0.75rem 2.5rem;
        font-weight: 700;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0px 2px 5px rgba(186, 0, 124, 0.2);
        transition: all 0.2s ease;
        width: 100%; 
    }
    div.stButton > button:first-child:hover {
        background-color: #D4803F !important; 
        color: #FFFFFF !important;
    }
    
    /* Caja de resultado limpia */
    .output-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 8px;
        border-left: 5px solid #BA007C;
        color: #2F3161;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    }

    /* Estilo para las pestañas */
    .stTabs [data-baseweb="tab"] {
        color: #2F3161 !important;
        font-weight: 600 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #BA007C !important;
        border-bottom-color: #BA007C !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. INTERFAZ EN PANTALLA
st.title("⚡ Crea tu contenido estratégico")
st.subheader("Laboratorio de Contenido para Emprendedoras")
st.write("Completa las opciones de abajo de forma simple para diseñar una estrategia de comunicación completa y a tu medida.")

st.markdown("<br>", unsafe_allow_html=True)

# 3. CONFIGURACIÓN DEL CONTENIDO INTUITIVO Y ENFOCADO
tipo_contenido = st.selectbox(
    "1. Selecciona el tipo de contenido:",
    [
        "Detrás de escena (Tu proceso de mezcla, llenado, el momento del desmolde o el lijado final)",
        "Inspiracional (Tus motivaciones, por qué elegiste el concreto, el valor del diseño de autor hecho a mano)",
        "Educativo (Cómo cuidar las piezas de cemento, ideas de decoración en casa, impermeabilización o datos útiles)",
        "Comunidad (Testimonios de clientes que ya tienen tus piezas en su hogar, mensajes bonitos, alianzas)"
    ]
)

formato_contenido = st.selectbox(
    "2. Formato de contenido:",
    ["Guión de reel", "Carrusel", "Copy de publicación"]
)

tono_comunicacion = st.selectbox(
    "3. Tono de comunicación:",
    ["Cálido y amigable", "Venta directa", "Divertido", "Inspirador"]
)

llamado_accion = st.selectbox(
    "4. ¿Qué querés que haga la audiencia al terminar de leer? (Llamado a la acción):",
    [
        "Que dejen un comentario",
        "Que me manden un mensaje directo (MD)",
        "Que vayan al link de la biografía (Tienda)",
        "Que guarden o compartan la publicación"
    ]
)

detalles_producto = st.text_area(
    "5. ¿De qué producto, lanzamiento o idea específica vas a hablar hoy?",
    placeholder="Ej: Lanzamiento de mi línea de bachas de baño, stock de macetas color block, porta velas rústicos...",
    height=120
)

st.markdown("<br>", unsafe_allow_html=True)

# 4. BOTÓN DE ACCIÓN Y GENERACIÓN CON EL NUEVO CEREBRO ESTRATÉGICO
if st.button("GENERAR ESTRATEGIA COMPLETA 🚀"):
    if not detalles_producto:
        st.warning("⚠️ Por favor, escribe una breve descripción de tu idea o producto para poder redactar.")
    else:
        if "gemini_api_key" in st.secrets:
            api_key_actual = st.secrets["gemini_api_key"]
        else:
            api_key_actual = None

        if not api_key_actual:
            st.error("❌ Error de configuración: Falta cargar la clave en el servidor de Streamlit (Secrets).")
        else:
            with st.spinner("Vaciando el molde... Preparando el contenido perfecto ✨"):
                try:
                    genai.configure(api_key=api_key_actual)
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    # FILTROS Y REGLAS INTERNAS ACORDES A TUS DEFINICIONES
                    prompt_sistema = f"""
                    Actuá como un estratega premium de marketing digital y director de contenido especialista en marcas de diseño de autor, decoración y objetos hechos artesanalmente en CONCRETO y CEMENTO.
                    Estás armando una propuesta de contenido para una alumna emprendedora de objetos de concreto.

                    MANIFIESTO ESTRATÉGICO DEL TALLER (Reglas estrictas de comunicación):
                    1. EVITÁ EL POST CATÁLOGO: Entendés que el error número uno de las alumnas es mostrar solo una foto fija del producto terminado creyendo que eso basta. Tu misión es obligarlas en la dirección visual y en el texto a mostrar 'la magia del proceso creativo' (el desorden del taller, las manos sucias, la mezcla, el desmolde). El proceso aporta el verdadero valor.
                    2. ENFOQUE DE VENTA DIRECTA: Si la alumna elige este tono, NO generes un texto transaccional aburrido o basado solo en precio. Enfocá la venta desde la perspectiva de que son 'piezas con carácter y personalidad' capaces de transformar por completo y cambiar un espacio en el hogar.
                    3. TRATAMIENTO DE IMPERFECCIONES (EL PORO): Si surge hablar de la textura, los poros, las marcas del molde o las variaciones del cemento, tratalos con total naturalidad. No los defiendas con exageración ni dejes que se noten como algo malo o un defecto. Es una propiedad misma del material con la que hay que amigarse; denota autenticidad.
                    4. FILTRO ANTI-CLICHÉS: Prohibido usar frases hechas de Instagram que matan la identidad y suenan todas igual. NO uses términos como 'piezas únicas', 'concreto con identidad', '¿buscás el regalo ideal?' o 'llegó el viernes'. Escribí de forma humana, directa y lo suficientemente abierta para que cada alumna pueda leerlo e imprimirle su propio tono de voz al hablar.
                    5. CERO ARCILLA O CERÁMICA: Recordá que el oficio es concreto/cemento. Nada de hornos, tornos ni modelado de arcilla desde cero con las manos. Usamos moldes, fraguado, vertido y lijado.

                    Variables seleccionadas por la alumna:
                    - Tipo de contenido: {tipo_contenido}
                    - Formato seleccionado: {formato_contenido}
                    - Tono de comunicación requerido: {tono_comunicacion}
                    - Objetivo/Llamado a la acción (CTA): {llamado_accion}
                    - Detalles de su producto o idea: {detalles_producto}

                    Tu respuesta DEBE estar dividida exactamente en estas 3 secciones utilizando títulos claros (separa cada sección con marcadores estructurales como [SECCION_TEXTO], [SECCION_VISUAL], [SECCION_ESTRATEGIA]):

                    [SECCION_TEXTO]
                    Generá el contenido final listo para copiar. Modulá el estilo estrictamente al tono '{tono_comunicacion}' de forma natural y fresca. Incluí un cierre integrado orgánicamente que cumpla con el llamado a la acción: '{llamado_accion}'.
                    - Si es Guión de reel: Estructura segundo a segundo enfocada en dinamismo visual y audio. Con un gancho fuerte que
