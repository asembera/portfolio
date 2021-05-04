import cv2 
import numpy as np
import os
from PIL import Image
import sys 


"""
This code reads in frames from the titration video.
It then crops out a specific part of the image to be analyzed.
It splits up the color channels and finds the ratios of each color in the
picture and writes the values to a file called newMethod.txt

meant to be run through the bash script called newBash.sh
"""



filename = sys.argv[1]
if "image" in filename:
	

	#reads in the image, crops a rectangle out and finds the 
	#average values for each of the color channels
	img = cv2.imread(filename)
	crop = img[238:355, 291:584]
	b, g, r =cv2.split(crop)
	greenAvg = np.mean(g)
	blueAvg = np.mean(b)
	redAvg = np.mean(r)
	

	#creates variables for the ratios of the colors to each other
	blue2red = blueAvg/redAvg
	blue2green = blueAvg/greenAvg
	red2green = redAvg/greenAvg
	
	#writes the data to a text file
	output = str(blue2red) + "  " + str(blue2green) + " " + str(red2green) +  " "+ str(filename)
	print(output)
	outfile = open("newMethod.txt", "a")
	outfile.write(output)
	outfile.write("\n")
	outfile.close()

