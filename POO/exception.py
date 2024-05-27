### Exceptions Handling ###

numberOne, numberTwo = 5, "1"


try: #Don't is optional
     print(numberOne + numberTwo)  
except: #Too
    print("Se ha producido un error")
finally:
    print("Terminado")


try: #Don't is optional
    print(numberOne + numberTwo)  
except ValueError: #Too
    print("Se ha producido un error")
except TypeError: #Too
    print("Se ha producido un error")
finally:
    print("Terminado")


#Captura de la información de excepción

try: #Don't is optional
     print(numberOne + numberTwo)  
except: #Too
    print("Se ha producido un error")
finally:
    print("Terminado")


try:
    print(numberOne + numberTwo)  
except ValueError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    print("Terminado")
