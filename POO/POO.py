class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar (self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años de edad.")

    
persona1 = Persona("Juan", 23)
persona1.saludar()
        
persona1 = Persona("Marta", 89)
persona1.saludar()