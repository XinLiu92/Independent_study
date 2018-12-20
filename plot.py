# importing the required module 
import matplotlib.pyplot as plt 
from scipy.interpolate import spline
import numpy as np


def main():
	pkloss = []
	th = []
	lentency = []
	f = open("data.txt")

	line = f.readline()

	while line:
		
		if len(line) == 1:
			line = f.readline()
			continue
		arr = line.split()
		#print(len(line))
		arr = line.split()
		
		th.append(arr[1])
		pkloss.append(arr[2])
		lentency.append(arr[0])
		line = f.readline()

	f.close()
	
	x1 = []
	y1 = []

	x10=[]
	y10=[]

	x100=[]

	y100=[]

	x500 = []
	y500 = []

	x1000 = []
	y1000 = []



	
	for i in range(0,len(th)):
		

		if i <= 5:
			x1.append(float(pkloss[i]))
			y1.append(float(th[i]))
		elif i<=11:
			x10.append(float(pkloss[i]))
			y10.append(float(th[i]))
		elif i<=17:
			x100.append(float(pkloss[i]))
			y100.append(float(th[i]))
		elif i<=23:
			x500.append(float(pkloss[i]))
			y500.append(float(th[i]))
		else:
			x1000.append(float(pkloss[i]))
			y1000.append(float(th[i]))
	
	# x1arr = np.array(x1)
	# y1arr = np.array(y1)


	# x10arr = np.array(x10)
	# y10arr = np.array(y10)

	# x100arr = np.array(x100)
	# y100arr = np.array(y100)


	'''
	# xnew1 = np.linspace(x1arr.min(),x1arr.max(),300)
	# ynew1 = spline(x1arr,y1arr,xnew1)
	# ms1, = plt.plot(xnew1,ynew1,'C1',label='1ms')
	# xnew10 = np.linspace(x10arr.min(),x10arr.max(),300)
	# ynew10 = spline(x10arr,y10arr,xnew10)
	# ms10, = plt.plot(xnew10,ynew10,'C2',label='10ms')
	# xnew100 = np.linspace(x100arr.min(),x100arr.max(),300)
	# ynew100 = spline(x100arr,y100arr,xnew100)
	# ms100, = plt.plot(xnew100,ynew100,'C3',label='100ms')
	# ms10 = plt.plot(x10arr,y10arr,'c3',label = '10ms')
	# ms100 = plt.plot(x100arr,y100arr,'c2',label = '100ms')
	# ms1 = plt.plot(x1arr,y1arr,'c1',label = '1ms')
	'''
	ms1 = plt.plot(x1,y1,'C1',label = '1ms')
	ms10 = plt.plot(x10,y10,'C2',label = '10ms')
	ms100 = plt.plot(x100,y100,'C3',label = '100ms')
	ms500 = plt.plot(x500,y500,'C4',label = '500ms')
	ms1000 = plt.plot(x1000,y1000,'C5',label = '1s')

	plt.legend()
	# naming the x axis 
	plt.xlabel('packet loss(%) ') 
	# naming the y axis 
	plt.ylabel('throughtput (mbps)') 
	# giving a title to my graph 
	plt.title('packet loss vs throughtput') 

	# function to show the plot 
	plt.show() 
	
if __name__== "__main__":
  
  main()
