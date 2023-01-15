# ------------LIBRERIAS----------------

import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import requests

# ----------CONFIGURACIÓN DE LA PÁGINA----------

st.set_page_config(page_title ="El Titanic a través de los datos.", layout = "centered")


# ----------DATAFRAME--------------

titanic = pd.read_csv("titanic.csv")


# -----------PREPROCESAMIENTO DATAFRAME-------------

# Abro dataframe del Titanic.
titanic = pd.read_csv("titanic.csv")

titanic["Age"].fillna(titanic["Age"].mean(), inplace = True)
titanic["Embarked"].fillna("S", inplace = True)
titanic.drop(["Cabin"], axis=1, inplace=True) 
titanic.set_index("PassengerId", inplace = True)
#titanic["Fare"] = titanic["Fare"].round(2)
#titanic["Age"] = titanic["Age"].round()
#genero = {"female":0, "male":1}
#titanic["Sex"] = titanic["Sex"].map(genero).astype(int)


#---------------VARIABLES-------------

# Creación de variables para la realización de las gráficas.

    # Variables utilizadas.

cantidad = titanic.value_counts()
media = titanic["Age"].mean()
mediana = titanic["Age"].median()
hombresjeres = titanic["Sex"].value_counts()
estemuertoestamuyvivo = titanic["Survived"].value_counts()
clase = titanic["Pclass"].value_counts()
hombres_survived = titanic[titanic["Sex"] == "male"]["Survived"].value_counts()
mujeres_survived = titanic[titanic["Sex"] == "female"]["Survived"].value_counts()

hombres = titanic[titanic["Sex"] == "male"]["Sex"].count()
mujeres = titanic[titanic["Sex"] == "female"]["Sex"].count()
clase1 = titanic[titanic["Pclass"] == 1]["Pclass"].count()
clase2 = titanic[titanic["Pclass"] == 2]["Pclass"].count()
clase3 = titanic[titanic["Pclass"] == 3]["Pclass"].count()

    # Variables descartadas.

# Hombres_fal_clase = titanic[titanic["Survived"]==0][titanic["Sex"]=="male"]["Pclass"].value_counts()
# Mujeres_fal_clase = titanic[titanic["Survived"]==0][titanic["Sex"]=="female"]["Pclass"].value_counts()
# mujeres_clase = titanic[titanic["Sex"]=="female"]["Pclass"].value_counts()
# hombres_clase = titanic[titanic["Sex"]=="male"]["Pclass"].value_counts()
# proporcion_supervivientes = titanic[titanic["Survived"]==1]["Sex"].value_counts().sum()
# proporcion_fallecidos = titanic[titanic["Survived"]==0]["Sex"].value_counts().sum()
# Edad_mediaH = titanic[titanic["Sex"]=="male"]["Age"].mean()
# Edad_mediaF = titanic[titanic["Sex"]=="female"]["Age"].mean()
# muertos = titanic[titanic["Survived"] == 0]["Survived"].count()
# vivos = titanic[titanic["Survived"] == 1]["Survived"].count()
# fallecidos_hombres = titanic[titanic["Sex"] == "male"][titanic["Survived"] == 0]["Sex"].count()
# supervivientes_hombres = titanic[titanic["Sex"] == "male"][titanic["Survived"] == 1]["Sex"].count()
# fallecidos_mujeres = titanic[titanic["Sex"] == "female"][titanic["Survived"] == 0]["Sex"].count()
# supervivientes_mujeres = titanic[titanic["Sex"] == "female"][titanic["Survived"] == 1]["Sex"].count()
# sobrevive_clase1 = titanic[titanic["Survived"]==1][titanic["Pclass"] == 1]["Pclass"].count()
# muere_clase1 = titanic[titanic["Survived"]==0][titanic["Pclass"] == 1]["Pclass"].count()
# sobrevive_clase2 = titanic[titanic["Survived"]==1][titanic["Pclass"] == 2]["Pclass"].count()
# muere_clase2 = titanic[titanic["Survived"]==0][titanic["Pclass"] == 2]["Pclass"].count()
# sobrevive_clase3 = titanic[titanic["Survived"]==1][titanic["Pclass"] == 3]["Pclass"].count()
# muere_clase3 = titanic[titanic["Survived"]==0][titanic["Pclass"] == 3]["Pclass"].count()


