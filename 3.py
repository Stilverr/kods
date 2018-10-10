s = input("Введите символ: ")
t = input("Введите какой либо текст: ")
a = t.split(s)
m = 0
for i in range(1,len(a)):
    if len(a[m]) > len(a[i]):
        m = i
print(a[m])
