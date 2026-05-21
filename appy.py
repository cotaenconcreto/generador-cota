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
st.write("Completa las opciones de abajo para diseñar una estrategia de comunicación completa y a tu medida.")

st.markdown
