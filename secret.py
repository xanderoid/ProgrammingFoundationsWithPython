import os
# define function to rename files
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r'/Users/devbyxan/Documents/dev resources/python/udacityProgramingFoundations/secret')
	
	#(2) for each file, rename filename
	os.chdir(r'/Users/devbyxan/Documents/dev resources/python/udacityProgramingFoundations/secret')
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, '0123456789'))
		#translate method removes the characters in the 2nd arg
rename_files()