def inputdata(filename):
    infile=open(filename,'r')
    infile.readline()
    data = {}  #Initialsierung des Dictionary
    for line in infile:
        strings=line.split()
        month=strings[0]
        number=float(strings[1])
        data[month]=number
    infile.close()
    return data

outfile=open('table.txt','w')
data = inputdata('water.txt')
print(data)
for month in data:
    outfile.write('%-10s %10g\n' %(month,data[month]))

outfile.close()