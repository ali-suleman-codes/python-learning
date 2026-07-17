# Statement
# A teacher records student marks.
# [78, 55, 91, 66, 83]
# Sort the marks in ascending order using the Bubble Sort algorithm (do not use sort()).

student_marks = [78, 55, 91, 66, 83]
print("Original marks :", student_marks)
swapped = True

while swapped :
    swapped = False
    for i in range(len(student_marks) - 1) :
        if student_marks[i] > student_marks[i + 1]:
            swapped = True
            student_marks[i], student_marks[i + 1] = student_marks[i + 1], student_marks[i]

print("Sorted marks :", student_marks)