# --------------APP----------------

st.markdown(
    """
    <style>
    .stApp {
        background: url("https://img.freepik.com/vector-gratis/fondo-acuarela_87374-69.jpg?w=2000")
    }
    button {
        background: url("https://i.pinimg.com/originals/4a/ee/d7/4aeed7337f42158be19888bc9cab419c.jpg")
    }
    .st-ck{
        background: url("https://img.freepik.com/vector-gratis/fondo-acuarela_87374-69.jpg?w=2000")
    }
    .css-6qob1r {
        background: url("https://i.pinimg.com/550x/1b/91/9c/1b919c9e386bf640be04c93460290553.jpg")
    }
   
    </style>
    """,
    unsafe_allow_html=True
)

# El siguiente código está bien, pero por alguna razón ahora no funciona si lo meto.
#
#.st-by {
#      background: url("https://i.pinimg.com/originals/4a/ee/d7/4aeed7337f42158be19888bc9cab419c.jpg"")
# }



# SIDEBAR

directorio = ["Info", "Dataframe", "Gráficos", "Conclusiones"]
seleccionar_direccion = st.sidebar.selectbox("Selecciona una dirección:", directorio)

st.sidebar.write("-----")
st.sidebar.text("Autor:")
st.sidebar.text("Ángel Pastor Sánchez")
st.sidebar.write("-----")
st.sidebar.text("Fecha:")
st.sidebar.text("11/01/2023")
if st.sidebar.button("*"):
    st.balloons()


# CUERPO CENTRAL

if seleccionar_direccion == "Info":

    st.title("TITANIC")
    st.header("A través de los datos.")
    st.image("https://images.ireland.com/thumbs/Images/Antrim/c46de5d660b643a09900e8ca3036c060/collagesecondary-desktop.jpg")
    st.write("Imagen obtenida de ireland.com")
    st.write("____")
    # el anchor es para introducir un emoticono de un ancla, puedo introducir otros emoticos, por ejemplo, dog
    st.subheader("Introducción a una historia apasionante. :anchor:")
    st.text("El Titanic fue un transatlántico británico, el mayor barco de pasajeros \ndel mundo al finalizar su construcción, que naufragó en las aguas del océano \nAtlántico durante la noche del 14 y la madrugada del 15 de abril de 1912, \nmientras realizaba su viaje inaugural desde Southampton a Nueva York, con \nescala en Cherburgo y Queenstone, tras chocar con un iceberg.")
    st.text("Entre sus pasajeros estaban algunas de las personas más ricas del mundo, \nademás de cientos de inmigrantes de nacionalidad irlandesa, británica \ny escandinava que iban en busca de una mejor vida en Norteamérica.")
    st.text("Un número muy elevado de hombres perecieron debido al estricto protocolo \nde salvamento que se siguió en el proceso de evacuación, conocido como \n«Las mujeres y los niños primero».")
    st.text("El naufragio del Titanic conmocionó e indignó al mundo entero por el elevado \nnúmero de víctimas mortales y por los errores cometidos en el accidente.")
    st.write("____")
    st.write("Información obtenida de Wikipedia")
    st.write("----")


