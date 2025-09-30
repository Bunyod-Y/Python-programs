import json

employee= {
            "name": "Spongebob",
            "age": 30,
            "job": "cooker" 
          }
file_path="/home/bunyodyokubov/PROJECTS/python pandas data science/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
except FileNotFoundError:
    print("That file not found")