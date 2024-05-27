###EJERCICIO POLIMORFIMO Y HERENCIAS POR DEFAULT###
class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El auto {self.marca} {self.modelo} esta arrancando"
    
class coche(vehiculo):
    def acelerar(self):
        return f"El auto {self.marca} {self.modelo} esta acelerando" 
    
class motocicleta(vehiculo):
    def calibrando(self):
        return f"La mootocicleta {self.marca} {self.modelo} esta está calibrando"
    
cochee = coche("Toyota", "Camry")
motocicletaa = motocicleta("Harley-Davidson", "Sportster")

print("Carro")
print(f"Marca y modelo: {cochee.marca}, {cochee.modelo}")
print("Motocicleta")
print(f"Marca y modelo: {motocicletaa.marca}, {motocicletaa.modelo}")
print("------------------------------------------------------------------------")

print(cochee.acelerar())
print(motocicletaa.calibrando())
print("------------------------------------------------------------------------")
print(cochee.arrancar())
print(motocicletaa.arrancar())






###EJERCICIO POLIMORFISMO Y HERENCIA POR CONSOLA###

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El auto {self.marca} {self.modelo} está arrancando"

class Coche(Vehiculo):
    def acelerar(self):
        return f"El auto {self.marca} {self.modelo} está acelerando"

class Motocicleta(Vehiculo):
    def calibrando(self):
        return f"La motocicleta {self.marca} {self.modelo} está calibrando"
    

elige = input("carro o motocicleta? ")

if elige.lower() == "carro":
    marca_usuario = input("Ingresa la marca del vehículo: ")
    modelo_usuario = input("Ingresa el modelo del vehículo: ")
    coche_usuario = Coche(marca_usuario, modelo_usuario)
    motocicleta_usuario = Motocicleta(marca_usuario, modelo_usuario)
    print("------------------------------------------------------------------------")
    print("Carro")
    print(f"Marca y modelo: {coche_usuario.marca}, {coche_usuario.modelo}")
    print("------------------------------------------------------------------------")
    print(coche_usuario.arrancar())
    print(coche_usuario.acelerar())    
elif elige.lower() == "motocicleta":
    marca_usuario = input("Ingresa la marca de la motocicleta: ")
    modelo_usuario = input("Ingresa el modelo de la motocicleta: ")
    coche_usuario = Coche(marca_usuario, modelo_usuario)
    motocicleta_usuario = Motocicleta(marca_usuario, modelo_usuario)
    print("Motocicleta")
    print(f"Marca y modelo: {motocicleta_usuario.marca}, {motocicleta_usuario.modelo}")
    print("------------------------------------------------------------------------")
    print(coche_usuario.arrancar())
    print(motocicleta_usuario.arrancar())
else:
    print("Elige una opción disponible")




###EJERCICIO SUPER CLASE ANIMAL###

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("El método hablar() debe ser implementado en las subclases.")


class Perro(Animal):
    def hablar(self):
        return "Guau"  

class Gato(Animal):
    def hablar(self):
        return "Miau"  


mi_perro = Perro("Doberman")
mi_gato = Gato("Gato de Egipto")


print(f"{mi_perro.nombre} dice: {mi_perro.hablar()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hablar()}")












