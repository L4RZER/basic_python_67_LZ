even_numbers = []
odd_numbers = []

for number in range(21, 41):
    if number % 2 == 0:  
        even_numbers.append(number)
    else:  
        odd_numbers.append(number)


print("จำนวนคู่:", even_numbers)
print("จำนวนคี่:", odd_numbers)
