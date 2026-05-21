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

    /* Etiquetas de los campos en color oscuro legible */
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
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #BA007C;
        color: #2F3161;
    }
    </style>
""", unsafe_allow_html=True)

# 2. INTERFAZ EN PANTALLA (Textos actualizados)
st.title("⚡ Crea tu contenido estratégico")
st.subheader("Laboratorio de Contenido para Emprendedoras")
st.write("Completa las opciones de abajo de forma simple para diseñar los textos de tu marca en un clic.")

st.markdown("<br>", unsafe_allow_html=True)

# 3. CONFIGURACIÓN DEL CONTENIDO (Menús limpios sin tecnicismos)
tipo_contenido = st.selectbox(
    "Selecciona el tipo de contenido:",
    ["Detrás de escena", "Inspiracional", "Educativo/usos", "Comunidad"]
)

formato_contenido = st.selectbox(
    "Formato de contenido:",
    ["Guión de reel", "Carrusel", "Copy de publicación"]
)

detalles_producto = st.text_area(
    "¿De qué producto, lanzamiento o idea específica vas a hablar hoy?",
    placeholder="Ej: El stock de tazas de cerámica, el lanzamiento de mis nuevas velas, cómo combino los colores de mis productos...",
    height=120
)

st.markdown("<br>", unsafe_allow_html=True)

# 4. BOTÓN DE ACCIÓN Y GENERACIÓN
if st.button("GENERAR CONTENIDO PARA MI MARCA 🚀"):
    if not detalles_producto:
        st.warning("⚠️ Por favor, escribe una breve descripción de tu idea o producto para poder redactar.")
    else:
        # Recuperar la API key cargada en los secretos de Streamlit
        if "gemini_api_key" in st.secrets:
            api_key_actual = st.secrets["gemini_api_key"]
        else:
            api_key_actual = None

        if not api_key_actual:
            st.error("❌ Error de configuración: Falta cargar la clave en el servidor de Streamlit (Secrets).")
        else:
            with st.spinner("Modelando tus ideas... Diseñando el texto perfecto ✨"):
                try:
                    genai.configure(api_key=api_key_actual)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # El prompt traduce las opciones simples en instrucciones avanzadas de marketing
                    prompt_sistema = f"""
                    Actuá como un estratega experto en marketing digital para redes sociales y copywriter premium para marcas de diseño de autor, artesanales y emprendimientos creativos.
                    Estás ayudando a una alumna de la escuela de emprendedoras a escribir el contenido de SU propia marca.
                    
                    Tono de voz final del texto generado: Apasionado por lo hecho a mano, auténtico, humano, creativo, cercano y muy directo. Evitá frases armadas cliché de marketing tradicional o palabras corporativas aburridas. Queremos conectar de verdad con la audiencia mostrando el valor del trabajo propio.
                    
                    Selecciones de la alumna:
                    - Tipo de contenido: {tipo_contenido} (Nota: 'Detrás de escena' refiere a procesos, fabricación o espacio; 'Inspiracional' a la historia, el propósito o la motivación; 'Educativo/usos' a cómo se usa el producto o ideas de combinación; 'Comunidad' a feedback, alianzas o agradecimientos).
                    - Formato seleccionado: {formato_contenido}
                    - Producto o tema central de su negocio: {detalles_producto}
                    
                    Estructura obligatoria según el formato seleccionado:
                    1. Si eligió 'Guión de reel': Armá un guión audiovisual paso a paso. Empezá con un gancho atrapante en los primeros 3 segundos (frase fuerte que frene el scroll). Incluí sugerencias de planos visuales dinámicos que muestren el proceso o el producto bajo luz natural, y terminá con una llamada a la acción clara para generar comentarios.
                    2. Si eligió 'Carrusel': Indicá con total claridad qué poner en cada placa (de la 1 a la 5) con títulos magnéticos y un cierre interactivo en la última placa.
                    3. Si eligió 'Copy de publicación': Creá un texto estructurado con párrafos cortos, renglones espaciados, uso limpio de emojis acordes al diseño y un cierre enfocado en comunidad.
                    
                    Escribí la respuesta de forma clara, directa y lista para que la alumna la copie y la use en su Instagram. Usa español latinoamericano o rioplatense fresco.
                    """
                    
                    response = model.generate_content(prompt_sistema)
                    
                    st.markdown("---")
                    st.markdown(f'<div class="output-box"><h3>✨ Tu Contenido Generado:</h3><br>{response.text}</div>', unsafe_allow_html=True)
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"Hubo un problema al procesar la solicitud con el servidor: {e}")
