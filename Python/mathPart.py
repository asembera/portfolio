import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys
import cv2 
import numpy as np
import os


"""
This code runs through the files that were written from finalCode.py.
It then calculates the ratio of dead to alive and the percentage
of dead worms within each plate. Then it creates a histogram visully 
representing the number of plates that have a certain number of dead 
worms.
"""

#reads input from terminal (should be the names of the text files)
filename = sys.argv[1]
filename2 = sys.argv[2]


#opens and reads each txt file
infile = open(filename, "r")
infile2 = open(filename2, "r")

read = infile.readlines()
read2 = infile2.readlines()

infile.close()
infile2.close()

#creates lists and appends the values from the txt files
#w1 is the dead nematoads and binary is the alive
w1List = []
binaryList = []

for i in read:
	w1List.append(int(i))

for j in read2:
	binaryList.append(j.strip("\n"))



#makes binary lists into integers so math can be done
intBiList = []
for k in binaryList:
	intBiList.append(int(k))



#creates a list of the ratios of alive to dead
#also creates counters for loop
count = 0
ratioList = []
count2 = 0

xList =[]
yList = []
ratioPlot = []



aliveList = []
#creates ratio of alive to dead and appends to list
for num in range(len(w1List)):
	dead = w1List[count2]
	numberOfAlive = intBiList[count2] - dead
	if numberOfAlive == 0:
		numberOfAlive = 1
	aliveList.append(numberOfAlive)
	alive = str(abs(numberOfAlive))
	ratio = alive + ":"+str(w1List[count2])
	ratioList.append(ratio)
	xList.append(w1List[count2])
	#yList.append(numberOfAlive)
	ratioPlot.append(abs((numberOfAlive)))
	count2 += 1
	
#print(ratioPlot)
#print statements to make output look cleaner
print("="* 50)
print("Percentage of dead nematodes in each plate")
print("="* 50)
imgName = open("imgNametxt.txt", "r")
read1 = imgName.readlines()
imgName.close()
percentageList = []
count4 = 0
#finds and prints the percentage of dead in each plate
for i in read1:
	
	percentage = w1List[count4]/intBiList[count4]*100
	percentage = format(percentage, '.2f')
	percentageList.append(str(i.strip("_binary.png\n")) + ": " + str(percentage) + "%")
	count4 += 1

print(percentageList)
#print(ratioList)


for i in range(len(ratioList)):
	yList.append(i)

#print(len(yList))
#print(len(ratioPlot))


#Creates and displays histogram of the number of dead nematodes in each plate
colors = (0,0,0)
area = np.pi*3
bins=100
n, bins, patches =plt.hist(w1List,bins, facecolor = 'blue', alpha = .5)
plt.title("Nematodes Histogram")
plt.xlabel("Dead")
plt.ylabel("Number of Plates")
plt.show()






