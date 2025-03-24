import json

def dict_to_json(dictionary):
    try:
        # Convert Python dictionary to JSON format
        json_data = json.dumps(dictionary)
        return json_data
    except Exception as e:
        print(f"An error occurred while converting to JSON: {e}")
        return None

def json_to_dict(json_data):
    try:
        # Convert JSON back to Python dictionary
        python_object = json.loads(json_data)
        return python_object
    except Exception as e:
        print(f"An error occurred while converting to Python object: {e}")
        return None

# Python dictionary
data = {"name": "Ahmet", "age": 58, "city": "Istanbul"}

# Convert dictionary to JSON
json_data = dict_to_json(data)
if json_data:
    print(f"JSON format: {json_data}")

# Convert JSON back to Python object
python_object = json_to_dict(json_data)
if python_object:
    print(f"Python object: {python_object}")
