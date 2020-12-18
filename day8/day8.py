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
			break
		visited[i] = True
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
		# print('new i =', i)
	return accumulator

print(move(day8_data))