import networkx as nx
#import community
import snap
import csv

edge_pair_list = list()
#row_number = 0
# with open('reciprocating_edge_list.csv', 'rb') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#         for row in spamreader:
# 		edge_pair_list.append([int(float(row[0])),int(float(row[1]))])

# print edge_pair_list

# G = nx.Graph()
# G.add_edges_from(edge_pair_list)

# G = snap.LoadEdgeList("reciprocating_edge_list.csv")

# print type(G)

# G2 = snap.TUNGraph.Load(G)

# CmtyV = snap.TCnComV()
# modularity = snap.CommunityGirvanNewman(G2, CmtyV)

# print "The modularity of the network is %f" % modularity

# dendo = community.generate_dendogram(G)
# print dendo
# part = community.best_partition(G)
# print part

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
print type(UGraph)
print UGraph
# CmtyV = snap.TCnComV()
# modularity = snap.CommunityGirvanNewman(UGraph, CmtyV)
# for Cmty in CmtyV:
#     print "Community: "
#     print Cmty
# print "The modularity of the network is %f" % modularity