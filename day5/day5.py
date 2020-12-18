data = open('day5.txt', 'r')
data_line = data.readline().strip()

data_list = []
while data_line:
	data_list.append(data_line)
	data_line = data.readline().strip()

list_id = []
for i in range(0, len(data_list)):
	data = data_list[i]

	row = 0
	column = 0

	def slice_row(letter, array):
		low = array[0]
		up = array[len(array) - 1]
		if letter == 'F':
			range_row = range(low, round((low + up)/2))
			return(range_row)
		elif letter == 'B':
			range_row = range(round((low + up + 1)/2), up + 1)
			return(range_row)
	a = slice_row(data[0], [0, 128])
	b = slice_row(data[1], a)
	c = slice_row(data[2], b)	
	d = slice_row(data[3], c)
	e = slice_row(data[4], d)
	f = slice_row(data[5], e)

	if data[6] == 'F':
		row = f[0]
	elif data[6] == 'B':
		row = f[-1]
	# print('row = ', row)

	def slice_column(letter, array):
		low = array[0]
		up = array[len(array) - 1]
		if letter == 'L':
			range_row = range(low, round((low + up)/2))
			return(range_row)
		elif letter == 'R':
			range_row = range(round((low + up + 1)/2), up + 1)
			return(range_row)
	l = slice_column(data[7], [0, 7])
	m = slice_column(data[8], l)

	if data[9] == 'L':
		column = m[0]
	elif data[9] == 'R':
		column = m[-1]
	# print('column = ', column)

	seat_ID = row * 8 + column
	list_id.append(seat_ID)

# print(list_id)

# print(max(list_id))

list_id.sort()

for i in range(0, len(list_id) - 1):
	if list_id[i] + 1 != list_id[i + 1]:
		print(list_id[i])
		break






