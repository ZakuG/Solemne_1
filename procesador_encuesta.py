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
        messagebox.showinfo("Éxito", "Archivo leído correctamente")
        return datos
    except FileNotFoundError:
        messagebox.showerror("Error", f'No se encontró el archivo: {nombre_archivo}')
    except Exception as e:
        messagebox.showerror("Error", f'Error al leer el archivo: {e}')
        

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
    respuesta.append(resultado)
    messagebox.showinfo("Resultados de la Encuesta", resultado)

def menu_interactivo():
    root = tk.Tk()
    root.withdraw()
    global respuesta
    global nombre
    global datos_encuesta
    respuesta = []
    var = []
    nombres = []
    nombre = ""
    datos_encuesta = []
    while True:
        opcion = simpledialog.askstring("Menú", f"{f"Archivo: {nombre}\n" if nombre != "" else ""}Seleccione una opción:\n\n1) Leer archivo de datos\n2) Mostrar estadísticas generales\n3) Filtrar datos por sexo\n4) Filtrar datos por rango de edad\n5) Guardar resultados en un archivo\n6) Salir").upper()
        if opcion == "1":
            nombre = ""
            archivo = simpledialog.askstring("Entrada", "¿Cuál es el nombre del archivo?")
            datos_encuesta = leer_archivo_csv(archivo)
            nombre = archivo if datos_encuesta else ""
        elif opcion == "2":
            if datos_encuesta and archivo and nombre != "":
                procesador_encuesta(datos_encuesta)
                var.append("Estadisticas generales")
                nombres.append(nombre)
            else:
                messagebox.showerror("Error", "No hay datos cargados")
        elif opcion == "3":
            if nombre == "":
                messagebox.showerror("Error", "No hay datos cargados")
            else:
                sexo = simpledialog.askstring("Filtro", "Ingrese el sexo a filtrar (Femenino/Masculino):")
                if sexo == "Femenino" or sexo == "Masculino":
                    datos_filtrados = {key: [datos_encuesta[key][i] for i in range(len(datos_encuesta["Sexo"])) if datos_encuesta["Sexo"][i] == sexo] for key in datos_encuesta}
                    procesador_encuesta(datos_filtrados)
                    var.append(f"Datos filtrados por {sexo}")
                    nombres.append(nombre)
                else:
                    messagebox.showerror("Error", """Ingrese 'Maculino' o 'Femenino' porfavor""")
        elif opcion == "4":
            try:
                a = True
                if nombre == "":
                    messagebox.showerror("Error", "No hay datos cargados")
                else:
                    while a:
                        edad_min = int(simpledialog.askstring("Filtro", "Ingrese la edad mínima:"))
                        max_real = int(max(datos_encuesta["Edad"]))
                        min_real = int(min(datos_encuesta["Edad"]))
                        if edad_min < min_real:
                            messagebox.showerror("Error", f"Error, la edad minima en la encuesta es {min_real}, porfavor intente nuevamente.")
                        edad_max = int(simpledialog.askstring("Filtro", "Ingrese la edad máxima:"))
                        if edad_max > max_real:
                            messagebox.showerror("Error", f"Error, la edad maxima en la encuesta es {max_real}, porfavor intente nuevamente.")
                        else:
                            a = False
                    datos_filtrados = {key: [datos_encuesta[key][i] for i in range(len(datos_encuesta["Edad"])) if edad_min <= int(datos_encuesta["Edad"][i]) <= edad_max] for key in datos_encuesta}
                    procesador_encuesta(datos_filtrados)
                    var.append(f"Datos filtrados por rango de edad [{edad_min} - {edad_max}]")
                    nombres.append(nombre)
            except Exception as e:
                messagebox.showerror("Error", f"Error, porfavor intente nuevamente: {e}")
        elif opcion == "5":
            with open("resultados.txt", "w") as archivo:
                i = 0
                for elemento in respuesta:
                    archivo.write(f"Resultados de la Encuesta: {nombres[i]}\n\n")
                    archivo.write(f"Opcion: {var[i]}\n")
                    archivo.write(f"{elemento}\n")
                    i += 1
                archivo.close
            messagebox.showinfo("Éxito", "Resultados guardados en 'resultados.txt'")
        elif opcion == "6":
            break
        else:
            messagebox.showerror("Error", "Opción no válida")

menu_interactivo()
