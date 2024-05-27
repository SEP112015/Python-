
class  MyEntyPerson:
    pass

print(MyEntyPerson)
print(MyEntyPerson())



"""class  Person:
   def __init__(self):
        self.name ="Sebastian" 
        self.surname = "Escaño"
        

my_person = Person()
print(f"{my_person.name}  {my_person.surname}")"""




class Person:
    def __init__(self, name, surname, alias ="Sin alias"):
        self.full_name = f"Mi nombre es {name} {surname} y mi nickname es los videojuegos es {alias}"

    def walk(self):
        print(f"{self.full_name} y ahora estoy caminando")

my_person = Person("Sebastian", "Escaño")
print(f"{my_person.full_name}")
my_person.walk()


my_other_person = Person("Sebastian", "Escaño", "Koro-sensei")
print(f"{my_other_person.full_name}")
my_other_person.walk()





