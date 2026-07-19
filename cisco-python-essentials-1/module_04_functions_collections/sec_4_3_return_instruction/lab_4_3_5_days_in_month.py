#  LAB :
# How many days: writing and using your own functions

# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).

def is_year_leap(year):

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
        return True
    else :
        return False


def days_in_month(year, month):

    # month_days = []
    # for i in range(1, 8):
    #     if i % 2 != 0:
    #         month_days.append(31)
    #     else :
    #         if i == 2:
    #             if is_year_leap(year):
    #                 month_days.append(29)
    #             else :
    #                 month_days.append(28)
    #         else :
    #             month_days.append(30)
    # for i in range(8, 13):
    #     if i %  2 != 0 :
    #         month_days.append(30)
    #     else :
    #         month_days.append(31)
    # print(month_days)
    # return month_days[month - 1]

    if year < 1 or month < 1 or month > 12 :
        return None
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    
    return month_days[month - 1]
    


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")