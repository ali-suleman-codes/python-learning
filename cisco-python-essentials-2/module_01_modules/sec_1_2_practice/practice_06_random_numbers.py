import random

print("Generating random numbers using Pseudorandom Number Generator (PRNG)")
print("--- Default Seed ---")
for i in range(5):
    print(f"num {i+1} : {random.random()}")

print("\n--- Fixed Seed (6) ---")
random.seed(6)

for i in range(5):
    print(f"num {i+1} : {random.random()}")

