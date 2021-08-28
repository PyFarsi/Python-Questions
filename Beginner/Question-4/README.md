<h1 dir="rtl">برنامه‌ای که دو رشته دریافت کرده و رشته دوم را وسط رشته اول قرار دهد.</h1>

<p dir="rtl"><b>توجه: </b>تضمین می‌شود تعداد کاراکترهای رشته اول عددی زوج باشد.</p>

```python
string1 = input()
string2 = input()
middle = len(string1)//2

print(string1[0:middle] + string2 + string1[middle:])
```
