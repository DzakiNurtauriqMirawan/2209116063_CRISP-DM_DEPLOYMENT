import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import *
from function import *

# Dataframe
df = pd.read_csv('clothes_price_prediction_data.csv') # Ganti 'clothes_price_prediction_data.csv' dengan nama file yang sesuai
df = pd.read_csv('combined_data.csv')
df = pd.read_csv('data_before_mapping.csv')
df = pd.read_csv('data_cleaned.csv')

# Menambahkan gambar dengan lebar 500 piksel dan posisi yang ditengahkan
st.markdown(
    f"""
    <style>
    .centered {{
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}
    </style>
    """
    , unsafe_allow_html=True
)

# Judul sidebar
st.sidebar.title("Clothes Data Prediction")

# Menu-menu di sidebar
menu_options = ["Home", "Distribusi", "Hubungan", "Komposisi & Perbandingan","Predict" ]
selected_option = st.sidebar.radio("Menu", menu_options)

# Konten untuk setiap menu
if selected_option == "Home":
    st.title("Home")
    # Menampilkan gambar
    st.image("https://th.bing.com/th/id/OIP.xtyTF-r3PXcPdebfbBtMrgHaHa?rs=1&pid=ImgDetMain")
    st.subheader("Optimasi Harga Pakaian untuk Keuntungan dan Kepuasan Pelanggan")
    st.write("Proyek ini bertujuan untuk memprediksi harga pakaian dengan akurat untuk meningkatkan keuntungan perusahaan dan kepuasan pelanggan. Dengan strategi harga yang tepat, perusahaan dapat menyesuaikan harga dengan pasar, membangun kepercayaan pelanggan, dan mengelola stok dengan lebih efisien untuk memaksimalkan penjualan.")

    st.image("https://thumbs.dreamstime.com/b/clothing-store-interior-banner-woman-fitting-room-dress-modern-boutique-people-inside-trendy-accessories-vector-145570423.jpg")
    st.subheader("Pengembangan Model Prediktif untuk Penetapan Harga Pakaian")
    st.write("Dalam industri pakaian yang dinamis, penting untuk memahami pasar dan faktor internal perusahaan untuk mengembangkan model prediktif yang akurat dalam memprediksi harga item pakaian. Dengan menganalisis tren pasar, kualitas data, dan strategi bisnis, perusahaan dapat merancang pendekatan yang tepat untuk menyesuaikan strategi penetapan harga dengan efektif.")

elif selected_option == "Distribusi":
    st.title("Distribusi")
    # st.write("Ini adalah halaman untuk melihat distribusi data.")
    distribusi_barchart()
    
elif selected_option == "Hubungan":
    st.title("Hubungan")
    # st.write("Ini adalah halaman untuk melihat hubungan antara variabel.")
    relation(df)

elif selected_option == "Komposisi & Perbandingan":
    st.title("Komposisi & Perbandingan")
    # st.write("Ini adalah halaman untuk melihat komposisi data.")
    distribusi_piechart()

elif selected_option == "Predict":
    st.title("Predict")
    predict()
