import tkinter as tk
from tkinter import simpledialog

def leer_archivo_csv(nombre_archivo):
    datos = {'Sexo': [], 'Edad': [], 'Respuesta': []}

    try:
        with open(f'{nombre_archivo}.csv', 'r') as archivo:
            encabezados = archivo.readline().strip().split(' ')
            for linea in archivo:
                valores = linea.strip().split(' ')
                datos['Sexo'].append(valores[0])
                datos['Edad'].append(valores[1])
                if len(valores) == 3:
                    datos['Respuesta'].append(valores[2])

                else:
                    datos['Respuesta'].append(f'{valores[2]} {valores[3]}')

    except FileNotFoundError:
        print(f'Error: no se encontro el archivo:\n{nombre_archivo}')
    
    except Exception as e:
        print(f'Error al leer el archivo: {e}')
    
    return datos
def promedio_edad(edad):
    return sum(edad)/len(edad)

def mediana_edad(edad):
    edad.sort()
    largo_edad = int(len(edad))
    indice_1, indice_2 = (largo_edad/2)-1, (largo_edad/2)
    if largo_edad % 2 == 0:
        mediana_edad = (edad[int(indice_1)] + edad[int(indice_2)])/2

    else:
        mediana_edad = (edad[int(indice_1)])

    return mediana_edad

def moda_edad(edad):
    frecuencia = contar_frecuencia(edad)
    max_frecuencia = max(frecuencia.values())
    moda = [key for key, value in frecuencia.items() if value == max_frecuencia]
    return moda

def contar_frecuencia(respuesta):
    frecuencia = {}
    for elemento in respuesta:
        if elemento in frecuencia:
            frecuencia[elemento] += 1

        else:
            frecuencia[elemento] = 1
    return frecuencia
    
def procesador_encuesta(datos_encuesta):
    edad = [int(elemento) for elemento in datos_encuesta["Edad"]]
    print(f'Promedio = {promedio_edad(edad)}, Mediana = {mediana_edad(edad)}, Moda = {moda_edad(edad)}')
    print(f'Frecuencias Respuestas:\n{contar_frecuencia(datos_encuesta["Respuesta"])}')

    return 
    
def main():
    archivo = simpledialog.askstring("Entrada", "¿Cual es el nombre del archivo?")
    datos_encuesta = leer_archivo_csv(archivo)
    if len(datos_encuesta) > 0:    
        procesador_encuesta(datos_encuesta)
        

main()