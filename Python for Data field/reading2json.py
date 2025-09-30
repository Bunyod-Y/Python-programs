import json 
file_path="/home/bunyodyokubov/PROJECTS/python pandas data science/output.json"
try:
    with open(file_path, "r") as file:
        content=json.load(file)
        print(content)
except FileExistsError:
    print("File is not found")
except PermissionError:
    print("You don't have permission to read that file")