#  Statement
# A sensor records temperatures every hour.
# [18, 20, 19, 21, 22, 23, 24, 25]
# Print every second reading using slicing.

temperature_records = [18, 20, 19, 21, 22, 23, 24, 25]

even_records = temperature_records[ : : 2] # list[start : stop : step]

print(even_records)