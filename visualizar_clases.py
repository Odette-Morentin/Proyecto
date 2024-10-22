#Importar librerias necesarias
import streamlit as st
import pandas as pd
import sqlite3

#Leer excel
ruta_excel = 'horario_db.xlsx'  
df = pd.read_excel(ruta_excel)

#Conectar a la base de datos
conexion = sqlite3.connect('clases.db')  
nombre_tabla = 'clases'  
df.to_sql(nombre_tabla, conexion, if_exists='replace', index=False)
conexion.close()

#Función para visualizar la base de datos completa
def mostrar_visualizar_clases():
    #Titulo
    st.title("Ver Clases")

    #Conexion a base de datos
    conn = sqlite3.connect('clases.db')
    cursor = conn.cursor()

    #Seleccionar lo que se va a mostrar
    cursor.execute("SELECT * FROM clases")
    clases = cursor.fetchall()

    #Mostrar solo si la base de datos no está vacía
    if clases: 
        df_clases = pd.DataFrame(clases, columns=["Carrera", "Materia", "ID", "Profesor","Semestre y Grupo", "Dia", "Horario", "Asistencia"])
        st.write(df_clases)
    else:
        st.write("No hay clases registradas en la base de datos.")

    conn.close()