#  LAB  :
# Day of the year

# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

def is_year_leap(year):

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
        return True
    else :
        return False
    

def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12 :
        return None
    month_days = []
    
    if month < 8 :
        stop_condition = month + 1
    else :
        stop_condition = 8
    
    for i in range(1, stop_condition):
        if i % 2 != 0:
            month_days.append(31)
        else :
            if i == 2:
                if is_year_leap(year):
                    month_days.append(29)
                else :
                    month_days.append(28)
            else :
                month_days.append(30)

    if month >= 8 :
        for i in range(8, month + 1):
            if i %  2 != 0 :
                month_days.append(30)
            else :
                month_days.append(31)
    return month_days


def day_of_year(year, month, day):
    result = days_in_month(year, month)
    if result is None:
        return None
    if year < 1 or month < 1 or month > 12 or day < 1 or day > result[month - 1]:
        return None
    
    total_days = day

    for i in range(month - 1):
        total_days += result[i]

    return total_days

print(day_of_year(2000, 12, 31)) # 366
print(day_of_year(2000, 2, 29)) # 60
print(day_of_year(1900, 2, 29)) # None
print(day_of_year(2024, 3, 1)) # 61
print(day_of_year(2026, 3, 1)) # 60
print(day_of_year(2026, 7, 31)) # 212
print(day_of_year(2026, 8, 1)) # 213
print(day_of_year(2026, 8, 31)) # 243
print(day_of_year(2026, 9, 5)) # 248
print(day_of_year(2026, 13, 1)) # None
print(day_of_year(2026, 0, 1)) # None
print(day_of_year(2026, 5, 0)) # None
print(day_of_year(2026, 1, 32)) # None

