"""
#
# Part: Python Funtion
# 
"""
def myFunction():
    i = 1
    while i <= 3:
        print("Hey Bro! ", i)
        i+=1

myFunction()

def myName(name):
    print("My name is " + name)
myName("Darwin")
myName("Niwrad")

def myFullname(first_name = "Unknow", lastname_name = "Nunez"):
    print("My name is " + first_name + " " + lastname_name)
myFullname("Darwin")
myFullname("Niwrad", "Nunez")
myFullname("Darwin", "Nunez")
myFullname(lastname_name = "Nunez", first_name = "Darwin")

def myFruit(fruits):
    for fruit in fruits:
        print(fruit)

fruits = ["Apple", "Banana", "Coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))