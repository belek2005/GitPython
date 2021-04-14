
import csv

def csv_writer(data, path):
	with open(path, "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=",")
		for line in data:
			writer.writerow(line)

data = [
	"username,email,ip_address".split(","),	
	"root,root@example.com,192.168.0.2".split(","),
	"admin,root@example.com,192.168.0.2".split(","),
	"test_user,root@example.com,192.168.0.2".split(","),
	"second_user,root@example.com,192.168.0.2".split(",")
]

path = "data.csv"

csv_writer(data, path)

def csv_reader(file_obj):
	reader = csv.DictReader(file_obj)

	for line in reader:
		print(line)

with open("data.csv", "r") as file_obj:
	csv_reader(file_obj)