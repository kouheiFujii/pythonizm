def modify_list(list):
    list.append(100)

my_list = [1, 2, 3, 4, 5]
modify_list(my_list)

print(my_list) # [1, 2, 3, 4, 5, 100]

def modify_reference(lst):
    lst = [0, 1, 2]

my_list = [0]
modify_reference(my_list)
print(my_list) # [0]
