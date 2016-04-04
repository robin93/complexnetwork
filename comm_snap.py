import pandas as pd
import snap
import csv

G1 = snap.TUNGraph.New()
list_of_nodes = list()
row_number = 0
with open('reciprocating_edge_list.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			# if row_number > 10:
			# 	break
			row_number += 1
			source = int(row[0])
			destination = int(row[1])
			if source not in list_of_nodes:
				G1.AddNode(source)
				list_of_nodes.append(source)
			if destination not in list_of_nodes:
				G1.AddNode(destination)
				list_of_nodes.append(destination)
			G1.AddEdge(source,destination)
			print source
			print row

print list_of_nodes

print "G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges())

GOut = snap.ConvertGraph(snap.PUNGraph, G1)

print "GOut: Nodes %d, Edges %d" % (GOut.GetNodes(), GOut.GetEdges())

CmtyV = snap.TCnComV()
modularity = snap.CommunityGirvanNewman(GOut, CmtyV)

comm_number = 1
comm_number_nodes_dict = dict()
for Cmty in CmtyV:
	comm_number_nodes_dict[comm_number] = list(Cmty)
    	comm_number += 1

print "The modularity of the network is %f" % modularity
print comm_number_nodes_dict

grid_community_df = pd.DataFrame(columns = ['nodes','community_number'])

df_index = 0
for key in comm_number_nodes_dict.keys():
	for grids in comm_number_nodes_dict[key]:
		grid_community_df.set_value(df_index,['nodes','community_number'],[grids,key])
		df_index += 1
print grid_community_df

grid_community_df.to_csv('GridCommunityMapping.csv',sep = ',',index = False)