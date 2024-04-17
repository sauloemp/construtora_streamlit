import streamlit as st
import pandas as pd
import plotly.express as px
import folium
import streamlit_folium as stf
import numpy as np
from app import sidebarPatern

def get_cohort_color(cohort):
    color = {
        'Muito Alto': "#08306B",
        'Alto' : "#2171B5",
        'Médio': "#6BAED6",
        'Baixo' : '#9ECAE1',
        'Muito Baixo': '#CECECE'
    }

    if cohort in color:
        return color[cohort]
    else:
        # Defina uma cor padrão (opcional)
        return "#FFFFFF"


st.set_page_config(
    page_title="BC - Imóveis BH",
    page_icon= "assets\Logo.svg",
    initial_sidebar_state="expanded",
    layout='wide'
)

st.header("Analises de Preço de Imóveis -BH")
st.markdown("""---""")



@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

dataframe = load_data('dataset/cleaned_data.csv')
MaxValuePriceNonFiltered = np.count_nonzero(dataframe.price)

df = dataframe



with st.sidebar:
    sidebarPatern(Intro = 'Essa é uma aplicação que visa apresentar os preços dos imóveis. entretanto é facimente pode facilmente ser utilizada para visualizar disponibilidade de lotes conforme esse link: [PolyLine Folium](https://python-visualization.github.io/folium/latest/user_guide/ui_elements/popups.html)')
    st.markdown('### Filtros')
    PriceFilter = st.slider('💵Preço do Imóvel', np.min(df['price']), np.max(df['price']), (np.min(df['price']),np.max(df['price'])))
    SqtFilter = st.slider('📏Imóveis m²', np.min(df['square-foot']), np.max(df['square-foot']), (np.min(df['square-foot']),np.max(df['square-foot'])))
    GarageFilter = st.slider('🚘Vagas de Garagem', np.min(df['garage-places']), np.max(df['garage-places']), (np.min(df['garage-places']),np.max(df['garage-places'])), step = 1.)
    RoomsFilter = st.slider('🛏️Quartos', np.min(df['rooms']), np.max(df['rooms']), (np.min(df['rooms']),np.max(df['rooms'])), step = 1.)
    
    
df = df.query(f'price >= {PriceFilter[0]} & price <= {PriceFilter[1]}')
df = df.query(f'`square-foot` >= {SqtFilter[0]} & `square-foot` <= {SqtFilter[1]}')
df = df.query(f'`garage-places` >= {GarageFilter[0]} & `garage-places` <= {GarageFilter[1]}')
df = df.query(f'`rooms` >= {RoomsFilter[0]} & `rooms` <= {RoomsFilter[1]}')

 #+ f'& `square-foot` >= {SqtFilter[0]} & `square-foot` <= {SqtFilter[1]}')

mapa = folium.Map(location= [-19.916667, -43.933333], zoom_start=10, tiles="OpenStreetMap")
for lat, lng, price, cohort,address, admfees, stdfoot in zip(df['latitude'].values, df['longitude'].values, df['price'].values, df['Price Split'].values, df['address'].values, df['adm-fees'].values,df['square-foot'].values):
    stdfoot = stdfoot if stdfoot != 0 else 'Não disponível os'
    folium.CircleMarker(
    location= [lat,lng],
    radius= price/1000000,
    color = get_cohort_color(cohort),
    fill = True,
    tooltip = f'<br><h4>Analise individual de terreno</h4><br><b>O endereço da propriedade é:</b> {address}<br><b>A propriedade cobra:</b> R${admfees} de taxas administrativas<br><b>O tamanho do terreno é:</b> {stdfoot} m²<br> <b>O preço da propriedade é considerada</b> {cohort} (R${price:,.2f})</br>'
    ).add_to(mapa)

fig = px.histogram(df, 
                   x="price", 
                   marginal = 'box',
                   color = 'Price Split',
                   color_discrete_map = 
                   {
                       'Muito Alto': "#08306B",
                       'Alto' : "#2171B5",
                       'Médio': "#6BAED6",
                       'Baixo' : '#9ECAE1',
                       'Muito Baixo': '#CECECE'
                   },

                   opacity= 0.7,
                   range_x=[np.min(df.price),np.max(df.price)],
                   labels={"count": "Volume de casa nas Bins",  "price": "Preço"},
                   template='simple_white',
                   title= 'Disperssão dos valores pagos em Apartamentos')

fig.update_xaxes( # the y-axis is in dollars
    tickprefix="$", showgrid=True
)

fig.update_layout( # customize font and legend orientation & position
    font_family="Segoe UI",
    legend=dict(
        title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"
    )
)

col1, col2 = st.columns(2)



with col1:
   st.header("Mapa")
   stf.folium_static(mapa)
   
with col2:
   col3, col4, col5 = st.columns(3)
   col3.metric("Número de propriedade", np.count_nonzero(df["address"]))
   col4.metric("Média de Preço", 'R${:,.2f}'.format(np.average(df.price)))
   col5.metric("Porcentagem dos imoveis disponíveis disponíve", "{:.0%}".format(np.count_nonzero(df.price)/MaxValuePriceNonFiltered))
       
   st.header("Distribuição de Preços")
   st.plotly_chart(fig, use_container_width=True)







#st.dataframe(dataframe)