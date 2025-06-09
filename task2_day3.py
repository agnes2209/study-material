from datetime import datetime, timedelta

month = int(input("Enter month as 1-12: "))
year = int(input("Enter year: "))

date = datetime(year, month, 1)

if month == 12:
    next_month = datetime(year + 1, 1, 1)
else:
    next_month = datetime(year, month + 1, 1)

print(f"\nCalendar")
print("Mo Tu We Th Fr Sa Su")

print("   " * date.weekday(), end='')  
while date < next_month:
    print(f"{date.day:2}", end=' ')
    if date.weekday() == 6:
        print()
    date += timedelta(days=1)

print()
