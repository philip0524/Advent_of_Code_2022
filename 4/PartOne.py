assignments = open('input.txt', 'r').read().replace(',', ' ').split()

score = 0

def getRange(element):
    indexHyphen = element.find('-')
    firstNumber = int(element[:indexHyphen])
    lastNumber = int(element[indexHyphen + 1:])
    elementRange = {firstNumber}
    for x in range(firstNumber + 1, lastNumber + 1):
        elementRange.add(x)
    return elementRange

for index, value in enumerate(assignments):
    if index % 2 == 0:
        firstRange = getRange(value)
        secondRange = getRange(assignments[index+1])
        if firstRange.issubset(secondRange) or secondRange.issubset(firstRange):
            score += 1

print(score)