# PART 1

import re

data = open('day4.txt', 'r')
full_data = data.read()
data_list = re.split(' |\n',full_data)
# print(data_list)
sublist = [[]]

for i, num in enumerate(data_list):
	sublist[-1].append(num)
	if num == '' and i != len(data_list)-1:
		sublist.append([])
# print(sublist)

for n in range(0, len(sublist)):
	for m in range(0, len(sublist[n])):
		if sublist[n][m] == '':
			sublist[n].pop()

list_dictionary = []

for x in range(0, len(sublist)):
	passport = {}
	# print('sublist[x] = ', sublist[x])
	for y in range(0, len(sublist[x])):
		keys = sublist[x][y][0:3]
		values = sublist[x][y][4:len(sublist[x][y])]
		passport[keys] = values
	list_dictionary.append(passport)

def valid_cid(fields_list):
	if len(fields_list) == 8:
		return True
	if len(fields_list) == 7:
		keys =  fields_list.keys()
		if 'cid' not in keys:
			return True
def valid_byr(fields_list):
	for key in fields_list.keys():
		if (key == 'byr'):
			value = int(list_dictionary[n][key])
			if (1920 <= value <= 2002):
				# print('valid_byr =', fields_list)
				return True

				

def valid_iyr(fields_list):
	for key in fields_list.keys():
		if (key == 'iyr'):
			value = int(list_dictionary[n][key])
			if (2010 <= value <= 2020):
				return True

def valid_eyr(fields_list):
	for key in fields_list.keys():
		if (key == 'eyr'):
			value = int(list_dictionary[n][key])
			if (2020 <= value <= 2030):
				return True

def valid_hgt(fields_list):
	for key in fields_list.keys():
		if (key == 'hgt'):
			value = list_dictionary[n][key]
			if (value.endswith('cm') == True):
				cm_value = int(value[:-2])
				if (150 <= cm_value <= 193):
					return True
			if (value.endswith('in') == True):
				in_value = int(value[:-2])
				if (59 <= in_value <= 76):
					return True

def valid_hcl(fields_list):
	range_number = ['0','1','2','3','4','5','6','7','8','9']
	range_letter = ['a', 'b', 'c', 'd', 'e', 'f']
	time_of_true = 0
	for key in fields_list.keys():
		if (key == 'hcl'):
			value = list_dictionary[n][key]
			if (len(value) == 7) & (value.startswith('#')):
				for i in range(1, len(value)):
					if (value[i] in range_letter) | (value[i] in range_number):
						time_of_true = time_of_true + 1
	if time_of_true == 6:
		return True

def valid_ecl(fields_list):
	color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	for key in fields_list.keys():
		value = list_dictionary[n][key]
		if value in color:
			return True

def valid_pid(fields_list):
	number = ['0','1','2','3','4','5','6','7','8','9']
	time_of_true = 0
	for key in fields_list.keys():
		value = list_dictionary[n][key]
		if (len(value) == 9):
			for i in range(0, len(value)):
				if value[i] in number:
					time_of_true = time_of_true + 1
	if time_of_true == 9:
		return True

valid = 0
		
for n in range(0, len(list_dictionary)):
	# print('list_dictionary[n] = ', list_dictionary[n])
	a = valid_cid(list_dictionary[n])
	# print('a =', a)
	b = valid_byr(list_dictionary[n])
	# print('b =', b)
	c = valid_iyr(list_dictionary[n])
	# print('c =', c)
	d = valid_eyr(list_dictionary[n])
	# print('d =', d)
	e = valid_hgt(list_dictionary[n])
	# print('e =', e)
	f = valid_hcl(list_dictionary[n])
	# print('f =', f)
	g = valid_ecl(list_dictionary[n])
	# print('g =', g)
	h = valid_pid(list_dictionary[n])
	# print('h =', h)

	if ((a == True) & (b == True) & (c == True) & (d == True) & (e == True) & (f == True) & (g == True) & (h == True)):
		valid = valid + 1

print(valid)


