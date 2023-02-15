import os
import sys

# check if the argument is provided
# if len(sys.argv) != 2:
#     print("Usage: python script.py <directory_path>")
#     sys.exit(1)

# get the directory path from the command line argument
directory_path = sys.argv[1]

# check if the directory path exists
if not os.path.exists(directory_path):
    print(f"The directory path {directory_path} does not exist")
    sys.exit(1)

# check if the directory path is a directory
if not os.path.isdir(directory_path):
    print(f"{directory_path} is not a directory")
    sys.exit(1)

# print the name of all files in the directory
for file_name in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, file_name)):
        print(file_name)

