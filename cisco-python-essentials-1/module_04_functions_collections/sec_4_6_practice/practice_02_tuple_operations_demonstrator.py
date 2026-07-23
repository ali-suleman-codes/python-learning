# Tuple Operations Demonstrator
# Purpose:

# Practice common operations that can be performed on tuples.

# Concepts:
# len()
# Tuple concatenation (+)
# Tuple repetition (*)
# in
# not in
# Tuple assignment (swapping)

pta_approved_phones = ("Vivo", "Google", "Infinix", "Redmi")
non_pta_approved_phones = ("Iphone", "Samsung")

available_phones = pta_approved_phones + non_pta_approved_phones

available_phones *= 3

print("Total number of phones :", len(available_phones))

if "Vivo" in available_phones:
    print("Vivo phone available")
if "Nokia" not in available_phones:
    print("Nokia phone not available")

pta_approved_phones, non_pta_approved_phones = non_pta_approved_phones, pta_approved_phones

print(pta_approved_phones)
print(non_pta_approved_phones)