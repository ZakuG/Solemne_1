import random

class CreateRespuesta:
    def __init__(self, Sexo, Edad, Respuesta):
        self.Sexo = Sexo
        self.Edad = Edad
        self.Respuesta = Respuesta
    
    def funcion(self):
        return f"{self.Sexo} {self.Edad} {self.Respuesta}\n"
    
def createCSV():
    with open("encuesta_habitos.csv", "w") as archivo:
        archivo.write("Sexo Edad Respuesta\n")
        for _ in range(300):
            persona = CreateRespuesta("Femenino" if random.random()<=0.5 else "Masculino", random.randint(18,45), "Si" if random.randint(1,3)==1 else "No" if random.randint(2,3)==2 else "Tal vez")
            archivo.write(persona.funcion())

        archivo.close()

createCSV()