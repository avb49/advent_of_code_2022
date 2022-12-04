# 1. import data
import csv

with open("code advent - day 1 input.csv", newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    data = list(reader)
    data.append([])

# 2. iterate through list -> keep a current_counter and a max variable. When space, compare to max and reset current_counter
max_calories = 0
current_calories = 0

for item in data:
    if item == []:
        
        if current_calories > max_calories:
            max_calories = current_calories
        
        # reset calorie counter
        current_calories = 0
   
    else:
        current_calories += int(item[0])
        pass

# 3. return max calories
print(max_calories)