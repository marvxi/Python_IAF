def someFunc(f1,f2,f3):
    summe = f1+f2+f3
    produkt = f1*f2*f3
    maximal = max([f1,f2,f3])
    minimal = min([f1,f2,f3])
    return summe,produkt,[maximal,minimal]
print('Summe: {},Produkt: {}, Max/Min: {}'.format(someFunc(1,2,3)[0],someFunc(1,2,3)[1],someFunc(1,2,3)[2]))