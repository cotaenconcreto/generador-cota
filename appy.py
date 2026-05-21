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
    
    /* Inputs y Selectores limpios */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important; 
        color: #2F3161 !important; 
        border: 1px solid #D4803F !important; 
        border-radius: 6px !important;
        box-shadow: none !important; 
    }

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
st.write("Completa las opciones de abajo para diseñar una estrategia de comunicación completa.")

st.markdown("<br>", unsafe_allow_html=True)

# 3. CONFIGURACIÓN DEL CONTENIDO (Líneas revisadas y compactas anti-recortes)
tipo_contenido = st.selectbox(
    "1. Tipo de contenido:",
    [
        "Detrás de escena (Proceso, mezcla, desmolde, lijado)",
        "Inspiracional (Motivaciones, propósito, el valor artesanal)",
        "Educativo (Cómo cuidar las piezas, ideas de uso, datos útiles)",
        "Comunidad (Testimonios de clientes, mensajes lindos, gracias)"
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
    "4. ¿Qué querés que haga la audiencia al final?:",
    [
        "Que dejen un comentario",
        "Que me manden un mensaje directo (MD)",
        "Que vayan al link de la biografía (Tienda)",
        "Que guarden o compartan la publicación"
    ]
)

detalles_producto = st.text_area(
    "5. ¿De qué pieza o idea vas a hablar hoy?:",
    placeholder="Ej: Lanzamiento de bachas de baño, stock de macetas, porta velas...",
    height=120
)

st.markdown("<br>", unsafe_allow_html=True)

# 4. BOTÓN DE ACCIÓN Y GENERACIÓN CON EL CEREBRO ESTRATÉGICO
if st.button("GENERAR ESTRATEGIA COMPLETA 🚀"):
    if not detalles_producto:
        st.warning("⚠️ Por favor, escribe una breve descripción de tu idea o producto.")
    else:
        if "gemini_api_key" in st.secrets:
            api_key_actual = st.secrets["gemini_api_key"]
        else:
            api_key_actual = None

        if not api_key_actual:
            st.error("❌ Error de configuración: Falta cargar la clave en los Secrets de Streamlit.")
        else:
            # Aquí abrimos el bloque de carga de forma segura
            with st.spinner("Vaciando el molde... Preparando el contenido perfecto ✨"):
                try:
                    genai.configure(api_key=api_key_actual)
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    # Estructura limpia unida renglón por renglón para que nunca falle la sintaxis
                    instrucciones_base = (
                        "Actuá como un estratega premium de marketing digital y director de contenido especialista en marcas "
                        "de diseño de autor, decoración y objetos hechos artesanalmente en CONCRETO y CEMENTO. "
                        "Estás armando una propuesta de contenido para una alumna emprendedora de objetos de concreto.\n\n"
                        
                        "MANIFIESTO ESTRATÉGICO DEL TALLER (Reglas estrictas de comunicación):\n"
                        "1. EVITÁ EL POST CATÁLOGO: Entendés que el error número uno de las alumnas es mostrar solo una foto fija "
                        "del producto terminado creyendo que eso basta. Tu misión es obligarlas en la dirección visual y en el "
                        "texto a mostrar la magia del proceso creativo como el desorden del taller, las manos sucias, la mezcla, "
                        "el desmolde. El proceso aporta el verdadero valor.\n"
                        "2. ENFOQUE DE VENTA DIRECTA: Si la alumna elige este tono, NO generes un texto transaccional aburrido "
                        "o basado solo en precio. Enfocá la venta desde la perspectiva de que son piezas con carácter y "
                        "personalidad capaces de transformar por completo y cambiar un espacio en el hogar.\n"
                        "3. TRATAMIENTO DE IMPERFECCIONES (EL PORO): Si surge hablar de la textura, los poros, las marcas del "
                        "molde o las variaciones del cemento, tratalos con total naturalidad. No los defiendas con exageración "
                        "ni dejes que se noten como algo malo o un defecto. Es una propiedad misma del material con la que "
                        "hay que amigarse; denota autenticidad.\n"
                        "4. FILTRO ANTI-CLICHÉS: Prohibido usar frases hechas de Instagram que matan la identidad. NO uses "
                        "términos como piezas únicas, concreto con identidad, buscas el regalo ideal o llego el viernes. "
                        "Escribí de forma humana, directa y lo suficientemente abierta para que cada alumna pueda leerlo e "
                        "imprimirle su propio tono de voz al hablar.\n"
                        "5. CERO ARCILLA O CERÁMICA: Recordá que el oficio es concreto y cemento. Nada de hornos, tornos ni "
                        "modelado de arcilla desde cero con las manos. Usamos moldes, fraguado, vertido y lijado.\n\n"
                        
                        f"Variables seleccionadas por la alumna:\n"
                        f"- Tipo de contenido: {tipo_contenido}\n"
                        f"- Formato seleccionado: {formato_contenido}\n"
                        f"- Tono de comunicación requerido: {tono_comunicacion}\n"
                        f"- Objetivo/Llamado a la acción (CTA): {llamado_accion}\n"
                        f"- Detalles de su producto o idea: {detalles_producto}\n\n"
                        
                        "Tu respuesta DEBE estar dividida exactamente en estas 3 secciones utilizando títulos claros "
                        "(separa cada sección con marcadores estructurales como [SECCION_TEXTO], [SECCION_VISUAL],
