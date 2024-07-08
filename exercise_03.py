# Find the common items between the lists and make SUM of
# the new list items which are common between the lists.

list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

common_list = list(set(list1) & set(list2))
print(f"common list : {common_list}")
print(f"common list sum  : {sum(common_list)}")