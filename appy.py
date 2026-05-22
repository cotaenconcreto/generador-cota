import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURACIÓN VISUAL INTEGRAL - ESTÉTICA COTA PREMIUM COHESIVA
st.set_page_config(page_title="Cota en Concreto - Escuela de Emprendedoras", page_icon="⚡", layout="centered")

# Inyección directa y segura de estilos sin lectura de archivos conflictivos
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600;700&display=swap'); .stApp { background-color: #F6F1CE !important; color: #2F3161 !important; font-family: 'Inter', sans-serif; } h1 { color: #BA007C !important; font-family: 'Archivo Black', sans-serif; text-transform: uppercase; letter-spacing: -1px; margin-bottom: 5px !important; font-size: 32px !important; } h3, .highlight { color: #D4803F !important; font-family: 'Inter', sans-serif; font-weight: 700; margin-top: 0px !important; } div[data-testid='stVerticalBlockBorderWithStyling'] { background-color: #FFFFFF !important; padding: 20px !important; border-radius: 12px !important; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04) !important; border: 1px solid #EAEAEA !important; margin-bottom: 10px !important; } .section-title { color: #2F3161; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; } .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb='select'] { background-color: #F9F9F9 !important; color: #2F3161 !important; border: 1px solid #E2E8F0 !important; border-radius: 8px !important; } label p { color: #4A5568 !important; font-weight: 600 !important; font-size: 14px !important; } div.stButton > button:first-child { background-color: #BA007C !important; color: #FFFFFF !important; border-radius: 8px; border: none !important; padding: 0.8rem 2.5rem; font-weight: 700; font-size: 16px; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0px 4px 10px rgba(186, 0, 124, 0.2); transition: all 0.2s ease; width: 100%; margin-top: 10px; } div.stButton > button:first-child:hover { background-color: #D4803F !important; } .output-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; border-left: 5px solid #BA007C; color: #2F3161; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); } .stTabs [data-baseweb='tab'] { color: #2F3161 !important; font-weight: 600 !important; } .stTabs [data-baseweb='tab'][aria-selected='true'] { color: #BA007C !important; border-bottom-color: #BA007C !important; }</style>", unsafe_allow_html=True)

# 2. INTERFAZ EN PANTALLA
st.title("⚡ Crea tu contenido estratégico")
st.subheader("Laboratorio de Contenido para Emprendedoras")
st.write("Completa los bloques de abajo para diseñar la comunicación de tus piezas de concreto.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BLOQUE 1: TU PRODUCTO
with st.container(border=True):
    st.markdown('<div class="section-title">📦 TU PRODUCTO Y FORMATO</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        tipo_contenido = st.selectbox(
            "1. Tipo de contenido:",
            [
                "Detrás de escena (Proceso, mezcla, desmolde, lijado)",
                "Inspiracional (Motivaciones, propósito, el valor artesanal)",
                "Educativo (Cómo cuidar las piezas, ideas de uso, datos útiles)",
                "Comunidad (Testimonios de clientes, mensajes lindos, gracias)"
            ]
        )
    with col2:
        formato_contenido = st.selectbox(
            "2. Formato de contenido:",
            ["Guión de reel", "Carrusel", "Copy de publicación"]
        )
    detalles_producto = st.text_area(
        "3. ¿De qué pieza o idea vas a hablar hoy?:",
        placeholder="Ej: Lanzamiento de bachas de baño, stock de macetas, porta velas...",
        height=120
    )

# 4. BLOQUE 2: ESTRATEGIA Y CIERRE
with st.container(border=True):
    st.markdown('<div class="section-title">💡 TONO Y OBJETIVO</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        tono_comunicacion = st.selectbox(
            "4. Tono de comunicación:",
            ["Cálido y amigable", "Venta directa", "Divertido", "Inspirador"]
        )
    with col4:
        llamado_accion = st.selectbox(
            "5. Llamado a la acción (Objetivo):",
            [
                "Que dejen un comentario",
                "Que me manden un mensaje directo (MD)",
                "Que vayan al link de la biografía (Tienda)",
                "Que guarden o compartan la publicación"
            ]
        )

# 5. BOTÓN DE ACCIÓN Y GENERACIÓN
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
                    
                    if os.path.exists("prompt.txt"):
                        with open("prompt.txt", "r", encoding="utf-8") as f:
                            manifiesto = f.read()
                    else:
                        manifiesto = "Actuá como estratega de contenido de concreto."
                    
                    instrucciones_finales = (
                        f"{manifiesto}\n\n"
                        f"DATOS DE LA PUBLICACIÓN:\n"
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
