import numpy as np

directory = './LNA_outnet_data/'

# Add 3 columns to original matrix to store the check results
outputdata = np.loadtxt('sweep_combinations_head6.txt')
newcolumn = np.zeros((outputdata.shape[0], 3))
outputdata = np.hstack((outputdata, newcolumn))

def biggerOrNot(args):
	inputarray, threshold = args
	return int((inputarray >= threshold).all())

# Use line number to open corresponding data file
for i in range(outputdata.shape[0]):
	inputdata = np.loadtxt(directory+'spec_'+ str(i+1) +'.txt', skiprows=1)
	# inputdata = checkFreq(inputdata, 7000000000.000000, 9000000000.000000)
	firstwithin = (inputdata[:,0] >= 7e9) & (inputdata[:,0] <= 9e9)

	output = map(biggerOrNot, [(-inputdata[firstwithin, 1],-14.5), (inputdata[firstwithin, 2],-14), (inputdata[firstwithin, 3],2.5)])
	print(list(output))

	inputdata = np.array([-inputdata[firstwithin,1], inputdata[firstwithin,2], inputdata[firstwithin,3]])
	print(inputdata.shape)

	output = (inputdata >= np.array([k * np.ones(firstwithin.sum()) for k in [-14.5, -14, 2.5]])).all(axis=1) # 3 * no. of points
	print(output)

	outputdata[i,9:] = output.copy()

# print(inputdata)
