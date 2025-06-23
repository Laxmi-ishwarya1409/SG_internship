# Serialization means converting a Python object (like dict, list) into a format (like JSON) so it can be saved to a file or sent over a network.

# Deserialization is converting that data back into a Python object.







# Example of json.dumps() – string output
import json

data = {"name": "Aishwarya", "age": 25}

# Convert to JSON string
json_string = json.dumps(data)

print(json_string)



# Example of json.dump() – write to file
import json

data = {"name": "Aishwarya", "age": 25}

# Write JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file)




# Example of json.loads() – string input

import json

json_string = '{"name": "Aishwarya", "age": 25}'

# Convert JSON string to Python object
data = json.loads(json_string)

print(data)



# Example of json.load() – read from file

import json

# Read JSON from a file
with open("data.json", "r") as file:
    data = json.load(file)

print(data)











import json

# Data (a Python dictionary)
data = {"name": "Laxmi", "age": 22, "email": "laxmi@example.com"}

# ➤ Serialization: Python → JSON (string)
with open("data.json", "w") as f:
    json.dump(data, f)  # dump = save to file

# ➤ Deserialization: JSON → Python
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded Data:", loaded_data)




# JSON with a List

import json

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

json_string = json.dumps(data,indent=4)
print(json_string)


python_data = json.loads(json_string)
print(python_data)




# JSON with Nested Dictionary
import json

person = {
    "name": "Charlie",
    "age": 28,
    "address": {
        "city": "Hyderabad",
        "zip": "500001"
    },
    "hobbies": ["reading", "traveling"]
}

json_person = json.dumps(person, indent=4)
print(json_person)


parsed_person = json.loads(json_person)
print(parsed_person)
