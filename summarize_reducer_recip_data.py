import csv
#stop_index = 0
tuple_dict = dict()
with open('reducer_output_merged.txt','rb') as textfile:
		spamreader = csv.reader(textfile, delimiter='\t', quotechar='|')
		for row in spamreader:
			#stop_index += 1
			#if stop_index > 10:
				#break
			if row[0] not in tuple_dict.keys():
				tuple_dict[row[0]]= 1
			else:
				tuple_dict[row[0]] += 1
			print row[0]
with open("8Nov_all_timestamp_recip_processed_fulldata.txt",'w') as text_file:
	for keys in tuple_dict.keys():
		text_file.write("%s\n"%[keys,tuple_dict[keys]])
text_file.close()

