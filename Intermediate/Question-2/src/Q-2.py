number = input()
aggregate = sum([int(i)**len(number) for i in number])

if number == aggregate:
    print("This number is an Armstrong number!")
else:
    print("This number isn't an Armstrong number!")