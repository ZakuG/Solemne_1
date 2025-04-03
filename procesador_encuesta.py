import tkinter as tk
from tkinter import simpledialog, messagebox

def leer_archivo_csv(nombre_archivo):
    datos = {'Sexo': [], 'Edad': [], 'Respuesta': []}

    try:
        with open(f'{nombre_archivo}.csv', 'r') as archivo:
            archivo.readline()
            for linea in archivo:
                valores = linea.strip().split(' ')
                datos['Sexo'].append(valores[0])
                datos['Edad'].append(valores[1])
                if len(valores) == 3:
                    datos['Respuesta'].append(valores[2])
                else:
                    datos['Respuesta'].append(f'{valores[2]} {valores[3]}')
    except FileNotFoundError:
        messagebox.showerror("Error", f'No se encontró el archivo: {nombre_archivo}')
    except Exception as e:
        messagebox.showerror("Error", f'Error al leer el archivo: {e}')
    
    return datos

def promedio_edad(edad):
    return sum(edad)/len(edad)

def mediana_edad(edad):
    edad.sort()
    largo_edad = int(len(edad))
    indice_1, indice_2 = (largo_edad//2)-1, (largo_edad//2)
    if largo_edad % 2 == 0:
        return (edad[int(indice_1)] + edad[int(indice_2)])/2
    else:
        return edad[int(indice_1)]
    
def contar_frecuencia(respuesta):
    frecuencia = {}
    for elemento in respuesta:
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
    return frecuencia

def moda_edad(edad):
    frecuencia = contar_frecuencia(edad)
    max_frecuencia = max(frecuencia.values())
    return [key for key, value in frecuencia.items() if value == max_frecuencia]

def procesador_encuesta(datos_encuesta):
    edad = [int(elemento) for elemento in datos_encuesta["Edad"]]
    promedio = promedio_edad(edad)
    mediana = mediana_edad(edad)
    moda = moda_edad(edad)
    frecuencias = contar_frecuencia(datos_encuesta["Respuesta"])
    
    resultado = f"Promedio = {promedio}\nMediana = {mediana}\nModa = {moda}\n\nFrecuencias de Respuestas:\n"
    for key, value in frecuencias.items():
        resultado += f"{key}: {value}\n"
    
    messagebox.showinfo("Resultados de la Encuesta", resultado)

def menu_interactivo():
    root = tk.Tk()
    root.withdraw()
    while True:
        opcion = simpledialog.askstring("Menú", "Seleccione una opción:\n\n1) Leer archivo de datos\n2) Mostrar estadísticas generales\n3) Filtrar datos por sexo\n4) Filtrar datos por rango de edad\n5) Guardar resultados en un archivo\n6) Salir").upper()
        
        if opcion == "1":
            global datos_encuesta
            archivo = simpledialog.askstring("Entrada", "¿Cuál es el nombre del archivo?")
            if archivo:
                datos_encuesta = leer_archivo_csv(archivo)
                messagebox.showinfo("Éxito", "Archivo leído correctamente")
        elif opcion == "2":
            if datos_encuesta:
                procesador_encuesta(datos_encuesta)
            else:
                messagebox.showerror("Error", "No hay datos cargados")
        elif opcion == "3":
            sexo = simpledialog.askstring("Filtro", "Ingrese el sexo a filtrar (Femenino/Masculino):")
            datos_filtrados = {key: [datos_encuesta[key][i] for i in range(len(datos_encuesta["Sexo"])) if datos_encuesta["Sexo"][i] == sexo] for key in datos_encuesta}
            procesador_encuesta(datos_filtrados)
        elif opcion == "4":
            edad_min = int(simpledialog.askstring("Filtro", "Ingrese la edad mínima:"))
            edad_max = int(simpledialog.askstring("Filtro", "Ingrese la edad máxima:"))
            datos_filtrados = {key: [datos_encuesta[key][i] for i in range(len(datos_encuesta["Edad"])) if edad_min <= int(datos_encuesta["Edad"][i]) <= edad_max] for key in datos_encuesta}
            procesador_encuesta(datos_filtrados)
        elif opcion == "5":
            with open("resultados.txt", "w") as archivo:
                archivo.write("Resultados de la Encuesta\n\n")
                archivo.write(f"Promedio de edad: {promedio_edad([int(e) for e in datos_encuesta['Edad']])}\n")
                archivo.write(f"Mediana de edad: {mediana_edad([int(e) for e in datos_encuesta['Edad']])}\n")
                archivo.write(f"Moda de edad: {moda_edad([int(e) for e in datos_encuesta['Edad']])}\n")
                archivo.write("\nFrecuencia de respuestas:\n")
                for key, value in contar_frecuencia(datos_encuesta["Respuesta"]).items():
                    archivo.write(f"{key}: {value}\n")
            messagebox.showinfo("Éxito", "Resultados guardados en 'resultados.txt'")
        elif opcion == "6":
            break
        else:
            messagebox.showerror("Error", "Opción no válida")

menu_interactivo()
