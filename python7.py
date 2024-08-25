"""
#
# Part: Python Class and Object
#
"""
class MyClass:
    x = 5

object1 = MyClass()
print("object1 = ", object1.x)
object2 = MyClass()
print("object2 = ", object2.x)

class Assasin:
    def __init__(self, name_f, age_f):
        self.name = name_f
        self.age = age_f

    def __str__(self):
        return f"{self.name} - {self.age}"
    
    def sayHi(self, last_name = "Nunez"):
        print (f"Hey Bro {self.name} {last_name}")

p1 = Assasin("Darwin", 8)
print(p1.name, p1.age)
print(p1)
p1.sayHi()

p2 = Assasin("Nunat", 9)
print(p2.name, p2.age)
print(p2)
p2.sayHi("Ranger")

class Car:
    def __init__(self, body_color, engine_size):
        self.wheels = 4
        self.windown = 4
        self.windown_front = 1
        self.windown_back = 1
        self.body_color = body_color
        self.enginr_size = engine_size

    def push_windown_button(self):
        pass

    def pep_windown_button(self):
        pass

    def calspeed(self):
        return self.enginr_size * 1000
    
    def turnOnFrontLight(self, status = "off"):
        if status == "on":
            pass
        else:
            pass