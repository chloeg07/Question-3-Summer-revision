#Question 3
total_rainfall = 0
count_exceeded = 0
rainfall_list = []

for day in range(1, 8):
    rainfall = float(input("Enter recorded rainfallfor day {}: " .format(day)))
    rainfall_list.append(rainfall)
    total_rainfall += rainfall
    if rainfall > 3.5:
        count_exceeded +=1
        print("Day {}: Rainfall exceeded 3.5 cm by {} cm.".format(day, round(rainfall - 3.5, 2)))

average_rainfall = rainfall / 7

print("\nTotal rainfall for the week: {} cm".format(total_rainfall))
print("Average rainfall for the week: {} cm".format(round(average_rainfall, 2)))