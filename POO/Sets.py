my_set = set()

my_other_set = {}

print(type(my_set))

print(type(my_other_set)) #Inicialmente es un Dict

my_other_set = {"Sebastian", "Escaño", 19, 1988}

print(my_other_set)

print(type(my_other_set))


my_other_set.add("Creo que funciona")
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("Creo que funciona")
print(my_other_set) #Un set no admite repeticiones

print("Sebastian" in my_other_set)
print("Sebastián" in my_other_set)

my_other_set.remove("Creo que funciona")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))


my_set = {"Sebastian", "Escaño", 19, 1988}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set ={"Ferragamos", "Salvatore", "Vitally", "Menphis"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_list = list(my_new_set)

print(my_list)

my_new_set = my_new_set.union({"C#", "JavaScript"})
print(my_new_set)

print(my_new_set.difference(my_set))
