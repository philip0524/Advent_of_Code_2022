assignments = open('input.txt', 'r').read().replace(',', ' ').split()

score = 0

def getRange(element):
    indexHyphen = element.find('-')
    firstNumber = int(element[:indexHyphen])
    lastNumber = int(element[indexHyphen + 1:])
    elementRange = []
    for x in range(firstNumber, lastNumber + 1):
        elementRange.append(str(x))
    return elementRange

for index, value in enumerate(assignments):
    if index % 2 == 0:
        firstRange = getRange(value)
        secondRange = getRange(assignments[index + 1])

        for x in firstRange:
            if x in secondRange:
                score += 1
                break

    

print(score)