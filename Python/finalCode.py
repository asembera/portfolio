#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:26:38 2019

Code is meant to be run through a bash script to go through a folder of images.

This code reads in nematode images using either the w1 or binary images.
It then draws contours over each worm in the image. It uses the average
value of a worm to decide what is called a worm and how many times it is 
counted. It then writes the number of worms that is found for the image to 
a file. Also writes to a file the plate names taken from the binary images.

"""
import cv2
import sys
import os 
import numpy as np
import math


#Create List 
w1List = []
w2List = []
fileNameList = []

#threshold variables
t = 50
t2 = 10

#terminal argument
img = sys.argv[1]


#counters for loops
num = 0
num2 = 0


#average area for the contour of a worm found through worm codes
avgArea = 890

#looks at the w1 images
if "w1" in img:
	#reads in image, blurs, thresholds
	readImage = cv2.imread(filename = img)
	blur = cv2.cvtColor(src = readImage, code = cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(src = blur, ksize = (13,13), sigmaX = 0)
	(t, threshImg) = cv2.threshold(src = blur, thresh = t, maxval = 255, type = cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	(_, contours, hierarchy) = cv2.findContours(image = threshImg, mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
	

	#draws and displays contours
	cv2.drawContours(image = readImage, contours = contours, contourIdx = -1, color =  (0,0,255), thickness = 2)

	#cv2.namedWindow("contours", flags = cv2.WINDOW_NORMAL)
	#cv2.imshow("contours", mat = readImage)
	#cv2.waitKey(0)
	

	#goes through each contour and adds the coordinates to a list
	ptsList = []
	areaList = []

	for i in contours:
		ptsList.append(i)

	#uses the coordiantes of each contour to find the area 
	for x in ptsList:
		cnt = x
		area = cv2.contourArea(cnt)
		areaList.append(area)
	
	#code to see average contour area for each image (used when testing it)
	#avgContArea = sum(areaList)/len(areaList)
	#print(avgContArea)

	#a percentage of the average of the contour area of each worm
	#percentage because the contours of worms vary b/c of image quality
	percentage = avgArea*.15
	

	#counts each contour based off area
	for area in areaList:
		if area >= percentage and area < (avgArea * 1.5):
			#print("First if")
			num +=1
			
		if area >= (avgArea*1.5) and area < (avgArea* 3):
			#print("Second if")
			num += 2

		if area >= (avgArea*3) and area < (avgArea*4):
			#print("Third if")
			num += 3 

		if area >= (avgArea*4):
			#print("Fourth if")
			num += 4


	#appends it to list and writes it to file
	w1List.append(num)
	filename = "contourCount.txt"
	outfile = open(filename, "a")
	outfile.write(str(num)+ "\n")
	outfile.close()

	print(w1List)	
	print("#" * 50)	

#looks at binary images (from the foreground folder from website)
if ".png" in img:
	#reads in image, blurs, thresholds
	readImage = cv2.imread(filename = img)
	gray = cv2.cvtColor(src = readImage, code = cv2.COLOR_BGR2GRAY)
	
	(_, contours, hierarchy) = cv2.findContours(image = gray, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)
	

	#draws and displays contours
	cv2.drawContours(image = readImage, contours = contours, contourIdx = -1, color = (0,0,255), thickness = 2)
	
	#cv2.namedWindow("contours", flags = cv2.WINDOW_NORMAL)
	#cv2.imshow("contours", mat = readImage)
	#cv2.waitKey(0)
	
        

	#goes through each contour and adds the coordinates to a list
	ptsList =[]
	areaList = []

	#uses the coordiantes of each contour to find the area
	for i in contours:
		ptsList.append(i)
	for x in ptsList:
		cnt = x
		area = cv2.contourArea(cnt)
		areaList.append(area)

	#avgContArea = sum(areaList)/len(areaList)
	#print(avgContArea)

	#a percentage of the average of the contour area of each worm
	#percentage because the contours of worms vary b/c of image quality
	percentage = avgArea*.45

	#counts each contour based off area
	for area in areaList:
	
		if area >= percentage and area < (avgArea * 1.5):
			#print("First if")
			num2 +=1
			
		if area >= (avgArea*1.5) and area < (avgArea* 3):
			#print("Second if")
			num2 += 2

		if area >= (avgArea*3) and area < (avgArea*4):
			#print("Third if")
			num2 += 3 

		if area >= (avgArea*4):
			#print("Fourth if")
			num2 += 4

	#appends it to list and writes it to file
	w2List.append(num2)
	filename = "contourCountBinary.txt"
	outfile = open(filename, "a")
	outfile.write(str(num2) + "\n")
	outfile.close()
	print(w2List)
	print("*" * 50)

	imgNametxt = "imgNametxt.txt"
	imgName = open(imgNametxt, "a")
	imgName.write(str(img))
	imgName.write("\n")
	imgName.close()






































     


        
        
        
