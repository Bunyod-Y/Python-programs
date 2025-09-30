# Python reading files (.txt, .json, .csv)

file_path = "/home/bunyodyokubov/PROJECTS/python pandas data science/output.csv"

try:
    with open(file_path, "r") as file:
            content=file.read()
            print(content)
except FileNotFoundError:
      print("That file is not found")
except PermissionError:
      print("You don't have permission")