# Scenario
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.

# Test your code carefully. Hint: using the % operator may be the key to success.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print("\nStarting time = ", hour, ":", mins, sep = "") 

mins += dura  
# Add the duration directly to the initial minutes

hour += (mins//60)  
# Perform integer division by 60 to calculate total elapsed hours, then add them to start hours

hour %= 24  
# Keep hours within a 24-hour format (0 to 23) using modulo 24

mins %= 60 
# Keep minutes within a 60-minute format (0 to 59) using modulo 60

print("\nEnd time = ", hour, ":", mins, sep = "") 


