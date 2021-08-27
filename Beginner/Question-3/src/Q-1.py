from math import factorial

number = input()
result = 0

for i in number:
    result += factorial(int(i))

if result == int(number):
    print("This number is a Strong number!")
else:
    print("This number isn't a Strong number!")