import pickle
import numpy as np
import streamlit as st
from PIL import Image

#load save model
RFC=pickle.load(open('RFC_model.sav','rb'))
scale=pickle.load(open('scaler.pkl','rb'))

#judul web
st.title("prediksi kacang kering dengan RFC")
primaryColor="#F63366"
backgroundColor="#FFFFFF"
image= Image.open('kacang.png')
st.image(image)

#untuk input data
col1, col2=st.columns(2)
with col1:
    Area=st.text_input("Area")
    if Area != '':
        Area = float(Area)  # Konversi ke float
with col2:
    Perimeter=st.text_input("Perimeter")
    if Perimeter != '':
        Perimeter = float(Perimeter)  # Konversi ke float
with col1:
    MajorAxisLength=st.text_input("MajorAxisLength")
    if MajorAxisLength != '':
        MajorAxisLength = float(MajorAxisLength)  # Konversi ke float
with col2:
    MinorAxisLength=st.text_input("MinorAxisLength")
    if MinorAxisLength != '':
        MinorAxisLength = float(MinorAxisLength)  # Konversi ke float
with col1:
    AspectRation=st.text_input("AspectRation")
    if AspectRation != '':
        AspectRation = float(AspectRation)  # Konversi ke float
with col2:
    Eccentricity=st.text_input("Eccentricity")
    if Eccentricity != '':
        Eccentricity = float(Eccentricity)  # Konversi ke float
with col1:
    ConvexArea=st.text_input("ConvexArea")
    if ConvexArea != '':
        ConvexArea = float(ConvexArea)  # Konversi ke float
with col2:
    EquivDiameter=st.text_input("EquivDiameter")
    if EquivDiameter != '':
        EquivDiameter = float(EquivDiameter)  # Konversi ke float
with col1:
    Extent=st.text_input("Extent")
    if Extent != '':
        Extent = float(Extent)  # Konversi ke float
with col2:
    Solidility=st.text_input("Solidility")
    if Solidility != '':
        Solidility = float(Solidility)  # Konversi ke float
with col1:
    roundness=st.text_input("roundness")
    if roundness != '':
        roundness = float(roundness)  # Konversi ke float
with col2:
    Compactness=st.text_input("Compactness")
    if Compactness != '':
        Compactness = float(Compactness)  # Konversi ke float
with col1:
    ShapeFactor1=st.text_input("ShapeFactor1")
    if ShapeFactor1 != '':
        ShapeFactor1 = float(ShapeFactor1)  # Konversi ke float
with col2:
    ShapeFactor2=st.text_input("ShapeFactor2")
    if ShapeFactor2 != '':
        ShapeFactor2 = float(ShapeFactor2)  # Konversi ke float
with col1:
    ShapeFactor3=st.text_input("ShapeFactor3")
    if ShapeFactor3 != '':
        ShapeFactor3 = float(ShapeFactor3)  # Konversi ke float
with col2:
    ShapeFactor4=st.text_input("ShapeFactor4")
    if ShapeFactor4 != '':
        ShapeFactor4 = float(ShapeFactor4)  # Konversi ke float

#kode untuk predikisi
Prediksi_kacang_kering =''
if st.button("Prediksi Kacang kering SEKARANG"):
    # Mengubah argumen menjadi array numpy dua dimensi
    sc=scale.transform([[Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,ConvexArea,EquivDiameter]])
    # Melakukan prediksi dengan XGBoost
    Prediksi_kacang = RFC.predict([[sc[0][0],sc[0][1],sc[0][2],sc[0][3],sc[0][4],sc[0][5],sc[0][6],Eccentricity,Extent, Solidility, roundness, Compactness, ShapeFactor1, ShapeFactor2, ShapeFactor3, ShapeFactor4]])
    
    if Prediksi_kacang[0]==0:
        Prediksi_kacang_kering ="Barbunya"
    elif Prediksi_kacang[0] == 1:
        Prediksi_kacang_kering = "Bombay"
    elif Prediksi_kacang[0] == 2:
        Prediksi_kacang_kering = "Cali"
    elif Prediksi_kacang[0] == 3:
        Prediksi_kacang_kering = "Dermason"
    elif Prediksi_kacang[0] == 4:
        Prediksi_kacang_kering = "Horoz"
    elif Prediksi_kacang[0] == 5:
        Prediksi_kacang_kering = "Seker"
    elif Prediksi_kacang[0] == 6:
        Prediksi_kacang_kering = "Sira"
    else:
        Prediksi_kacang_kering = "tidak ditemukan jenis"

st.success(Prediksi_kacang_kering)

#teks
st.caption('Developer')
st.caption('Nunung Nurhasanah')
st.caption('Chyntia Traurina')
st.caption('Yazid Zinedine HDiana')