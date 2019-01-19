#!python3
#number_sorter.py takes a list of numbers and sorts them in ascending order

import pyperclip

num_list = []

def create_list():
	input_list = pyperclip.paste().split()
	input_list.sort(key=float)
	return input_list


def copy_back(num_list):
	pyperclip.copy('\n'.join(num_list))

## 4 3 2 6 7 9 4 10 ctrl+c numbers :D
if __name__ == "__main__":
	num_list = create_list()
	copy_back(num_list)
	print(pyperclip.paste())