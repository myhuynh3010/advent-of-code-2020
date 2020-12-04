# PART 1

# data = open('day4.txt', 'r')
# data_line = data.readline().strip()
# fields = []
# while data_line:
# 	data_list  = data_line.split(' ')
# 	for n in range(0, len(data_list)):
# 		fields.append(data_list[n][0:3])
# 	print(data_list)
# 	data_line = data.readline().strip()

# print(fields)

# valid = 0
# expected_fields = 8
# number_of_fields = len(fields)

# if number_of_fields == expected_fields:
# 	valid =+ 1
# elif (number_of_fields == expected_fields - 1) & ('cid' not in fields):
# 	valid =+ 1

# print(valid)
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
# print(sublist)

valid = 0
invalid = 0

for x in range(0, len(sublist)):
	fields = []
	for y in range(0, len(sublist[x])):
		fields.append(sublist[x][y][0:3])
	print(fields)

	expected_fields = 8
	number_of_fields = len(fields)

	if (number_of_fields == expected_fields):
		valid = valid + 1
		print(valid)
	elif (number_of_fields == expected_fields - 1) & ('cid' not in fields):
		valid = valid + 1
		print(valid)
	else:
		invalid = invalid + 1
		print(invalid)

print(len(sublist))

# print(valid)