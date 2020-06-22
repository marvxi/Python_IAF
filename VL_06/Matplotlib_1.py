import matplotlib.pyplot as plt

#1D -Daten
y_1 = [0,1,2,3,4,5,6,7,8,10] # x wert wird automatisch zugewisen 0-x
plt.plot(y_1,label="1D-Daten")
#plt.show()

#2d - Daten
y = [0,1,2,3,4,5,6,7,8,10]
x = [5,7,9,13,14,22,25,30,34,2]
plt.plot(x,y,label="2D-Daten")
#plt.legend(["1D-Daten","2D-Daten"]) #benötigt liste, auf Reihenfolge der plt.plot befehle achten!
plt.legend() # Mit label in plt.plot ist die liste unnötig, Reihenfolge ist auch egal dann!
plt.xlabel("x")
plt.ylabel("y")
plt.title("test")
plt.grid()
plt.show()
