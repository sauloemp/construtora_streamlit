import streamlit as st
import pandas as pd
#from src import utils as u
from app import sidebarPatern
import os

st.set_page_config(
    page_title="BC - SGC (Analítico)",
    page_icon= "assets\Logo.svg",
    initial_sidebar_state="expanded",
    layout='wide'
)

with st.sidebar:
    sidebarPatern(Intro = 'Essa é a pagina de controle e Cadatro dos imóveis')


with st.form(key = 'include_Property'):
    Address = st.text_input('Endereço', placeholder='Ex: Rua Clemente de ramos Barbosa')
    city = st.text_input('Cidade', placeholder='Ex: Belo Horizonte')
    cep = st.text_input('cep', placeholder='Ex: 50791060 (tente colocar só numeros)')
    complemento = st.text_input('Complemento', placeholder='Ex: Lote 3, Apt 13, sala 2')
    admfees = st.number_input('Taxa Administrativa', placeholder="Valor em R$", step= 0.01, value= None, min_value=0.)
    price = st.number_input('Preço do Terreno', placeholder="Valor em R$", step= 0.01, value= None, min_value=0.)
    garage = st.number_input('Vagas em Garagem', placeholder="Digite algum numero", step= 1, value= None, min_value=0)
    rooms = st.number_input('Quartos', placeholder="Digite algum numero", step= 1, value= None, min_value=0)
    sqrmeters = st.number_input('Metragem do Terreno: ', placeholder="Digite o tamanho do terreno em m²", step= 0.01, value= None, min_value=0.)
    latitude = st.number_input('Latitude', placeholder="Ex: -19.9364152", step= 0.00000001, value= None)
    longitude = st.number_input('Latitude', placeholder="Ex: -43.9533964", step= 0.00000001, value= None)
    statusLoot = st.radio("Status do Terreno:", ["Vendido", "Reservado", "Dísponivel"])

    if st.form_submit_button('Enviar dados'):
        if 'data' not in st.session_state:
            st.session_state.data = pd.DataFrame(columns=['endereco', 'cidade', 'cep', 'complemento', 'taxaAdm', 'preco', 'garagem', 'quartos', 'metrosQuadrados', 'lat', 'lon', 'status'])

        dados = {'endereco': Address, 
                'cidade': city, 
                'cep': cep, 
                'complemento': complemento, 
                'taxaAdm': admfees, 
                'preco': price, 
                'garagem': garage, 
                'quartos': rooms, 
                'metrosQuadrados': sqrmeters, 
                'lat': latitude, 
                'lon': longitude, 
                'status': statusLoot
            }
        df = pd.DataFrame(dados, index=[0]) if os.path.exists(os.path.join('dataset/data.csv')) == False else pd.read_csv('dataset/data.csv')
        st.session_state.data = pd.concat([st.session_state.data, df], ignore_index=True)
        st.success("Funcionário cadastrado com sucess!!!!")

    st.write('## Lista de Funcionários')
    if 'data' in st.session_state:
        st.write(st.session_state.data)        
        