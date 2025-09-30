import json
import csv

employees=[
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cooker"],
    ["Patrick", 37, "Une,mployeed"],
    ["Sandy", 27, "Scientist"]]

file_path="/home/bunyodyokubov/PROJECTS/python pandas data science/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
except FileExistsError:
    print("Error")