# Compare the two dictionaries and find the common items based on KEYs of the dictionaries

dict1 = {
    'age': 13,
    'id': 12,
    'address': 'Banani',
    'course': 'Python'
}

dict2 = {
    'address': 'Rupnagar',
    'id': 25,
    'course': 'MERN'
}

set_of_dict1 = set(dict1)
set_of_dict2 = set(dict2)

common_keys = set_of_dict1 & set_of_dict2
print(f"common keys of dict1 & dict2 : {common_keys}")

