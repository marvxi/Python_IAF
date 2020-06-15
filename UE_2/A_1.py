x = []

for i in range(1,11):
    for j in range(1,11):
        print('{}x{}={}\t'.format(i,j,i*j), end='') # Einsetzen der Werte in der Reihenfolge von format
                                                    # \t horizontaler tab, end='' nächste Zeile

    print()