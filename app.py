import streamlit as st
import numpy as np
from st_pages import Page, show_pages

def sidebarPatern(Intro):
        st.image("assets\Brand.svg", width=200)
        st.markdown('### Introdução')
        st.markdown(Intro)

        st.markdown('### Navegação')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages\Analytics.py", label="Analítico", icon="💻")
        st.page_link("pages\dataviz.py", label="DataViz", icon="📊")
        st.page_link("https://github.com/sauloemp", label="Site", icon="🌐")

st.set_page_config(
    page_title="BC - SGC (Home)",
    page_icon= "assets\Logo.svg",
    initial_sidebar_state="expanded",
    layout='wide'
)

with st.sidebar:
    sidebarPatern('Esse é a proposição de projeto tirada do [kaggle- House Pricing in Belo Horizonte](https://www.kaggle.com/datasets/guilherme26/house-pricing-in-belo-horizonte/data). O objetivo desse projeto é pensar em um dash para que seja usado como portifólio.')
    #st.image("https://fronteimoveis.com.br/wp-content/uploads/2019/06/cropped-fronte-imoveis-logo.png", width=200)
    #st.markdown('### Introdução')
    #st.markdown('Esse é a proposição de projeto para a fronte imóveis. O objetivo desse projeto é pensar em novos modulos sempre para dá suporte ao time comercial.')

    #st.markdown('### Navegação')
    #st.page_link("app.py", label="Home", icon="🏠")
    #st.page_link("pages\Analytics.py", label="Analítico", icon="💻")
    #st.page_link("pages\dataviz.py", label="DataViz", icon="📊")#, disabled=True)
    #st.page_link("https://fronteimoveis.com.br/", label="Site Fronte", icon="🌐")
    #st.page_link(r"C:\Users\saulo\OneDrive\Documentos\Portifolio\Project Fronte\src\Analytics.py", label="Analítico", icon="💻", disabled=True)
    #hide_pages(["Another page"])


st.header("Sitema de Gestão Comercial - Fronte")
st.markdown("""---""")






st.markdown('''
### 📕Documentação

**Bem-vindo à nossa Plataforma: Aqui transformamos Dados em Insights Relevantes**

**Home:** A página inicial serve como um ponto de partida, apresentando um resumo simplificado das principais funcionalidades disponíveis em nossa plataforma.

**DataViz:** Aqui, oferecemos uma experiência visual impactante, onde os usuários podem identificar facilmente os lotes através de mapas interativos e informações de vendas detalhadas. Essa ferramenta é especialmente útil para a equipe executiva, fornecendo suporte valioso na tomada de decisões estratégicas.

**Analítico:** Esta seção é dedicada à análise detalhada dos dados. Aqui, os usuários têm a capacidade de explorar e manipular os dados em uma tabela dinâmica, permitindo que façam ajustes e observem imediatamente os reflexos dessas mudanças na tela de DataViz. É uma ferramenta poderosa para extrair insights significativos e personalizados.

**Site Fronte:** Nosso Site Fronte é a porta de entrada para informações sobre as próximas obras. Se alguém estiver interessado em saber mais sobre os projetos futuros, esta é a seção onde podem encontrar detalhes relevantes e atualizados.

Fique muito livre e Explore nossa plataforma e descubra como podemos ajudar a transformar seus dados em decisões inteligentes e estratégicas.
''')