zahl = int(100)
a,b = 0,1
for i in range(zahl):
    a,b = b, a+b

print(b)