import csv as csv
import numpy as np

output_file = open("one_timestamp_data_of8Nov_for_regression.txt","w+")
row_count = 0
with open("MItoMI-2013-11-08.txt",'rb') as csvfile:
	spamreader = csv.reader(csvfile,delimiter="\t")
	for row in spamreader:
		row_count += 1
		print row_count
		#if row_count > 1000000:
			#break
		if row[0] == "1383913200000":
			output_line = (str(row[1])+(",")+str(row[2])+(",")+str(row[3])+"\n")
			output_file.writelines(output_line)	
