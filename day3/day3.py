data = open('day3.txt', 'r')
grid_row = data.readline().strip()

grid = []

while grid_row:
	grid.append(grid_row)
	grid_row = data.readline().strip()

number_of_tree = 0
for i in range(0, len(grid)):

	x = (i * 3) % len(grid[i])
	print(x)
	if grid[i][x] == '#':
		print(i, x)
		number_of_tree += 1
print(number_of_tree)



