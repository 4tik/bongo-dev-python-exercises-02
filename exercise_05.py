# Sort the list in DESCENDING order and find the subtraction of maximum and minimum numbers.

list_1 = [4, 9, 8, 7, 5, 2, 13]
list_1.sort(reverse = True)

print(f"DESCENDING sorting : {list_1}")

max_value = list_1[0]
min_value = list_1[len(list_1)-1]
print(f"subtraction of maximum({max_value}) and minimum({min_value}) : {(max_value-min_value)}")