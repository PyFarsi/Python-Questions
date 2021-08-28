<h1 dir="rtl">برنامه‌ای که عددی را خوانده، تشخیص می‌دهد عددی Armstrong است یا خیر⁉️</h1>

<p dir="rtl">عددی Armstrong است که مجموع ارقام به توان تعداد ارقام برابر خود عدد باشد.</p><br>

```python
number = input()
aggregate = sum([int(i)**len(number) for i in number])

if number == aggregate:
    print("This number is an Armstrong number!")
else:
    print("This number isn't an Armstrong number!")
```
