# School Timetable

# Purpose:
# Store weekly subjects in a timetable and retrieve
# complete days and individual subjects.

# Concepts:
# - Nested lists
# - Row indexing
# - Column indexing

# A school has timetable of 3 days of 3 subjects

timetable = [
    ["Math", "English", "Physics"],
    ["Chemistry", "Biology", "Computer"],
    ["Urdu", "Islamiat", "History"]
]

print("Monday  :", timetable[0])
print("Tuesday :", timetable[1])

print("Wednesday subject 2 :", timetable[2][1])
print("Monday subject 3    :", timetable[0][2])