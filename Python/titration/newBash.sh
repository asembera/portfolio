#!/bin/bash

for f in *.png; 

do
	python newTitration.py "$f"

done
