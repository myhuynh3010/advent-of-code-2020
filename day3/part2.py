data = open('day3.txt', 'r')
grid_row = data.readline().strip()

grid = []

while grid_row:
	grid.append(grid_row)
	grid_row = data.readline().strip()

number_of_tree_1 = 0
for i in range(0, len(grid)):

	x = (i * 1) % len(grid[i])
	# print(x)
	if grid[i][x] == '#':
		# print(i, x)
		number_of_tree_1 += 1
print(number_of_tree_1)

number_of_tree_3 = 0
for i in range(0, len(grid)):

	x = (i * 3) % len(grid[i])
	# print(x)
	if grid[i][x] == '#':
		# print(i, x)
		number_of_tree_3 += 1
print(number_of_tree_3)

number_of_tree_5 = 0
for i in range(0, len(grid)):

	x = (i * 5) % len(grid[i])
	# print(x)
	if grid[i][x] == '#':
		# print(i, x)
		number_of_tree_5 += 1
print(number_of_tree_5)

number_of_tree_7 = 0
for i in range(0, len(grid)):

	x = (i * 7) % len(grid[i])
	# print(x)
	if grid[i][x] == '#':
		# print(i, x)
		number_of_tree_7 += 1
print(number_of_tree_7)

number_of_tree_2 = 0
for i in range(0, len(grid), 2):

	x = (round(i / 2)) % len(grid[i])
	# print(x)
	if grid[i][x] == '#':
		# print(i, x)
		number_of_tree_2 += 1
print(number_of_tree_2)

print(number_of_tree_1 * number_of_tree_2 * number_of_tree_3 * number_of_tree_5 * number_of_tree_7)