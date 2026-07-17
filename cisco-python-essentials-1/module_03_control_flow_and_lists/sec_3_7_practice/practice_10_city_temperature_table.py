# City Temperature Table

# Purpose:
# Store daily temperatures for three cities.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A region has 3 cities and each has 4 temperatures

city_temperatures = [
    [31, 32, 33, 34],
    [29, 30, 31, 32],
    [27, 28, 29, 30]
]

print("City B temperatures  :", city_temperatures[1])
print("City A temperature 3 :", city_temperatures[0][2])
print("City C temperature 4 :", city_temperatures[2][3])