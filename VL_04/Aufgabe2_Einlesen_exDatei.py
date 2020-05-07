Datei = open('water.txt','r')

Datei.readline()#Erste Zeile überlesen

numbers=[] # initialisieren !
months=[]

for line in Datei:

    strings=line.split()# Da wo zwischenräume sind wird gesplittet
    month=strings[0] #Erste spalte
    number = float(strings[1]) #Zweite spalte
    numbers.append(number)#Anhängen
    months.append(month)

Datei.close()

for i in range(1,13):
    print('%-10s %-10g' %(months[i-1],numbers[i-1])) # Weil in der zweiten Zeile gestartet wird