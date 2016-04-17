import csv as csv

row_count = 0
list_tuples = list()
timestamp_recipList_dict = dict()
with open('recip_timestamp_dict.txt','rU') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		row_count += 1
		# if row_count > 10:
			# break
		print row_count
		print row
		tuple1 = [int(row[1]),int(row[2])]
		if tuple1 not in list_tuples:
			list_tuples.append(tuple1)

		if row[0] not in timestamp_recipList_dict.keys():
			timestamp_recipList_dict[row[0]] = ["0","0","0","0","0","0","0","0","0"]

		if tuple1 == [1,1]:
			timestamp_recipList_dict[row[0]][0] = str(row[3])
		elif tuple1 == [1,2]:
			timestamp_recipList_dict[row[0]][1] = str(row[3])
		elif tuple1 == [1,3]:
			timestamp_recipList_dict[row[0]][2] = str(row[3])
		elif tuple1 == [2,1]:
			timestamp_recipList_dict[row[0]][3] = str(row[3])
		elif tuple1 == [2,2]:
			timestamp_recipList_dict[row[0]][4] = str(row[3])
		elif tuple1 == [2,3]:
			timestamp_recipList_dict[row[0]][5] = str(row[3])
		elif tuple1 == [3,1]:
			timestamp_recipList_dict[row[0]][6] = str(row[3])
		elif tuple1 == [3,2]:
			timestamp_recipList_dict[row[0]][7] = str(row[3])
		elif tuple1 == [3,3]:
			timestamp_recipList_dict[row[0]][8] = str(row[3])


print timestamp_recipList_dict

row_count = 0
output_file = open("reciprocity_all_timestamp_data.txt", "w+")
for key in timestamp_recipList_dict.keys():
	if row_count == 0:
		header = "timestamp,1-1,1-2,1-3,2-1,2-2,2-3,3-1,3-2,3-3"+"\n"
		output_file.writelines(header)
	row_count += 1
	output_line = (str(key)+(",")+str(timestamp_recipList_dict[key][0])+(",")+str(timestamp_recipList_dict[key][1])+(",")+str(timestamp_recipList_dict[key][2])+(",")+str(timestamp_recipList_dict[key][3])+(",")+str(timestamp_recipList_dict[key][4])+(",")+str(timestamp_recipList_dict[key][5])+(",")+str(timestamp_recipList_dict[key][6])+(",")+str(timestamp_recipList_dict[key][7])+(",")+str(timestamp_recipList_dict[key][8])+("\n"))
	output_file.writelines(output_line)




