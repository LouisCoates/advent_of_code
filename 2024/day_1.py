with open('/home/coates/python_projects/advent_of_code/2024/data/day1_input.txt', 'r') as file:
    string_data = file.read()

lines = string_data.strip().split('\n')

# Create two empty lists to store the values
list1 = []
list2 = []

# Iterate through the lines and extract the values
for line in lines:
    values = line.strip().split()  # Split each line by whitespace
    list1.append(int(values[0]))  # Convert the first value to an integer and append to list1
    list2.append(int(values[1]))  # Convert the second value to an integer and append to list2

list1.sort()
list2.sort()

distances = []

for i in range(len(list1)):
    distances.append(abs(list1[i] - list2[i]))

print('Task 1: ',sum(distances))

similarity = []

for value in list1:
    similarity.append(list2.count(value) * value)

print('Task 2: ',sum(similarity))