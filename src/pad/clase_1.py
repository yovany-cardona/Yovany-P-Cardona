# class -  relacion directa con un objeto (entidad o objeto)
# def   - aciones o funciones del objeto

class Personas():
    def __init__(self):
        # atributos del objeto
        self.nombre = "Andres" # variable de tipo texto "" ''
        self.edad =   0 # variablke de tipo numerico
        self.estatura = 100.0 # variable de tipo decimal
        self.peso    = 35.6 # variable de tipo decimal


persona =Personas()
persona.edad =   42
persona.estatura = 193
print("nombre: ",persona.nombre," edad: ",persona.edad, " cms: ", persona.estatura)
print("nombre: ",persona.nombre," edad: ",persona.edad, " cms: ", persona.estatura)