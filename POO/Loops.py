
my_condition = 0

#while my_condition < 10:
#    print(my_condition)
#    my_condition += 1
#if (my_condition  == 10):
#    print("Ya haz alcanzado el número máximo")
#else:
#    print("El numero no ha alcanzado el límite")



"""while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Hemos llegado a 15")
        break
    print(my_condition)"""


"""my_list = [24, 30, 40, 50, 34, 27, 50]


for element in my_list:
    print(element)"""



"""my_set = {"Sebastian", "Escaño", 19, 1988}

for element in my_set:
    print(element)"""


"""my_dict = {
    "Nombre": "Sebastian", 
    "Apellido": "Escaño", 
    "Edad": 19,
    "Lenguajes" : {"Python", "C#", "R", "MongoDB"},
    1: 1.70
           }


for element in my_dict.values():
    print(element)
"""
my_dict = {
    "Nombre": "Sebastian", 
    "Apellido": "Escaño", 
    "Edad": 19,
    "Lenguajes" : {"Python", "C#", "R", "MongoDB"},
    1: 1.70
           }


for element in my_dict:
    print(element)
    if element == "Edad":
        print(f"Hemos encontrado la {element}")
        break
    