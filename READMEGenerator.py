import os
PARENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
# Traverse through all files and directories in the given path
for root, dirs, files in os.walk(PARENT_FOLDER):
    # Extract the relative path of the current folder
    folder_path = os.path.relpath(root, PARENT_FOLDER)
    if folder_path == '.':
        print("Root Directory:")
    else:
        print(f"### {folder_path[:10]} - {folder_path[10:]}")
    
    # List all files in the current folder with their relative paths
    # - [prog1.py](./Week1/prog1.py)
    for file in files:
        file_path = os.path.join(folder_path, file)
        # print(f"  {file} : .\\{file_path}")
        print(f"- [{file}]({file_path})")