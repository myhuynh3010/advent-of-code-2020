import re

data = open('day6.txt', 'r')
full_data = data.read()
data_list = re.split(' |\n',full_data)
# print(data_list)
sublist = [[]]

for i, num in enumerate(data_list):
	sublist[-1].append(num)
	if num == '' and i != len(data_list)-1:
		sublist.append([])

for n in range(0, len(sublist)):
	for m in range(0, len(sublist[n])):
		if sublist[n][m] == '':
			sublist[n].pop()

print(sublist)

list_string = []
for n in range(0, len(sublist)):
	string = ''
	for m in range(0, len(sublist[n])):
		string = string + sublist[n][m]
	list_string.append(string)

# print(list_string)

total = 0
for x in range(0, len(list_string)):
	list_string[x] = ''.join(set(list_string[x]))
	total = total + len(list_string[x])
# print(total)

def every_yes(group_answer):
	count_yes = 0
	if len(group_answer) == 1:
		count_yes = len(group_answer[0])
		return count_yes
	else:
		for z in range(0, len(group_answer[0])):
			# print(group_answer[0][z])
			true_yes = 0
			for y in range(0, len(group_answer)):
				if ((group_answer[0][z]) in group_answer[y]):
					# print(y)
					# print(group_answer[y], y)
					true_yes = true_yes + 1
			if true_yes == len(group_answer):
				count_yes = count_yes + 1
		return count_yes

sum_of_count = 0
for i in range(0, len(sublist)):
	sum_of_count = sum_of_count + every_yes(sublist[i])
print(sum_of_count)
