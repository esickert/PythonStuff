# import OS module
import os
# Get the list of files and directories
os.system('pwd')
os.system('ls')
path = ("//home/esickert")
print("Prints contents of " +  path);
print(path);
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)