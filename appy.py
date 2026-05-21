import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURACIÓN VISUAL INTEGRAL - ESTÉTICA COTA CLARA Y PREMIUM
st.set_page_config(page_title="Cota en Concreto - Escuela de Emprendedoras", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600;700&display=swap');
    
    .stApp {
        background-color: #F6F1CE !important; 
        color: #2F3161 !important; 
        font-family: 'Inter', sans-serif;
    }
    h1 {
        color: #BA007C !important;
        font-family: 'Archivo Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: -1px;
        margin-bottom: 5px !important;
        font-size: 32px !important;
    }
    h3, .highlight {
        color: #D4803F !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        margin-top: 0px !important;
    }
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
    .output-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 8px;
        border-left: 5px solid #BA007C;
        color: #2F3161;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    }
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

# 3. CONFIGURACIÓN DEL CONTENIDO
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

# 4. BOTÓN DE ACCIÓN Y GENERACIÓN
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
            with st.spinner("Vaciando el molde... Preparando el contenido perfecto ✨"):
                try:
                    genai.configure(api_key=api_key_actual)
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    # Leemos las instrucciones de manera segura desde el archivo externo
                    if os.path.exists("prompt.txt"):
                        with open("prompt.txt", "r", encoding="utf-8") as f:
                            manifiesto = f.read()
                    else:
                        manifiesto = "Actuá como estratega de contenido de concreto."
                    
                    # Armamos la consulta inyectando las variables de forma limpia
                    instrucciones_finales = (
                        f"{manifiesto}\n\n"
                        f"DATOS DE LA Publicación:\n"
                        f"- Tipo de contenido seleccionado: {tipo_contenido}\n"
                        f"- Formato: {formato_contenido}\n"
                        f"- Tono requerido: {tono_comunicacion}\n"
                        f"- Llamado a la acción: {llamado_accion}\n"
                        f"- Idea/Producto: {detalles_producto}\n"
                    )
                    
                    response = model.generate_content(instrucciones_finales)
                    texto_completo = response.text
                    
                    parte_texto = "No se pudo generar el texto principal."
                    parte_visual = "No se pudieron generar las ideas visuales."
                    parte_estrategia = "No se pudo generar la estrategia."
                    
                    try:
                        if "[SECCION_TEXTO]" in texto_completo:
                            partes = texto_completo.split("[SECCION_TEXTO]")[1].split("[SECCION_VISUAL]")
                            parte_texto = partes[0].strip()
                            if len(partes) > 1:
                                sub_partes = partes[1].split("[SECCION_ESTRATEGIA]")
                                parte_visual = sub_partes[0].strip()
                                if len(sub_partes) > 1:
                                    parte_estrategia = sub_partes[1].strip()
                        else:
                            parte_texto = texto_completo
                    except:
                        parte_texto = texto_completo
                    
                    st.markdown("---")
                    st.markdown('<div class="output-box">', unsafe_allow_html=True)
                    
                    tab1, tab2, tab3 = st.tabs(["✍️ El Texto Listo", "📸 Dirección Visual", "💡 Ganchos y Estrategia"])
                    
                    with tab1:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.write(parte_texto)
                        
                    with tab2:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.write(parte_visual)
                        
                    with tab3:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.write(parte_estrategia)
                        
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"Hubo un problema al procesar la solicitud con el servidor: {e}")
