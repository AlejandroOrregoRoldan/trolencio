import pandas as pd
import numpy as np
import streamlit as st


print("hola mundo")
#Nombre en la pestaña
st.set_page_config(layout='centered',
                   page_title='talento teach',
                   page_icon=':smile:')

#Titulo de la pagina
t1, t2 = st.columns([0.3,0.7])
t1.image('capibara.jfif', width=200)
t2.title('La vida en Peru')
t2.markdown("tel:123| email: piu@gmail.com")

#secciones
steps = st.tabs(['Pestaña 1','Pestaña 2','Pestaña $\sqrt{9}$'])
with steps[0]:
    camp_df=pd.read_csv('Campanhas.csv', encoding='latin-1', sep=';')
    camp=st.selectbox('escoge un ID de campaña', 
                      camp_df['ID_Campana'], 
                      help='mUEStra las exsistente')
    met_df= pd.read_csv('Metricas.csv', encoding='latin-1', sep=';')

    m1,m2,m3 = st.columns([1,1,1])

    id1=met_df[(met_df['ID_Campana']==camp)]
    id2=met_df[(met_df['ID_Campana']==camp)]
    m1.write('Metricas filtradas')
    m1.metric(label='metrica 1', value=sum(id1['Conversiones']), 
            delta=str(sum(id1['Rebotes']))+'total de Rebotes', 
            delta_color='inverse')
    m2.metric(label='metrica 2', value=np.mean(id1['Clics']), 
            delta=str(np.mean(id1['Impresiones']))+'Promedios de Impresiones', 
            delta_color='inverse')
    

    st.write('Hola mundo')
    st.image('mono.jpg', width=1000)
    data={'nombre':['Kuzco','Kronk'], 'Fecha de nacimiento': [0,0]}
    df=pd.DataFrame(data)
    st.table(df)
    st.dataframe(df)

with steps[1]:
    df=pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
    df.Fecha=pd.to_datetime(df.Fecha, format="%d/%m/%Y")
    df.set_index('Fecha', inplace=True)
    #st.table(df)
    varx=st.selectbox('Elige la variable x', df.columns)
    #vary=st.selectbox('Elige la variable y', met_df['Clic'])
    fig, ax = plt.subplots()
    ax = sns.histplot(data=df, x=varx)
    st.pyplot(fig)

    if st.button('boton clave', type='primary'): 
        st.write('bombardeaste Peru')

with steps[2]:
    st.selectbox('Escoja una opcion', ['bombardea rusia', 'bombardea China', 'bombardea Corea', 'bombardea Iran', 'bombardea Bolivia'])
        
