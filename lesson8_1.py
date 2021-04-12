import csv

def csv_writer(data, path):
	with open(path, "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=",")
		for line in data:
			writer.writerow(line)

data = [
	"first_name, last_name".split(","),	
	"Ivan, Ivanov".split(","),
	"Petr,Petrov".split(","),
	"Klara,Korallova".split(",")
]

path = "output.csv"

csv_writer(data, path)