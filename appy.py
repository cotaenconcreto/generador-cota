import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURACIÓN VISUAL INTEGRAL - ESTÉTICA COTA PREMIUM
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
    
    /* Encabezado Principal */
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
    
    /* Estilizado para los contenedores nativos de Streamlit */
    div[data-testid="stVerticalBlockBorderWithStyling"] {
        background-color: #FFFFFF !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04) !important;
        border: 1px solid #EAEAEA !important;
        margin-bottom: 10px !important;
    }
    
    /* Títulos de sección */
    .section-title {
        color: #2F3161;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }

    /* Inputs estilizados */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #F9F9F9 !important; 
        color: #2F3161 !important; 
        border: 1px solid #E2E8F0 !important; 
        border-radius: 8px !important;
    }

    label p {
        color: #4A5568 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    
    /* Botón de Acción Principal */
    div.stButton > button:first-child {
        background-color: #BA007C !important; 
        color: #FFFFFF !important;
        border-radius: 8px;
        border: none !important;
        padding: 0.8rem 2.5rem;
        font-weight: 700;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0px 4px 10px rgba(186, 0, 124, 0.2);
        transition: all 0.2s ease;
        width: 100%; 
        margin-top: 10px;
    }
    div.stButton > button:first-child:hover {
        background-color: #D4803F !important;
