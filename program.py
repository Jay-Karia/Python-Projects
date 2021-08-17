import os

print("Welcome to Python IO Program Developed -- By Jay")
sel = input("\n1) Custom Directory\n2) Default Directory\n")


# Methods
def list(directory):
    li = os.listdir(directory)
    print("\nItems:\n")
    for items in li:
        print(items)

def read(directory, filename):
    with open(directory + filename) as reading:
        print(f"\nReading from {filename}...\n")
        print(reading.read())
        print("\nReading Finished from a File!")

def writeToAFile(directory, filename):
    with open((directory + filename), "w") as writing:
        print("Enter \'X\' to stop writing...")
        w = ""
        w = input()
        writing.write(w.replace("X", " "))
        while w != "X":
            w = input()
            writing.write(("\n" + w.replace("X", " ")))
        print("\nWriting Finished To a File!")

def appendToAFile(directory, filename):
    # Read from a File
    read(directory, filename)
    # Append to a File
    with open((directory + filename), "a") as appender:
        print("Enter \'X\' to stop writing...")
        a = ""
        while a != "X":
            a = input()
            appender.write(("\n" + a.replace("X", " ")))
        print("Appending Finished To a File!")

def newDir(directory):
    dir = input(f"Enter the name of the folder at:\n {directory}")
    os.mkdir(directory + dir)
    print("Directory Created Successfully!")

def newDirs(directory):
    dir = input(f"Enter the name of the folder at:\n {directory}")
    os.makedirs(directory + dir)
    print("Directory Created Successfully!")

if sel == "1":
    print("\nSelected 1) Custom Directory\n")
    str = "Enter you Directory: "
    dir = input(str)
    cDir = dir + "\\"
    print(f"Directory is set to: " + cDir)
else:
    print("Selected 2) Default Directory\n")
    cDir = os.getcwd() + "\\"
    print(f"Directory is set to: " + cDir)

opt = input(
    "\nEnter what do you want do:\n1) List the items in the Directory\n2) Read a file\n3) Write into a file\n4) Append to a file\n5) Create a new directory\n6) Create new directories\n")

try:
    if opt == "1":
        list(cDir)
    elif opt == "2":
        name = input("Enter file name: ")
        read(cDir, name)
    elif opt == "3":
        name = input("Enter file name: ")
        writeToAFile(cDir, name)
    elif opt == "4":
        name = input("Enter file name: ")
        appendToAFile(cDir, name)
    elif opt == "5":
        newDir(cDir)
    elif opt == "6":
        newDirs(cDir)
except:
    print(f"An Error Occurred! Sorry")