import csv
file_path="/home/bunyodyokubov/PROJECTS/python pandas data science/output.csv"

try:
    with open(file_path, "r") as file:
        content=csv.reader(file)
        for line in content:
            print(line)
except FileExistsError:
    print("File is not found")