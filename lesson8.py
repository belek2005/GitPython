import csv

def csv_dickt_reader(file_obj, dilimiter =','):
	reader = csv.DicktReader(file_obj, dilimiter=dilimiter)

	for line in reader:
		print(line)
		print()
		print(line["first_name"])
		print(line["last_name"])

with open("data.csv", "r") as file_obj:
	csv_dickt_reader(file_obj)
