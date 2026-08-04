from random import randrange, randint

print("Generating random numbers using randrange() with a step size of 2:")
for i in range(5):
    print(f"num {i+1} : {randrange(3, 15, 2)}")

print("\nGenerating random numbers using randint() within an inclusive range:")
for i in range(5):
    print(f"num {i+1} : {randint(10, 18)}")
