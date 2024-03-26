#import OS module
import os
#import webdriver
# Get the list of files and directories
os.system('pwd')
#os.system('ls')
root_dir = ("//home/esickert")
print("Prints contents of " + root_dir );
print(root_dir);
dir_list = os.listdir(root_dir)
print("Files and directories in '", root_dir, "' :")
# prints all files
print(dir_list)

print("******************************************")
#from selenium import webdriver
#?????????
print("HELP HELP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("this tries to use selenium but does not work!!!!!!")
import webdriver
driver_path = "//SeleniumDrivers//"
driver_path = "path/to/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
#*********************************************************

#from selenium import webdriver
driver_path = "path/to/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("Python")
search_box.submit()