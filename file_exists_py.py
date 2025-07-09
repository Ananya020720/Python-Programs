import os

file_path = 'example.txt'

if os.path.exists(file_path):
    print(f"File '{file_path}' exists. Its contents are:\n")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
else:
    print(f"File '{file_path}' does not exist.")
