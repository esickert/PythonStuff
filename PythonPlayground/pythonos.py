# import OS module
import os
# Get the list of files and directories
os.system('pwd')
os.system('ls')
root_dir = ("//home/esickert")
print("Prints contents of " + root_dir );
print(root_dir);
dir_list = os.listdir(root_dir)
print("Files and directories in '", root_dir, "' :")
# prints all files
print(dir_list)