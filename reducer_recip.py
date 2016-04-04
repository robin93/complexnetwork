#!/usr/bin/python
import sys


# sys.stdout = open("timestamp_edgestr1_edgestr2.txt", "w")
running_timestamp = None
running_node1 = None
running_node2 = None
running_edge_strength = 0
current_edge_strength = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	time_nodepair_key,edge_strength = data[0],int(data[1])
	time_nodepair_key2 = time_nodepair_key.split('[')
	time_nodepair_key3 = time_nodepair_key2[1].split("]")
	time_nodes = time_nodepair_key3[0].split(",")
	timestamp,node1,node2 = int(float(time_nodes[0])),int(time_nodes[1]),int(time_nodes[2])
	if (running_timestamp!= timestamp or running_node1 != node1 or running_node2 != node2):
	   	running_timestamp,running_node1,running_node2 = timestamp,node1,node2
	   	running_edge_strength = edge_strength
	elif (running_timestamp == timestamp and running_node1 == node1 and running_node2 == node2):
		if edge_strength > running_edge_strength:
			print '%s\t%s'%([timestamp,running_edge_strength,edge_strength],1)
		else:
	  	 	print '%s\t%s'%([timestamp,running_edge_strength,edge_strength],1)