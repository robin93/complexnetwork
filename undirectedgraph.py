import networkx
import csv

edge_pair_list = list()
row_number = 0
with open('OneTimeStampLevel3.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if row_number != 0:
			pair = [0,0]
			tokens = row[0]
			source = int(float(row[1]))
			destination = int(float(row[2]))
			pair[0],pair[1] = source,destination
			edge_pair_list.append(pair)
			# print source,destination
		row_number += 1
print edge_pair_list

reciprocating_edge_list = list()

with open('reciprocating_edge_list.csv','wb') as csvfile:
	spamwriter = csv.writer(csvfile,delimiter=',')

	reference_list = edge_pair_list[:]
	#code to remove non-reciprocating edges
	for edge in edge_pair_list:
		#print 'assessing edge',edge
		recip_edge = [edge[1],edge[0]]
		#print 'length of list',len(edge_pair_list)
		if recip_edge in reference_list:
			reciprocating_edge_list.append(edge)
			print len(reciprocating_edge_list)
			spamwriter.writerow(edge)
			reference_list.remove(edge)
			reference_list.remove(recip_edge)


print 'length of original edge list',len(edge_pair_list)
print 'length of final edge list',len(reciprocating_edge_list)

