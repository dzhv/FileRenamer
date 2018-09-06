import os
from os.path import isfile, join, splitext
import file_accountant

PATH = "/Users/dziugas/Pictures/Keliones/bandom"

files = [join(PATH, item) for item in os.listdir(PATH) 
	if isfile(join(PATH, item)) and not item.startswith('.')]

for file_path in files:
	file_name, extension = splitext(file_path)
	creation_date = file_accountant.get_creation_date(file_path)
	os.rename(file_path, join(PATH, creation_date) + extension)