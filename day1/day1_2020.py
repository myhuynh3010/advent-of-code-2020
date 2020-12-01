# PART 1

data = open('day1_2020.txt','r')
data_line = data.readline().strip()
data_list = data_line.split('\t')
integer_data = []

while data_line:
	# print(data_list)
	for string in data_list:
		number = int(string)
		integer_data.append(number)
	data_line = data.readline().strip()
	data_list = data_line.split('\t')

# print(integer_data)
	
for x in range(0, len(integer_data) -1):
	for y in range(0, len(integer_data) -1):
		if (integer_data[x] + integer_data[y]) == 2020:
			print(integer_data[x] * integer_data[y])


# PART 2

for x in range(0, len(integer_data) -1):
	for y in range(0, len(integer_data) -1):
		for z in range(0, len(integer_data) -1):
			if (integer_data[x] + integer_data[y] + integer_data[z]) == 2020:
				print(integer_data[x] * integer_data[y] * integer_data[z])