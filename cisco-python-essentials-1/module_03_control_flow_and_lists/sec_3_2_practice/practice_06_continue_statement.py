# Goal
# Print numbers 1–20.
# Skip multiples of 3 using continue.

num = 1
while num <= 20 :
    if num % 3 == 0 :
        num += 1
        continue
    else :
        print(num)
        num += 1