import json, datetime

current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
data = [
	{"id": 1, "username": "admin", "email": "admin@example.com", "registered_ad": current_datetime},
	{"id": 2, "username": "first", "email": "first@example.com", "registered_ad": current_datetime},
	{"id": 3, "username": "second", "email": "second@example.com", "registered_ad": current_datetime}

]

with open("data.json", "w") as file:
	json.dump(data, file)
	file.close()

with open("data.json", "r") as file:
	loaded_data = json.load(file)
	print(loaded_data)
	file.close()