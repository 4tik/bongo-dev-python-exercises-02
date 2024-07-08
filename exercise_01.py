# Exercise 01: The list below is the collection of the ages of people from a
# village. Clean up the data and store only numbers in another list.

data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
numbers_list = []

for data in data_list:
    if(isinstance(data, int)):
        numbers_list.append(data)

print(f"numbers list : {numbers_list}")