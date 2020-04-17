import numpy as np

directory = './LNA_outnet_data/'

outputdata = np.loadtxt('sweep_combinations_head6.txt')
newcolumn = np.zeros((outputdata.shape[0], 3))
outputdata = np.hstack((outputdata, newcolumn))

def checkFreq(inputarray, upper, lower):
	firstcol = inputarray[:,0]
	firstwithin = (firstcol >= upper) & (firstcol <= lower)
	return inputarray[firstwithin]

def checkS21(inputarray, threshold):
	secondcol = inputarray[:,1]
	secondwithin = secondcol <= threshold
	return int(~secondwithin.any())

def checkS22(inputarray, threshold):
	thirdcol = inputarray[:,2]
	thirdwithin = thirdcol >= threshold
	return int(~thirdwithin.any())

def checkNF(inputarray, threshold):
	fourthcol = inputarray[:,3]
	fourthwithin = fourthcol >= threshold
	return int(~fourthwithin.any())

for i in range(outputdata.shape[0]):
	inputdata = np.loadtxt(directory+'spec_'+ str(i+1) +'.txt', skiprows=1)
	inputdata = checkFreq(inputdata, 7000000000.000000, 9000000000.000000)
	outputdata[i][9] = checkS21(inputdata, 14.5)
	outputdata[i][10] = checkS22(inputdata, -14)
	outputdata[i][11] = checkNF(inputdata, 2.5)

print(outputdata)



