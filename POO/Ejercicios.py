# class Calculadora:
#     def __init__(self, numero1, numero2):
#         self.numero1 = numero1 
#         self.numero2 = numero2  

#     def resultado (self):
#         print(f"La suma de {self.numero1} + {self.numero2} es igual a  {self.numero1 + self.numero2}")
#         print(f"La resta de {self.numero1} - {self.numero2} es igual a  {self.numero1 - self.numero2}")
#         print(f"La multiplicación de {self.numero1} * {self.numero2} es igual a  {self.numero1 * self.numero2}")
#         if self.numero2 != 0:
#             print(f"La división de {self.numero1} / {self.numero2} es igual a  {self.numero1 / self.numero2}")
#         else:
#             print("Error, no se puede dividir entre 0")

        
# persona1 = Calculadora()
# print("Calculadora 1:")
# persona1.resultado()

# print("------------------------------------------------------")
# print("Calculadora 2:")
# class Calculadora2:
#     def __init__(self, numero):
#         self.resultado = numero

#     def sumar(self, numero):
#         self.resultado += numero
    
#     def multiplicar(self, numero):
#         self.resultado *= numero

#     def restar(self, numero):
#         self.resultado -= numero

#     def divir(self, numero):
#         if numero != 0:
#             self.resultado /= numero
#         else:
#             print("Error, no se puede dividir entre 0")
    
# calculo = Calculadora2(0)

# calculo.sumar(5)
# calculo.multiplicar(4)
# calculo.restar(5)
# calculo.divir(2)
# resultado = calculo.resultado
# print(f"Resultado:{resultado}")



# print("Calculadora 3:")
# class Calculadora2:
#     def suma(self, numero1, numero2):
#         return numero1 + numero2

#     def restar(self, numero1, numero2):
#         return numero1 - numero2
    
#     def multiplicar(self, numero1, numero2):
#         return numero1 * numero2

#     def divir(self, numero1, numero2):
#         if numero2 != 0:
#             return numero1 / numero2
#         else:
#             print("Error, no se puede dividir entre 0")
    
# numero1 = float(input("Ingresa el primer numero: "))
# numero2 = float(input("Ingresa el segundo numero: "))

# calculadora = Calculadora2()

# suma = calculadora.suma(numero1, numero2)
# resta = calculadora.restar(numero1, numero2)
# multiplicacion = calculadora.multiplicar(numero1, numero2)
# division = calculadora.divir(numero1, numero2)

# print(f"La suma de {numero1} + {numero2} es igual a {suma}")
# print(f"La resta de {numero1} - {numero2} es igual a  {resta}")
# print(f"La multiplicación de {numero1} * {numero2} es igual a  {multiplicacion}")
# print(f"La división de {numero1} / {numero2} es igual a  {division}")


# print(------------------------------------------------------)
# Ejercicio:

# class ContadorPalabras:
#     def __init__(self):
#         self.contador = 0

#     def contar(self, cadena):

#         palabras = cadena.split()
#         self.contador += len(palabras)

#     def obtener_contador(self):
#         return self.contador


# contador = ContadorPalabras()

# texto_contador = input("Ingrese la cadena de texto aquí: ")
# contador.contar(texto_contador)

# print(f"El texto escrito contiene un total de: {contador.obtener_contador()} palabras")
