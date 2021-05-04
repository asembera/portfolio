import cv2
import matplotlib.pyplot as plt
import statistics


"""
this code reads in the ratio values that were created
in newTitration.py. It then checks to see if those ratios 
correlate to a pink color. If they do, it will write the frame 
number to a file called frameNames.txt
"""



#reads in file
infile = open("newMethod.txt", "r")

read = infile.readlines()
infile.close()

#typical ratios of the colors to each other
#pinkBR is blue:red, pinkBG is blue:green, pinkRG is red:green
pinkBR = .92
pinkBG = 1.2
pinkRG = 1.3

#creates lists for the ratios to be appended later
BR = []
BG = []
RG = []

#creates variables that will be used to confirm if an image is pink
a = False
b = False
c = False

#list to hold the name and frame number of the frames the code calls pink
nameList = []


#checks the ratios from each image to see if it is pink
for i in read:
	#splits because it is read from lines from a file
	i = i.split()
	name = i[3]
	br = float(i[0])
	bg = float(i[1])
	rg = float(i[2])
	
	
	
	if br >= (pinkBR - .04) and br <= (pinkBR +.04):
		BR.append(br)
		a = True

	
	if bg >= (pinkBG -.09) and bg <= (pinkBG +.09):
		BG.append(bg)
		b = True

	
	if rg >= (pinkRG - .05) and rg <= (pinkRG +.05 ):
		RG.append(rg)	
		c = True
	
	#if all the ratios are within the range, they are assigned true and
	#the frame is appended to the nameList
	if a == True and b == True and c == True:
		nameList.append(name)
	a = False
	b = False
	c = False



#writes all the frames that were considered pink to a file
outfile = open("frameNames.txt", "a")
for i in nameList:
	outfile.write(i)
	outfile.write("\n")
outfile.close()