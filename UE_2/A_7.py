liste = ["hallo","Welt","test","bla","hatischi","steffi"]
#print('{}+{}'.format(liste[0],liste[1]))

def umwandlung(liste):
    for i in range(len(liste)):
        if i < (len(liste)-1):
            print('{}+'.format(liste[i]),end='')
        else:
            print('{}'.format(liste[i]),end='')

umwandlung(liste)