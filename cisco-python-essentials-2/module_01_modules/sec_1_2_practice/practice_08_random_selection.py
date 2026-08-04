import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List       :", my_list)
print("\nchoice     :", random.choice(my_list))
print("sample(5)  :", random.sample(my_list,5))
print("sample(10) :" , random.sample(my_list,10))
