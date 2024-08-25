"""
#
# Part" Python Try Exception
# 
"""

try:
    print(x)
except NameError as e:
    print("Not Defind :", e)
except Exception as e:
    print("Something else went wrong! -", e)

try:
    print("Hello World")
except:
    print("Something else went wrong!")
else:
    print("Nothing went wrong!")
finally:
    print("Finished!!")

# x = -1
# if x < 10:
#    raise Exception("Sorry, number below zero")

x = "Hello"
if not (type(x)is int):
    raise TypeError("Only integers are allowed")
