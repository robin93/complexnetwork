def WriteDictToCSV(csv_file,csv_columns,dict_data):
	try:
		with open(csv_file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
			writer.writeheader()
			for data in dict_data:
				writer.writerow(data)
	except IOError as (errno, strerror):
		print("I/O error({0}): {1}".format(errno, strerror))    
	return

csv_columns = ['timestamp','Edge_strength_t']
currentPath = os.getcwd()
csv_file = currentPath + "/csv/Edge_strength.csv"

WriteDictToCSV(csv_file,csv_columns,edge_emergence_dict)