if seleccionar_direccion == "Dataframe":

    # Establezco un título como encabezado de la página.

    st.title("Dataframe")


    # Diseño la página.
        # Introduzco texto para indicar el preprocesamiento realizado.

    st.write("____")
    st.write("PREPROCESAMIENTO REALIZADO:")
    st.write("-Sustitución valores nulos en la columna 'Age' por la media, en este caso 29.699.")
    st.write("-Sustitución valores nulos en la columna 'Embarked' por la moda, en este caso 'S'.")
    st.write("-Elimino columna 'Cabin' por exceso de valores nulos (77.1%).")
    st.write("-Establezco la columna 'PassengerId' como índice del dataframe.")
    st.write("----")

    # Inserto el dataframe.

    if st.button ("DATAFRAME", disabled=False, type = "primary", help = "Pulsa para ver el dataframe."):
        st.dataframe(titanic);
    st.write("----")


if seleccionar_direccion == "Gráficos":    
    # Doy título a la página.

    st.title("Gráficos")

    # Creo pestañas para los diferentes gráficos.

    tabs = st.tabs(["Características sociales",
                    "Estadísticas supervivencia"
                    ])


    # Creo todas las gráficas.

    tab_plot = tabs[0]
    with tab_plot:
        grafico0 = sns.displot(titanic["Age"], kde = False, bins = 30, color = "aquamarine", height=3.5)
        st.write(f"La media de edad es {media:,.3f}")
        #st.write(f"La mediana de la edad es {mediana:,.3f}") -- La comento por no considerarla necesaria a última hora.
        st.write("____")
        st.text("Cantidad de pasajeros por edad.")
        st.pyplot(grafico0)
        st.write("____")
        st.write("Comentario: En este gráfico se puede apreciar como la edad de una amplia mayoría de pasajeros corresponde a la media. Igualmente se aprecia como hay una cantidad considerable de bebés, pero llegando a edades elevadas el número de pasajeros disminuye progresivamente.")
    
    with tab_plot:
        grafico4 = px.scatter(titanic, x = "Age", y = "Fare", color = "Pclass")
        st.write("____")
        st.text("Proporción de pasajeros por edad y tarifa.")
        st.plotly_chart(grafico4)
        st.write("____")
        st.write("Comentario: todos los pasajeros que han pagado una tarifa elevada son de primera clase. Los pasajeros de clase 1 y 2 pagan tarifas bajas, que no llegan a 100 um. Como dato de interes, solo son tres personas las que pagan la tarifa máxima y quince hombres acceden gratis, desconociendose la causa.")
        st.write("____")
        #pasajeros_tarifa0 = titanic[titanic["Fare"]==0]
        #st.write(pasajeros_tarifa0)

    with tab_plot:
        st.write(f"{hombres} hombres\n\n{mujeres} mujeres")
        grafico1 = px.pie(hombresjeres, values = "Sex", names = ("hombres","mujeres"), title = "Proporción de hombres y mujeres", width=600, height=600)
        st.write("____")
        st.plotly_chart(grafico1)
        st.write("____")
        st.write("Comentario: La cantidad de hombres supone casi el doble que la cantidad de mujeres.")
    
    with tab_plot:
        grafico3 = px.histogram(titanic, x = "Pclass", y = cantidad, color = "Sex", barmode="group", title = "Proporción hombres-mujeres por clase", labels={"Pclass": "Clase de pasajero", "Survived": "Cantidad"})
        st.write("____")
        st.plotly_chart(grafico3)
        st.write("____")
        st.write("Comentario: en todas las clases sociales la cantidad de hombres es superior a la de mujeres, siendo especialmente llamativo la cantidad de hombres de 3ª clase dobla a la de mujeres de la misma.")

    with tab_plot:
        st.write(f"1ª clase: {clase1}\n\n2ª clase: {clase2}\n\n3ª clase: {clase3}")
        grafico2 = px.pie(clase, values = "Pclass", names = ("3ª clase", "1ª clase", "2ª clase"), title = "Proporción de pasajeros por clase", width=600, height=600)
        st.write("____")
        st.plotly_chart(grafico2)
        st.write("____")
        st.write("Comentario: se puede apreciar como la 3ª clase es la más numerosa de todas, con más del 50% de los pasajeros. El resto se lo reparten la 1ª clase con cerca del 25% y la 2ª con poco más del 20%")
    
    
    tab_plot = tabs[1]
    with tab_plot:
        grafico5 = px.pie(estemuertoestamuyvivo, values = "Survived", names = ("Muere", "Sobrevive"), title = "Proporción fallecidos-supervivientes", width=600, height=600)
        st.write("____")
        st.plotly_chart(grafico5)
        st.write("____")
        st.write("Comentario: fallecen más del 60% de los pasajeros, alrededor de 550. Por contra, solo sobreviven 342 de los pasajeros que embarcaron, lo que supone más de un 38%")

    with tab_plot:
        grafico6 = sns.lmplot(x="Age", y="Fare", row="Pclass", col="Survived", hue = "Sex",data=titanic, fit_reg=False)
        st.write("____")
        st.pyplot(grafico6)
        st.write("____")
        st.write("Comentario: en esta tabla se puede apreciar la relación entre supervivientes y fallecidos con la clase a la que pertenecen, filtrados por sexo y teniendo en consideración edad y tarifa. Como datos significativos hay que resaltar que solo fallecen tres mujeres de 1ª clase por seis de 2ª clase. Solo es significativo el número de mujeres fallecidas de 3ª clase. En cuanto a supervivientes destacan las mujeres en todas las clases, estando más equilibrado en 3ª clase..")

    with tab_plot:
        grafico7 = px.histogram(titanic, x= "Pclass", y= "Survived", color="Sex", barmode="group",title="Supervivientes por sexo y clase.",
                    labels={"Pclass": "Clase de pasajero", "Survived": "Supervivientes"})
        st.write("____")
        st.plotly_chart(grafico7)
        st.write("____")
        st.write("Comentario: en esta table se pueden observar supervivientes pora clase y sexo. En todas las clases sobreviven más mujeres y es especialmente llamativo los pocos hombres que sobreviven de segunda clase y en tercera en comparación con la cantidad que habia.")

    with tab_plot:
        col1, col2 = st.columns(2)
        with col1:
            grafico8 = px.pie(hombres_survived, values = "Survived", title = "Propor. hombres supervivientes", width=400, height=400, color = "Survived", color_discrete_sequence=['royalblue','skyblue'])
            st.plotly_chart(grafico8)
            st.write("____")
            st.write("Comentario: más del 80% de los hombres en el Titanic fallece, no llegando al 19% aquellos que logran subrevivir.")
        
        with col2:
            grafico81 = px.pie(mujeres_survived, values = "Survived", title = "Propor. mujeres supervivientes", width=400, height=400, color = "Survived", color_discrete_sequence=['skyblue','royalblue'], names = ("Sobrevive", "Muere"))
            st.plotly_chart(grafico81)
            st.write("____")
            st.write("Comentario: en el caso de las mujeres la estadística se revierte, sobreviviendo más del 70% y muriendo algo más del 25%.")


if seleccionar_direccion == "Conclusiones": 

    # Doy título a la página.

    st.title("Conclusiones.")

    # Escribo las conclusiones.

    st.write("----")
    st.write("-Hay muchos pasajeros jovenes en edad de trabajar.")
    st.write("-Notable diferencia entre los pasajeros de tercera clase y el resto de clases.")
    st.write("-En todas las clases hay más hombres que mujeres, especialmente en tercera.")
    st.write("-Fallecen más del 50% de los pasajeros.")
    st.write("-En todas las clases sobreviven más mujeres que hombres y fallecen más hombres que mujeres.")
    st.write("-La proporción de fallecidos hombres supera el 80%, mientras que en mujeres apenas sobrepasa el 25%.")
    st.write("----")
    st.image("https://i0.wp.com/imgs.hipertextual.com/wp-content/uploads/2019/08/hipertextual-2019736066.jpg?fit=1728%2C1080&quality=50&strip=all&ssl=1")

   