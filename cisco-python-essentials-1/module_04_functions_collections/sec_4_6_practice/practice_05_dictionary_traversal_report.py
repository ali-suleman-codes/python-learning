# Dictionary Traversal Report
# Purpose:

# Practice traversing dictionaries using different dictionary methods.

# Concepts:
# keys()
# values()
# items()
# sorted()
# for loop

book_store = {
    "Python" : 1500,
    "C++ DSA": 2000,
    "Web development" : 1000
    }

print("BOOK TILES :")
for key in book_store.keys():
    print(key)

print("\nBOOK PRICES :")
for value in book_store.values():
    print(value)

print("\nORIGINAL DICTIONARY :")
for key, value in book_store.items():
    print(f"{key : <20} : {value}")


print("\nSORTED DICTIONARY :")
for key, value in sorted(book_store.items()):
    print(f"{key : <20} : {value}")
    