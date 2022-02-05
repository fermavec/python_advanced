#Union
my_set_1 = {1, 2, 3}
my_set_2 = {3, 4, 5}

my_union = my_set_1 | my_set_2
print(my_union)

#Intersection
my_set_3 = {1, 2, 3}
my_set_4 = {3, 4, 5}

my_intersection = my_set_3 & my_set_4
print(my_intersection)

#Diference
my_diference_1 = my_set_1 - my_set_2
my_diference_2 = my_set_4 - my_set_3
print(my_diference_1)
print(my_diference_2)

#Simetric Diference
my_simetric = my_set_4 ^ my_set_3
print(my_simetric)

def elimination(some_list):
    no_duplicates = []
    for element in some_list:
        if element not in no_duplicates:
            no_duplicates.append(element)
    return no_duplicates

print(elimination([1, 1, 2, 2, 5]))

print(set([1, 1, 2, 2, 5]))