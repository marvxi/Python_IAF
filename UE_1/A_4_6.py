import matplotlib.pyplot as plt
def iter():
    n = 100
    a,b = 0,1
    x = []
    y = []
    for i in range(n):
        a,b = b, a+b
        x.append(i)
        y.append(a)

    print(a)
    plt.plot(x,y)
    plt.show()


iter()


#----Erklärung zur schreibweise in der for schleife
a,b = 3,2
a,b = b,a+b
print(a)
print(b)


#------Rekusiv, dauert extrem Lange!
#import sys
#sys.setrecursionlimit(10000)
def recusi(zahl):
    if zahl <= 1:
        return zahl
    else:
        return recusi(zahl-1)+recusi(zahl-2)
#print(recusi(50))