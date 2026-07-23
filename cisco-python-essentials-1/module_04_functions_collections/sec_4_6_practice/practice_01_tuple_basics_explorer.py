# Tuple Basics Explorer

# Purpose:
# Practice creating and accessing tuples.

# Concepts:
# - Tuple creation
# - Empty tuple
# - One-element tuple
# - Indexing
# - Slicing
# - for loop


dell_storage = ()
apple_storage = (4,)
hp_storage = (32, 64, 128, 256, 512)

print("Dell storage  :", dell_storage)
print("Apple storage :", apple_storage)

print("\n1st storage capacity of hp   :", hp_storage[0])
print("Last storage capacity of hp  :", hp_storage[-1])

print("\nUpper storage capacities of hp :", hp_storage[2 : ])

print("\nAll storag capacities of hp :")
for capacity in hp_storage:
    print(capacity, end = " ")
