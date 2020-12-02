# PART 1

import re

data = open('day2.txt', 'r')
data_line = data.readline().strip()

# correct_passwords = 0

# while data_line:
# 	data_list = re.split(': |-| ', data_line)
# 	if data_list[2] in data_list[3]:
# 		count_letters = 0
# 		for x in range(0, len(data_list[3])):
# 			if data_list[3][x] == data_list[2]:
# 				count_letters += 1
# 		if count_letters in range(int(data_list[0]), int(data_list[1]) + 1):
# 			correct_passwords += 1		
# 	data_line = data.readline().strip()

# print(correct_passwords)

# PART 2
correct1 = 0
correct2 = 0
while data_line:
	data_list = re.split(': |-| ', data_line)
	
	firstPositionContains = data_list[3][int(data_list[0]) - 1] == data_list[2]
	secondPositionContains = data_list[3][int(data_list[1]) - 1] == data_list[2]

	if firstPositionContains ^ secondPositionContains:
		correct1 += 1
	data_line = data.readline().strip()

print(correct1 - correct2)