<h2 id="-" dir="rtl">محاسبه جمع ارقام فاکتوریل</h2>

<p dir="rtl">برنامه‌ای که با گرفتن یک عدد حسابی، حاصل‌جمع ارقام فاکتوریل آن عدد را محاسبه می‌کند.<br><br><b>برای مثال:</b><br>27 = 3+6+2+8+8+0+0 ➡ 3628800 = !10</p>

```python
from math import factorial

number = int(input())
digits = str(factorial(number))

print(sum(map(int, digits)))
```
