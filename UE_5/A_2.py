import numpy as np
import matplotlib.pyplot as plt

def conv(x):
    return x.replace(',','.').encode()

filePath = r'C:\Users\Marvi\OneDrive\03_Studium Unterlagen\10_Master\03_Semester\02_Python\02_UE\Datensatz_UE5'

restults = {} #Dictionary
Emoduln = []
VLast = []

def calcEModul(strain,stress):

    pos05 = np.nanargmin(np.abs(strain-0.0005))
    pos0025 = np.nanargmin(np.abs(strain - 0.0025))

    p = np.polyfit(strain[pos05:pos0025],stress[pos05:pos0025],1)

    return p

for i in range(5):
    fileName = '\Specimen_RawData_' + str(i+1) + '.csv'
    rawData = np.genfromtxt((conv(x) for x in open(filePath+fileName)),delimiter=";",skip_header=6)

    results[str(i+1)] = {'movement':rawData[:,1]/1000,'force':rawData[:,2]*1000}
