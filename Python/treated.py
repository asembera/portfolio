import sys 
import cv2
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


"""
This code predicts whether a plate was treated or untreated based off of our method
of counting dead and alive. It then tests how accurate we were at predicting by 
comparing it to the known data from the paper. Columns 1-12 were treated and 
13-24 were untreated so we were able to compare our 1-12 and 13-24 to that.
Displays a bar graph that visually represents how accurate we were to the 
actual number.
"""

#reads in the file with names of each image and the number of dead 
imgName = open("imgNametxt.txt", "r")
w1List = open("contourCount.txt", "r")

read1 = imgName.readlines()
read2 = w1List.readlines()

imgName.close()
w1List.close()

#creates and appends lists for image names and number of dead
imgNameList = []
deadList = []

for i in read1:
	imgNameList.append(i)

for j in read2:
	deadList.append(j)

#counts total number of treated and untreated
treated = 0
untreated = 0

#creates a list that will have the name of a plate, the number of dead and whether or not we called it treated
wormList = []

#shows what we called treated and untreated based on our code 
for k in range(100):
	if int(deadList[k]) <= 3:
		#print("#")
		#print(imgNameList[k] + deadList[k] + "treated" + "\n")
		wormList.append(str(imgNameList[k] + deadList[k] + "_treated"))
		treated += 1
		
	else:
		#print("#")
		#print(imgNameList[k] + deadList[k] + "untreated" + "\n")
		wormList.append(str(imgNameList[k] + deadList[k] + "_untreated"))
		untreated += 1

#creates lists used in next part
aList1 = []
aList2 = []
bList1 = []
bList2 = []
cList1 = []
cList2 = []
dList1 = []
dList2 = []
eList1 = []

count = 0

#splits up each set of plates based on treated and untreated
#1-12 is treated 13-24 is untreated

while "A13" not in wormList[count]:
	aList1.append(wormList[count])
	count += 1

while "B01" not in wormList[count]:
	aList2.append(wormList[count])
	count += 1


while "B13" not in wormList[count]:
	bList1.append(wormList[count])
	count += 1
	
	
while "C01" not in wormList[count]:
	bList2.append(wormList[count])
	count += 1


while "C13" not in wormList[count]:
	cList1.append(wormList[count])
	count += 1
	
	

while "D01" not in wormList[count]:
	cList2.append(wormList[count])
	count += 1

while "D13" not in wormList[count]:
	dList1.append(wormList[count])
	count += 1

while "E01" not in wormList[count]:
	dList2.append(wormList[count])
	count += 1
	#print(count)

while "E04" not in wormList[count]:
	eList1.append(wormList[count])
	count += 1
	if "E04" in wormList[count]:
		eList1.append(wormList[count])
	


#counters of how correct we were for each group
#used to create graph later
Aincorrect = 0
Bincorrect = 0
Cincorrect = 0
Dincorrect = 0
Eincorrect = 0
Acorrect = 0
Bcorrect = 0
Ccorrect = 0
Dcorrect = 0
Ecorrect = 0

#variables to tally total number of correct and incorrect
incorrect = 0
correct = 0


#goes through each of the previous lists and counts where we were correct and incorrect
#compares what we called each plate to what the plate actually was to see if we were correct
for i in aList1:
	if "untreated" in i:
		incorrect += 1
		Aincorrect+= 1
	else:
		correct += 1
		Acorrect+= 1


for i in aList2:
	if "untreated" in i:
		correct += 1
		Acorrect+= 1
	else:
		incorrect += 1
		Aincorrect+= 1

for i in bList1:
	if "untreated" in i:
		incorrect += 1
		Bincorrect+= 1
	else:
		correct += 1
		Bcorrect+= 1

for i in bList2:
	if "untreated" in i:
		correct += 1
		Bcorrect+= 1
	else:
		incorrect += 1
		Bincorrect+= 1


for i in cList1:
	if "untreated" in i:
		incorrect += 1
		Cincorrect+= 1
	else:
		correct += 1
		Ccorrect+= 1

for i in cList2:
	if "untreated" in i:
		correct += 1
		Ccorrect+= 1
	else:
		incorrect += 1
		Cincorrect+= 1


for i in dList1:
	if "untreated" in i:
		incorrect += 1
		Dincorrect+= 1
	else:
		correct += 1
		Dcorrect+= 1


for i in dList2:
	if "untreated" in i:
		correct += 1
		Dcorrect+= 1
	else:
		incorrect += 1
		Dincorrect+= 1

for i in eList1:
	if "untreated" in i:
		incorrect += 1
		Eincorrect+= 1
	else:
		correct += 1
		Ecorrect+= 1



#calculates and displays our percent error for predicting whether or not a plate was treated
percentError = (correct - 100)
accuracy = 100 - abs(percentError)
print(int(accuracy),"%", "accurate in predicting if treated or untreated")

#variables used for representing control on graph
controlTreated = 52
controlUntreated = 48
AControl = 24
BControl = 24
CControl = 24
DControl = 24
EControl = 4

#creates graph
objects = ('A Control','A Correct','A Incorrect','B Control','B Correct','B Incorrect','C Control','C Correct','C Incorrect','D Control','D Correct','D Incorrect','E Control','E Correct','E Incorrect')

y_pos = np.arange(len(objects))
yAxis = [AControl, Acorrect,Aincorrect,BControl, Bcorrect,Bincorrect,CControl, Ccorrect,Cincorrect,DControl,
Dcorrect,Dincorrect,EControl, Ecorrect,Eincorrect,]

plt.bar(y_pos, yAxis, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Plates')
plt.title('Known vs Experimental')

plt.show()
