<h2 id="-" dir="rtl">برنامه‌ای که عددی را خوانده، تشخیص می‌دهد آیا این عدد Strong است یا خیر⁉️</h2>

<p dir="rtl">عددی Strong است که حاصل جمع فاکتوریل ارقام آن برابر خود آن عدد باشد.</p>

```python
from math import factorial

number = input()
result = 0

for i in number:
    result += factorial(int(i))

if result == int(number):
    print("This number is a Strong number!")
else:
    print("This number isn't a Strong number!")
```
