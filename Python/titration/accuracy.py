import cv2
import matplotlib.pyplot as plt


"""
This program reads the data that was created in newMethod.py.
it then finds the equivalence point from the provided data
and compares the results from the code to the actual results.
"""


#reads the frames from the text file
infile = open("frameNames.txt", "r")
nameRead = infile.readlines()
nameList = []
#creates list of names
for i in nameRead:
	nameList.append(i)



#gets the first frame from the list
#which is the only one that is needed
name = ( " " + str(nameList[0]))

#gets just the number
numName = name.split("-")
numName = numName[1]
numName = numName.strip(".png\n")

print("\n")
print("=" * 100)
print("The equivalence point that our code found is at frame ", numName)

time = int(numName)
print("\nThe time our code said it took to reach the equivalence point was ", "%.2f" % time,"seconds")


numName = int(numName)

fileName = ("pH.txt")




pHlist = []
seconds = []

#reads in the slopes from the given data
#used to find the equivalence point
#max slope is the equivalence point
slopeFile = open("slope.txt", "r")
slopes = slopeFile.readlines()
slopeFile.close()
slopeList  = []

count3 = 0
for i in slopes:
	i = i.strip("\n")
	i = float(i)
	slopeList.append(i)
	count3 += 1

maxSlope = max(slopeList)
index = 0
count4 =1
#finds the frame that is associated with the highest slope
while True:
	num = slopeList[index]
	if num == maxSlope:
		goodFrame = count4
		break
	count4 += 1
	index += 1

goodFrame = int(goodFrame)



#compares the results of the code to the actual data
difference = numName - goodFrame
difference = abs(difference)
neutralTime = goodFrame
timeDiff = time - neutralTime
timeDiff = abs(timeDiff)

print("\nThe actual equivalence point is frame ", goodFrame)
print("The actual time it took to reach the equivalence point was ", "%.2f" %  neutralTime, "seconds")
print("\nWe were off by ", difference, "frames", "and", "%.2f" % timeDiff, "seconds")
print("=" * 100)
