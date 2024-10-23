#Importar librerias necesarias
import streamlit as st

# Función que saluda al usuario y explica cómo navegar por el sitio
def guiaUsuario() -> str:

    # Formato de título
    html_code = """<h1 style="text-align: center;">Bienvenido</h1>"""
    st.markdown(html_code, unsafe_allow_html=True)
    
    # HTML con estilo CSS para dar formato al texto
    html_code = """
    <div style='text-align: center; font-size: 14px;'>
        <p>Para navegar en este sitio web cuentas con un menú desplegable en el lado izquierdo de la pantalla donde podrás elegir la opción que sea de tu interés:</p>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

