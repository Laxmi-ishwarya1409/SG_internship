# Get Current Working Directory

import os

print("Current directory:", os.getcwd())




# List All Files in a Folder
import os

print("Files in current directory:")
for file in os.listdir():
    print(file)



# Create and Remove a Folder

import os

# Create a folder
os.mkdir("test_folder")
print("Folder created.")

# Remove the folder
os.rmdir("test_folder")
print("Folder removed.")



# Create Nested Folders

import os

os.makedirs("level1/level2/level3")
print("Nested folders created.")




# Delete a File
import os

# Create a dummy file first
with open("sample.txt", "w") as f:
    f.write("Hello!")

# Now remove it
os.remove("sample.txt")
print("File deleted.")