import streamlit as st
from notion_client import Client
import os
from dotenv import load_dotenv
from datetime import datetime
import utils

p = 0
pn = 0

lista1=["murcia","alicante","jumilla","yecla","novelda""alcoi","alcoy","cartagena","las torres de cotillas","lorca","elche"]
lista2=["valencia","castellon","castellón","jaén","jaen","almeria","almería","granada","albacete"]
lista3=["madrid","toledo","cuenca","ciudad real","teruel","cordoba","córdoba","málaga","malaga","teruel"]
lista4=["barcelona","zaragoza","sevilla","cadiz","cádiz","tarragona","lerida","lérida"]

st.set_page_config(
    page_title="IsabellaEstilista",
    page_icon="💄",
    
    
)

utils.local_css("estilos.css")

# Cargar variables de entorno
load_dotenv()

# Configurar cliente de Notion
notion = Client(auth=os.getenv(""))

# Formulario Streamlit

a = st.container()

with a:

    st.title(":blue[Formulario de Citas IsabellaEstilista]")

    nombre = st.text_input("Nombre")
    fecha_evento = st.text_input("Fecha del evento", placeholder="dd/mm/aa")

    lugar = st.text_input("Lugar")
    lugar = lugar.lower()
    if lugar in lista1 :
        personas = st.number_input("Número de invitadas SIN novia",min_value=4)
    elif lugar in lista2:
        personas = st.number_input("Número de invitadas SIN novia",min_value=7)
    elif lugar in lista3:
        personas = st.number_input("Número de invitadas SIN novia",min_value=8)
    elif lugar in lista4:
        personas = st.number_input("Número de invitadas SIN novia",min_value=10)
    else:
        personas = st.number_input("Número de invitadas SIN novia",min_value=4)
        
    novia =  st.radio("Novia",["Si","No"])
    telefono = st.text_input("Telefono")
    email = st.text_input("Email")
    enviar = st.button("Guardar Cita")



@st.dialog("Presupuestos💵")

def novia1(p):
    p=110*personas
    st.write("Presupuesto Novia: ", 200,"€")
    st.write("Presupuesto Invitadas: ",110,"€ x persona")
    

@st.dialog("Presupuestos💵")

def novia2(p):
    p=120*personas
    st.write("Presupuesto Novia: ", 250,"€")
    st.write("Presupuesto Invitadas: ",120,"€ x persona ")
    

@st.dialog("Presupuestos💵")

def novia3(p):
    p=150*personas
    st.write("Presupuesto Novia: ", 350,"€")
    st.write("Presupuesto Invitadas: ",150,"€ x persona")
    
@st.dialog("Presupuestos💵")

def invitada1(p):
    p=110*personas
    st.write("Presupuesto Invitadas: ",110,"€ x persona")
    
@st.dialog("Presupuestos💵")

def invitada2(p):
    p=120*personas
    st.write("Presupuesto Invitadas: ",120,"€ x persona")
    
@st.dialog("Presupuestos💵")

def invitada3(p):
    p=150*personas
    st.write("Presupuesto Invitadas: ",150,"€ x persona")
    

if enviar:
    
    if lugar in lista1 and novia == "Si":
        novia1(p)
        p=110*personas
        pn=200
    elif lugar in lista2 and novia == "Si":
        novia2(p)
        p=120*personas
        pn=250
    
    elif lugar in lista3 and novia == "Si":
        novia3(p)
        p=150*personas
        pn=350

    elif lugar in lista4 and novia == "Si":
        novia3(p)
        p=150*personas
        pn=350
    elif lugar in lista1 and novia == "No":
        invitada1(p)
        p=110*personas
    elif lugar in lista2 and novia == "No":
        invitada2(p)
        p=120*personas
    elif lugar in lista3 and novia == "No":
        invitada3(p)
        p=150*personas
    elif lugar in lista4 and novia == "No":
        invitada3(p)
        p=150*personas
    
    # Notion
    
    notion_api_key = st.secrets["notion_api_key"]
    document_ID = "1ddfc20415a680188fdcf6a1859386ea"

    # Inicializar el cliente
    notion = Client(auth=notion_api_key)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Enviar datos a Notion
    try:
    # Estructurar datos para Notion (JSON)
        notion.pages.create(
        parent={"database_id": document_ID},
        properties={
                "Name": {"title": [{"text": {"content": nombre}}]},
                "Fecha": {"rich_text": [{"text": {"content": fecha_evento}}]},
                "lugar": {"rich_text": [{"text": {"content": lugar}}]},
                "Invitadas": {"number": personas},
                "Novia":{"rich_text": [{"text": {"content": novia}}]},
                "Teléfono": {"phone_number": telefono},
                "Contact Email": {"email": email},
                "presupuesto Novia": {"number": pn},
                "presupuesto invitada": {"number": p}
            })

        st.success("Guardado correctamente, Gracias!")
    except Exception as e:
        st.error(f"Error: {e}")

    
