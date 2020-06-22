import matplotlib.pyplot as plt
def Import(Path):
    infile = open(Path,'r')
    lineStr = [] #Leere liste
    for line in infile:
        lineStr.append(line) #Jede Zeile wird angehangen
    infile.close()

    time_temp1 = lineStr[1].split(' ') # split label and numbers
    data_temp1 = lineStr[2].split(' ')

    time = [float(i) for i in time_temp1[1].split('-')]
    data_temp2 = data_temp1[1].replace(',','.')
    data = [float(i) for i in data_temp2.split('-')]

    data = {lineStr[0].strip(): {time_temp1[0]: time, data_temp1[0]: data}}

    #print(type(time))

    return data

daten = Import(r'C:\Users\Marvi\Documents\Pycharm_Projects\Python_IAF\UE_2\data_export.txt')
print(daten['Probe1']['Zeit'])
print(daten['Probe1']['Wert'])

#Erstelle labels
keys = []
labels = []
for key1 in daten:
    keys.append(key1)
    for key2 in daten[key1]:
        labels.append(key2)
        print(labels)


plt.figure()
plt.plot(daten['Probe1']['Zeit'],daten['Probe1']['Wert'])
plt.xlabel(daten['Probe1']['Zeit'][1])
plt.xlabel(labels[0])
plt.ylabel(labels[1])
plt.show()