#!/usr/bin/python
#the above shebang line ensures that the correct version of python is being used
import sys

def strength_factor_level(edge_strength):
	if (edge_strength<4.9537572503600E-05):
		return 1
	elif(edge_strength>4.9537572503600E-05 and edge_strength<0.000378677825463000):
		return 2
	elif(edge_strength>0.000378677825463000):
		return 3

# stop_index = 0
for line in sys.stdin:
	# stop_index += 1
	# if stop_index > 10:
	# 	break
	data = line.strip().split("\t")
	timestamp,source,dest,edge_strength = (int(data[0]) - 1.38386520000E+12)/600000,int(data[1]),int(data[2]),strength_factor_level(float(data[3]))
	if source > dest:
		print [timestamp,dest,source],"\t",edge_strength
	elif dest > source:
		print [timestamp,source,dest],"\t",edge_strength