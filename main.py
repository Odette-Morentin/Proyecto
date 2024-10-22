#Importar librerías y documentos necesarios
import streamlit as st
import inicio as inicio
import visualizar_clases as visualizar_clases

#Menu de opciones y lógica de cada una
def main():
    menu_principal = ["Inicio", "Registro de Clase", "Registro de Maestro", "Visualizar Clases", "Reportes y Estadísticas"]
    selected = st.sidebar.selectbox("Opciones", menu_principal)
    match selected:

        #Mensaje de bienvenida y cómo navegar
        case "Inicio":
            inicio.guiaUsuario()

        #Se visualizan todos los horarios, materias y profesores de TODA la base de datos
        case "Visualizar Clases":
            visualizar_clases.mostrar_visualizar_clases()

if __name__ == "__main__":
    main()