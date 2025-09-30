

employees=["Eugene", "Squidward", "Spongebob", "Patrick"]
file_path="/home/bunyodyokubov/PROJECTS/python pandas data science/output.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
except FileNotFoundError:
    print("That file already exist!")