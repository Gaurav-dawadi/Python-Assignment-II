"""Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python."""

import json

my_info = {
  "name": "Gaurab",
  "age": 23  
}

toJSON = json.dumps(my_info)
print("------------------------")
print("In JSON Format:")
print(toJSON)
print("------------------------")

backToPython = json.loads(toJSON)
print("In Python:")
print("Name:", backToPython['name'])
print("Age:", backToPython['age'])
print("------------------------")
