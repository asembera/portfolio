#!/bin/bash

for f in *.tif; 

do
	python finalCode.py "$f"

done

for f in *.png; 

do
	python finalCode.py "$f"

done
