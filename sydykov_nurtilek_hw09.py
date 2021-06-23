import json
import datetime
import time
class JsonHW:
   def __init__(self):
      self.items = {}

   def json_writer(self, json_data, json_filename):
      with open(json_filename + ".json", "w") as my_json:
         json.dump(json_data, my_json)
         my_json.close()
   def json_reader(self, json_filename):
      with open(json_filename + ".json", "r") as my_json:
         return json.load(my_json)
time_now = datetime.datetime.now()
json_work = JsonHW()
print(json_work.items)
my_data = {
   "admin": {
      "id": 1,
      "username": "belek",
      "email": "belek@example.com",
      "reistered_at": f'{time_now}'
   },
   "first_user": {
      "id": 1,
      "username": "user",
      "email": "user@example.com",
      "reistered_at": f'{time_now}'
   },
   "second_user": {
      "id": 1,
      "username": "seconduser",
      "email": "seconduser@example.com",
      "reistered_at": f'{time_now}'
   }
}
json_work.json_writer(my_data, 'homework9')
print(json_work.json_reader('homework9'))