import csv as csv

#selected_timestamp_data_03_11_processed.csvoutput_file = open("regression_data3.txt", "w+")

row_count = 0
list_of_nodes = list()
number_of_edges = 0
with open('reciprocating_edge_list.csv','rU') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print row
		row_count += 1
		#if row_count > 10:
		#	break
		#if row[0] == '85':
		number_of_edges += 1
		print number_of_edges
		if row[0] not in list_of_nodes:
			list_of_nodes.append(row[0])
		if row[1] not in list_of_nodes:
			list_of_nodes.append(row[1])

print "Number of nodes", len(list_of_nodes)
print "Number of edges",number_of_edges
