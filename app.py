import streamlit as st
import pandas as pd
import os
import datetime
import re
from langchain_groq import ChatGroq

# Sayfa Ayarları
st.set_page_config(page_title="Tubitak Llama - Okul Asistanı", page_icon="🎓")
st.title("🎓 Okul Ders Asistanı")

# API Anahtarı (Streamlit Secrets'tan alacağız)
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
else:
    st.error("Lütfen Streamlit Cloud üzerinden API anahtarını ekleyin!")

# Veriyi Yükle
@st.cache_data
def load_data():
    return pd.read_csv('SinifProgrami1404.csv', sep=';')

df = load_data()
llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)

# Senin yazdığın o harika asistan fonksiyonu (Streamlit uyumlu)
def ogrenci_asistani(soru):
    # (Buraya Colab'daki 'ogrenci_asistani_kesin_cozum' fonksiyonunu aynen yapıştır)
    # Sadece print() yerine return kullanmaya devam et.
    pass 

# Arayüz
soru = st.text_input("Sorunu buraya yaz (Örn: 9-A yarın ilk ders ne?)")

if soru:
    with st.spinner('Düşünüyorum...'):
        yanit = ogrenci_asistani(soru)
        st.chat_message("assistant").write(yanit)
