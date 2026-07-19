# Library Book Registration

# Purpose:
# Understand default parameter values.

# Concepts:
# - Default parameters
# - Keyword arguments
# - Function parameters

def book_info(title, author, status = "Available"):
    print("Title : " + title + " | Author : " + author + " | Status : " + status)

book_info("Python Basics", "Ali")
book_info("Data Science", "Ahmed", "Checked Out")