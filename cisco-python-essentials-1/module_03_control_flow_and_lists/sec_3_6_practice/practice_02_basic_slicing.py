#  Statement
# A library stores book IDs.
# [11, 12, 13, 14, 15, 16, 17]
# Print
# first three books
# middle three books
# last two books

book_ids = [11, 12, 13, 14, 15, 16, 17]

first_three_book_ids = book_ids[: 3]
middle_three_book_ids = book_ids[2 : 5]
last_two_book_ids = book_ids[5 :]

print("First  :", first_three_book_ids)
print("Middle :", middle_three_book_ids)
print("Last   :", last_two_book_ids)