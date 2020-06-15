def Import(Path):
    infile = open(Path,'r')
    lineStr = [] #Leere liste
    for line in infile:
        lineStr.append(line) #Jede Zeile wird angehangen
    infile.close()
    

    dic = {'Probe1': {'Zeit':textDatei[1],'Wert':textDatei[2]}}

print(dic['Probe1']['Zeit'])

Import(r'C:\Users\Marvi\Documents\Pycharm_Projects\Python_IAF\UE_2\data_export.txt')