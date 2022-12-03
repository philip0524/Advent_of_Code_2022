file = open("input.txt", 'r').read()

elves = file.splitlines()

calories = 0
caloriesPerElve = []

for elve in elves:
    if elve != '':
        calories += int(elve)
    else:
        caloriesPerElve.append(calories)
        calories = 0

caloriesPerElve.sort(reverse = True)


print(caloriesPerElve)
print(sum(caloriesPerElve[0:3]))