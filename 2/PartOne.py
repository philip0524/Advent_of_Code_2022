# A = Rock
# B = Paper
# C = Scissors

file = open('input.txt', 'r')
strategyGuide = file.read().replace('X','A').replace('Y','B').replace('Z','C').splitlines()

score = 0
for x in strategyGuide:
    match x[-1]:
        case 'A':
            score += 1
        case 'B':
            score += 2
        case 'C':
            score += 3

    if x[0] == x[-1]:
        score += 3
    else:
        match x:
            case 'A B':
                score += 6
            case 'B C':
                score += 6
            case 'C A':
                score += 6

print(score)