care_hours = [4, 3.5, 4, 2.5, 5]
weekly_allowance = 26

total_hours = sum(care_hours)
hours_remaining = weekly_allowance - total_hours

print("Total hours used:", total_hours)
print("Hours remaining:", hours_remaining)

if total_hours <= weekly_allowance:
    print("Within weekly allowance")
else:
    print("Weekly allowance exceeded")

care_hours_week2 = [4, 5, 4, 4, 5, 3, 4]
total_hours_week2 = sum(care_hours_week2)
hours_remaining_week2 = weekly_allowance - total_hours_week2

print("Week 2")
print("Total hours used:", total_hours_week2)
print("Hours remaining:", hours_remaining_week2)

if total_hours_week2 <= weekly_allowance:
    print("Within weekly allowance")
else:
    print("Weekly allowance exceeded")

