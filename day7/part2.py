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

def must_contain(bag):
	must_contain_count = 0
	# print(bag, D[bag]) #D[bag]: find the first layer inside the bag (shiny bag)
	for key in D[bag].keys(): # loop through the key to have number of bags inside for every bag
		must_contain_count = must_contain_count + D[bag][key] #must_content_count increase by the number of bags inside
		# print('must_content(key): ', must_contain(key))
#		print(key, D[bag][key])
		if must_contain(key) > 0:
			must_contain_count = must_contain_count + D[bag][key] * must_contain(key)
	return must_contain_count
		



number_of_bags = must_contain('shiny gold')

print(number_of_bags)