import calendar

#part1
month = int(input("Enter month as 1-12 : "))
year = int(input("Enter year: "))
print("\nCalendar")
print(calendar.month(year, month))


'''
Enter month as 1-12 : 5
Enter year: 2025

Calendar:
      May 2025
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31  
'''