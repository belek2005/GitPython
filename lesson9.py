import json

data = {
	"dog":{
		"name": "John",
		"color": "Grey",
		"age": None
	}
}

with open("data_file.json", "w") as file:
	json.dump(data, file)
	file.close()

with open("data_file.json", "r") as file:
	data = json.load(file)
	print(data)