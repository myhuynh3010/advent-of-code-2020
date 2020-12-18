import time

data = open('day8.txt', 'r')
data_line = data.readline().strip()

day8_data = []

while data_line:
	data_list = data_line.split()
	data_list[1] = int(data_list[1])
	day8_data.append(data_list)
	data_line = data.readline().strip()

# print(day8_data)

def move(step):
	accumulator = 0
	visited = {}
	i = 0
	while True:
		if i in visited.keys():
			return None
		if i < 0 or i >= len(step):
			return accumulator
		visited[i] = True
		# print(i)
		# print('i =', i)
		if step[i][0] == 'acc':
			accumulator = accumulator + step[i][1]
			# print('acc')
			# print('accumulator1 = ', accumulator)
			i += 1
		elif step[i][0] == 'jmp':
			# print('jmp')
			# print('accumulator2 = ', accumulator)
			i += step[i][1]
		elif step[i][0] == 'nop':
			# print('nop')
			# print('accumulator3 = ', accumulator)
			i += 1


# print(day8_data)

for i in range(0, len(day8_data)):
	new_day8 = list(day8_data)

	if day8_data[i][0] == 'jmp':
		new_day8[i] = ['nop', day8_data[i][1]]
		print(new_day8)

	if day8_data[i][0] == 'nop':
		new_day8[i] = ['jmp', day8_data[i][1]]
		print(new_day8)

	result = move(new_day8)
	if result == None:
		print('not', i)
	else:
		print(result)
		break



		# if move(new_day8) != None:
		# 	print(move(new_day8))
		# else:
		# 	print('not nop')
	# if day8_data[i][0] == 'jmp':
	# 	new_day8 = day8_data
	# 	new_day8[i][0] = 'nop'
	# 	if move(new_day8) != None:
	# 		print(move(new_day8))

# print(move(day8_data))