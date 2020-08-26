import numpy as np
import webbrowser

def a():
    A = np.array([[1,-2,1],
                  [2,1,-1],
                  [-1,-4,3]])

    l = np.array([[6],[-3],[14]])

    #Prüfe vorab Determinate

    print(f'Die Determinate lautet: {np.linalg.det(A):.0f}')

    if np.linalg.det(A) > 0:
        x = np.linalg.solve(A,l)
        print(f'Der Vektor x lautet: {x}')
#a()

def b():
    A = np.array([[1,1,1],
                  [1,-3,4],
                  [3,-2,-2]])

    b = np.array([[4],[33],[2]])

    print(f'Die Determinate lautet: {np.linalg.det(A):.0f}')

    if np.linalg.det(A) > 0:

        inverse = np.linalg.inv(A) #berechnet die inverse
        print(f'Der Lösungsvektor lautet: {inverse.dot(b)}')


#b()

def c():
    A = np.array([[2,1,2],
                  [1,0,1],
                  [4,1,4]])

    b = np.array([[1],[4],[0]])

    try:
        x = np.linalg.solve(A,b)
    except:
        print('Matrix ist singulär, verwende Nährungslösung')
        x = np.linalg.lstsq(A,b,rcond=None)

    print(f'Der Lösungsvektor lautet: {x}')

#c()

def d():
    A = np.array([[np.pi, 2.5],
                  [np.exp(1),0.1]])

    key = np.array([[190.58097349],[143.15889764]])

    try:
        target = np.linalg.solve(A,key)
    except:
        target = np.linalg.lstsq(A,b,rcond=None)
    print(target[0][0])

    webbrowser.open(f'https://www.google.de/maps/place/{target[0][0]}+{target[1][0]}')


#d()

def e():

    def lösung(A,b):

        # Berechne ob Matrix invertierbar ist
        try:
            inv = np.linalg.inv(A)
            print(f'Die inverse der Matrix A lautet: {inv}')
        except:
            lös = np.linalg.lstsq(A,b,rcond=None)
            print(f'Matrix ist nicht invertierbar, verwende Nährungslösung: {lös}')
            exit()

        det = np.linalg.det(A)
        if det <= 0:
            lös = np.linalg.lstsq(A,b,rcond=None)
            print(f'Die Determinate der Matrix A ist: {det:.0f}, verwende Nährungslösung: {lös} ')

        else:
            lös = np.linalg.solve(A,b)
            print(f'Die Determinate der Matrix A ist: {det:.0f} , verwende direkte Lösung: {lös}')



        #try:
        #    lös = np.linalg.solve(A,b)
#
        #except:
        #    print('Lösung nicht eindeutig verwende Nährung:')
        #    lös = np.linalg.lstsq(A,b,rcond=None)
        #print(lös)





    A = np.array([[3,1,1],
                  [8,0,7],
                  [8,0,9]])

    b = np.array([[6],[10],[2]])
    #lösung(A,b)

    A = np.array([[4,0,6,5],
                 [8,7,1,9],
                 [5,5,9,6],
                 [6,7,2,6]])
    b = np.array([[8],[4],[1],[8]])
    #lösung(A,b)

    A = np.array([[0.43, 0.20, 0.87 ,0.15],
                  [0.23,0.97,0.76,0.61],
                  [0.38,0.59,0.47,0.04]])

    b = np.array([[0.77],[0.99],[0.15]])
    #lösung(A,b)

    A = np.array([[62,-8,86,72],
                  [-52,40,92,20],
                  [97,91,1,-77],
                  [57,-25,2,74],
                  [-61,69,99,-87],
                  [60,1,-11,-91,]])

    b = np.array([[69],[60],[-33],[6],[50],[-60]])
    #lösung(A,b)

    A = np.array([[-28,-90,52,-49],
                  [8,98,-13,-97],
                  [-10,26,64,-54],
                  [82,-98,-81,46]])
    b = np.array([[97],[-20],[35],[-56]])
    #lösung(A,b)

    A = np.array([[9,-3,6],
                  [-4,-6,2],
                  [-7,-5,0]])
    b = np.array([[15],[-99],[-51]])
    #lösung(A,b)

    A = np.array([[1,-8,-6],
                  [-5,-1,4],
                  [5,-9,9]])
    b = np.array([[68],[36],[-24]])
    #lösung(A,b)



#e()

