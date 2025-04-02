"""
    "r" - Read (default mode)
    "w" - Write (creates a new file or overwrites an existing file)
    "a" - Append (adds data to the end of the file)
    "b" - Binary mode (e.g., "rb", "wb" for non-text files like images)
    "x" - Exclusive creation (fails if the file already exists)
    "t" - Reads as text mode
"""

import os

class OpenAndReadAllFileLines:
    def __init__(self):
         # Get the absolute path of the current script
         self.script_dir = os.path.dirname(__file__)
         self.new_file_path = os.path.join(self.script_dir,"FileIOFiles\paragraphFile1.txt")
         self.file_path = os.path.join(self.script_dir, "FileIOFiles\paragraph.txt")  # Construct path

    def readFile(self):
        try:
            with open(self.file_path, "r") as file: #this can also be written as file=open(self.file_path, "r")
                print(file.read())  # reads all lines
                file.close()
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

    def readFileLines(self):
        try:
            with open(self.file_path, "r") as file:
                print(file.readlines())
                file.close() 
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

    def readFileLine(self):
        try:
            with open(self.file_path, "r") as file:
                print(file.readline(10)) # reads the number of characters
                file.close()
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

    def readBinary(self):
        try:
            with open(self.file_path, "rb") as file: # reads the file in binary
                print(file.read()) 
                file.close()
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

    def appendText(self):
        try:
            with open(self.file_path, "a") as file: # append new text
                file.write("Added additional Text")
                file.close()
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

    def createNewFile(self):
        try:
            with open(self.new_file_path, "x") as file: # create new file
                file.write("Added additional Text")
                file.close()
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

    def writeInNewFile(self):
        try:
            with open(self.new_file_path, "w") as file: # over writes
                file.write("This is update text")
                file.close()
        except FileNotFoundError:
            print("Error: The file 'paragraph.txt' was not found.")

fileIO = OpenAndReadAllFileLines()
def switch_case(value):
    match value:
        case 1:
            fileIO.readFile()
        case 2:
            fileIO.readFileLines()
        case 3:
            fileIO.readFileLine()
        case 4:
            fileIO.readBinary()
        case 5:
            fileIO.appendText()
        case 6:
            fileIO.createNewFile()
        case 7:
            fileIO.writeInNewFile()
        case _:
            return "Default Case"
        
getProcessType = int(input("Enter file process type: "))      
switch_case(getProcessType)


