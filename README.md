# 📊 Proyecto de Encuesta de Hábitos

Este proyecto implementa un sistema completo para **gestionar encuestas sobre hábitos**. Incluye generación automática de respuestas, almacenamiento en CSV, análisis estadístico y una interfaz gráfica amigable para interactuar con los datos.

---

## 🧠 ¿Qué hace este proyecto?

### 1. **Generación de Datos**
Se generan 300 respuestas aleatorias que incluyen:
- **Sexo:** Masculino o Femenino.
- **Edad:** Entre 18 y 45 años.
- **Respuesta:** "Sí", "No" o "Tal vez".

Se guardan en un archivo `encuesta_habitos.csv`.

### 2. **Procesamiento de Datos**
Desde el archivo CSV, se pueden analizar los datos cargados:
- **Promedio**, **mediana** y **moda** de las edades.
- **Frecuencia** de las respuestas.

### 3. **Interfaz Gráfica**
Utilizando `Tkinter`, el usuario puede:
- Leer el archivo CSV.
- Ver estadísticas generales.
- Filtrar por sexo.
- Filtrar por rango de edad.
- Guardar resultados en un archivo de texto.
- Salir del programa.

---

## 🧩 Estructura del Proyecto

| Archivo         | Descripción                                                  |
|----------------|--------------------------------------------------------------|
| `main.py`       | Código principal que integra todas las funcionalidades.     |
| `encuesta_habitos.csv` | Archivo generado con datos simulados de la encuesta.  |
| `resultados.txt` | Archivo donde se guardan los resultados estadísticos.      |

> 💡 Puedes modularizar el código en archivos como `generador.py`, `lector.py`, `estadisticas.py`, etc., para mantenerlo más limpio.

---

## 📌 Ejemplo de salida
Promedio = 31.5 Mediana = 30 Moda = [28, 33]

Frecuencias de Respuestas: Sí: 100 No: 120 Tal vez: 80

---

## 🛠 Requisitos

- Python 3.6 o superior
- Tkinter (usualmente viene instalado con Python)

---

✨ Funcionalidades destacadas
✅ Generación automática de encuestas
✅ Interfaz gráfica con menús interactivos
✅ Cálculo de promedio, mediana y moda
✅ Análisis por filtros de sexo y edad
✅ Resultados exportables a un archivo .txt

📚 Conclusión
Este proyecto es ideal para practicar:

Manejo de archivos CSV

Estadística básica en Python

Interacción con el usuario mediante interfaces gráficas

Organización y análisis de datos

Una herramienta educativa simple pero poderosa para análisis de encuestas.

👤 Hecho con 💻 y ☕ por ZakuG,StormDead,mariscalrommel


