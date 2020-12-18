import re

data = open('day7.txt', 'r')
data_line = data.readline().strip()
D = {}

while data_line:
	rule_in_words = data_line.split(' bags contain ')
	small_d = {}
	# print(rule_in_words[1])
	if rule_in_words[1] != 'no other bags.':
		# print(rule_in_words)
		second_value = re.split(' bag, | bags, | bag.| bags.', rule_in_words[1])
		# print(second_value)

		for i in range(0, len(second_value) - 1):
			# print(second_value[i])
			new_value = second_value[i].split(' ')
			# print('len new_value:', len(new_value))
			# print(new_value)

			
			small_d[(new_value[1]) + ' ' + (new_value[2])] = int(new_value[0])
			# print(small_d)

	D[rule_in_words[0]] = small_d
	data_line = data.readline().strip()

# print(D)

def can_contain(bag, value_of_outerbag):
	if bag in value_of_outerbag:
		return True
	
	for value in value_of_outerbag:
		# print(value, D[value])
		if can_contain(bag, D[value].keys()):
			return True

	return False

number_of_contain = 0
for value in D.values():
	# print(value.keys())
	if can_contain('shiny gold', value.keys()) == True:
		number_of_contain = number_of_contain + 1
print(number_of_contain)

