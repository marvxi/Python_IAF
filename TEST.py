import openpyxl as opx

fileName = r'C:\Users\Marvi\OneDrive\03_Studium Unterlagen\10_Master\03_Semester\02_Python\02_UE/MeineDaten.xlsx'
wb = opx.load_workbook(filename=fileName)

ws = wb['Tabelle1']

# Wie lang ist das Datenset?

count = 0
field = 'A'
data = ''

while data != None:
    count+=1
    data = ws['A' + str(count)].value
