a = 10
b = 6
sum = a + b
print("sum of a and b is:",sum) 

a = 5.2
b = 3.8
sum = a + b
print("sum of a and b is:",sum) 


first_value = int(input("Enter the first value to be added:"))
second_value = int(input("Enter the second value to be added:"))
sum = first_value + second_value
print("sum of first_value and second_value is:",sum) 


def adding_numbers(a, b):
    while True:
        try:
            a = int(input("Enter the first value to be added:"))
            b = int(input("Enter the second value to be added:"))
            break
        except ValueError:
            print("Please enter valid numbers.")
            
    return a + b

sum = adding_numbers(a, b)
print("sum of a and b is:",sum) 