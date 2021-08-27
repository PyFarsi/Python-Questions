from math import factorial

number = int(input())
digits = str(factorial(number))

print(sum(map(int, digits)))
