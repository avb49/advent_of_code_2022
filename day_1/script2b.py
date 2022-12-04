# NEATER Solution



# 1. import data
import csv
import time

with open("code advent - day 1 input.csv", newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    data = list(reader)
    data.append([])

start_time = time.time()

# 2. iterate through list -> keep a current_counter and a max variable. When space, compare to max and reset current_counter
max_calories_top1 = 0
max_calories_top2 = 0
max_calories_top3 = 0

current_calories = 0

totals = []
for item in data:
    if item == []:     
        totals.append(current_calories)
        # reset calorie counter
        current_calories = 0
    else:
        current_calories += int(item[0])
        pass

# 3. return max calories
sorted_totals = sorted(totals)
print(sorted_totals[-1] + sorted_totals[-2] + sorted_totals[-3])
print("--- %s seconds ---" % (time.time() - start_time))