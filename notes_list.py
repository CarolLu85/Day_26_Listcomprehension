numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)


# list comprehension
# new_list = [new_item for item in list]

# to achieve the same goal as from line 1 - 5 using list comprehension

new_list = [n+1 for n in numbers]

name = "Angela"

name_new_list = [letter for letter in name]

range(1, 5)

range_list = [number*2 for number in range]

# conditional list comprehension

new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

names_list = [name for name in names if len(name) < 5]

name_list_upper = [name.upper() for name in names if len(name) >= 5]