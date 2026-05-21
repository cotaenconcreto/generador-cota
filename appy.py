import streamlit as st
import google.generativeai as genai

# 1. CONFIGURACIÓN VISUAL BASADA EN TU MANUAL DE MARCA
st.set_page_config(page_title="Cota en Concreto - Escuela de Emprendedoras", page_icon="⚡", layout="centered")

# Estilos CSS para mantener tu identidad visual en la app de tus alumnas
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;700&display=swap');
    
    /* Fondo General: Azul/Violeta Corporativo de Cota (#4F5198) */
    .stApp {
        background-color: #4F5198 !important; 
        color: #F6F1CE !important; /* Texto claro crema */
        font-family: 'Inter', sans-serif;
    }
    
    /* Títulos principales: Magenta Corporativo (#BA007C) */
    h1, h2 {
        color: #BA007C !important;
        font-family: 'Archivo Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: -1px;
    }
    
    /* Subtítulos en Naranja/Siena (#D4803F) */
    h3, .highlight {
        color: #D4803F !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    
    /* Botón Principal */
    div.stButton > button:first-child {
        background-color: #BA007C !important;
        color: #F6F1CE !important;
        border-radius: 4px;
        border: 2px solid #D4803F !important;
        padding: 0.75rem 2.5rem;
        font-weight: bold;
        font-size: 18px;
        letter-spacing: 1px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        transition: all 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #D4803F !important;
        border-color: #BA007C !important;
        color: #4F5198 !important;
    }
    
    /* Campos de texto y selectores */
    .stTextInput input, .stTextArea textarea, .stSelectbox div {
        background-color: #383A75 !important;
        color: #F6F1CE !important;
        border: 1px solid #BA007C !important;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #2F3161 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. INTERFAZ EN PANTALLA
st.title("⚡ COTA EN CONCRETO")
st.subheader("Laboratorio de Contenido para Emprendedoras")
st.write("Escribí la estrategia y los copys para TU propia marca con el poder de la IA.")

st.markdown("---")

# Barra lateral para el control de créditos descentralizado
st.sidebar.header("🔑 Clave de Acceso Personal")
user_api_key = st.sidebar.text_input("Pegá tu API Key de Gemini:", type="password", help="Tu llave gratuita generada en Google AI Studio")
st.sidebar.markdown("[¿Cómo saco mi clave gratis en 1 minuto?](https://aistudio.google.com/)")

# 3. SELECTORES ADAPTADOS PARA CUALQUIER ALUMNA
st.markdown("### 🛠️ Configura tu pieza de contenido")

pilar = st.selectbox(
    "Seleccioná el pilar estratégico de TU marca:",
    [
        "Detrás de escena (El proceso creativo, el desorden real, el paso a paso de fabricación, el taller o espacio de trabajo)",
        "Tu Historia de Autor (Por qué creaste este emprendimiento, tu propósito, tus valores y qué te inspira a diseñar)",
        "Estilo y Beneficios (Cómo se usa el producto en el día a día, ideas de decoración, combinaciones de colores, propuesta de valor)",
        "Comunidad y Conexión (Agradecimientos, feedback de clientes, alianzas con otras marcas, valores compartidos)"
    ]
)

formato = st.selectbox(
    "Formato de salida:",
    ["Guion de Reel de Alta Retención (Scroll-stopper)", "Carrusel Educativo de Instagram (Paso a paso)", "Copy / Caption con Conexión Emocional"]
)

# Campo abierto para que CADA alumna ponga su producto
detalles_producto = st.text_area(
    "¿De qué producto, lanzamiento o idea específica vas a hablar hoy?",
    placeholder="Ej: El lanzamiento de mis nuevas velas artesanales, el stock de tazas de cerámica, cómo combino los colores de mis textiles...",
    height=120
)

# 4. BOTÓN DE ACCIÓN Y LÓGICA DE INTELIGENCIA ARTIFICIAL
if st.button("GENERAR CONTENIDO PARA MI MARCA 🚀"):
    if not user_api_key:
        st.error("❌ Falta la API Key en la barra lateral. Para que esta herramienta sea 100% gratuita y libre, ingresá tu clave personal.")
    elif not detalles_producto:
        st.warning("⚠️ Contame un poco sobre tu producto o la idea del post para que la IA pueda ayudarte.")
    else:
        with st.spinner("Modelando tus ideas... Preparando el contenido ✨"):
            try:
                genai.configure(api_key=user_api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Instrucciones para que la IA entienda que debe guiar a una alumna emprendedora
                prompt_sistema = f"""
                Actuá como un estratega experto en marketing digital para redes sociales, especialista en retención y copywriter premium para marcas de diseño de autor, artesanales y emprendimientos creativos.
                Estás ayudando a una alumna de la escuela de emprendedoras de 'Cota en Concreto' a escribir el contenido de SU propia marca.
                
                Tono de voz que vas a usar para armar el texto de la alumna: Apasionado por lo hecho a mano, auténtico, humano, creativo, cercano y muy directo. Evitá frases armadas, clichés de marketing tradicionales o palabras demasiado corporativas. Queremos conectar de verdad con la audiencia mostrando el valor del trabajo propio.
                
                Información del post que definió la alumna:
                - Pilar de contenido de su marca: {pilar}
                - Formato de post seleccionado: {formato}
                - Producto o tema central de su negocio: {detalles_producto}
                
                Estructura que debés devolver:
                1. Si pidió Guion de Reel: Armá un gancho atrapante para los primeros 3 segundos (scroll-stopper). Incluí sugerencias de planos visuales dinámicos (Ej: planos detalle, luz natural, paneo del proceso) para evitar que la audiencia deslice y se vaya del video, y cerrá con una llamada a la acción (CTA) que invite a comentar.
                2. Si pidió Carrusel: Indicá qué poner en cada placa (de la 1 a la 5) con títulos magnéticos.
                3. Si pidió Copy: Creá un texto estructurado con párrafos cortos, uso limpio de emojis y un cierre enfocado en comunidad.
                
                Escribí la respuesta de forma clara y directa en español latinoamericano (o rioplatense si el contexto del producto lo amerita), listo para que la alumna lo copie y use.
                """
                
                response = model.generate_content(prompt_sistema)
                
                st.markdown("---")
                st.markdown("## ✨ Tu Contenido Generado:")
                st.write(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"Hubo un problema al procesar tu clave o generar el texto. Verificá tu API Key. Detalle técnico: {e}")