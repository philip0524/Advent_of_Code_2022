# A = Rock
# B = Paper
# C = Scissors

#.replace('X','A').replace('Y','B').replace('Z','C')

file = open('input.txt', 'r')
strategyGuide = file.read().splitlines()

what = 0
score = 0

for x in strategyGuide:
    what = x[-1]
    firstLetter = x[0]
    # Aktion berechnen
    if what == 'Y': # Draw
        lastLetter = firstLetter
        score += 3
    elif what == 'X': # Loose
        match firstLetter:
            case 'A':
                lastLetter = 'C'
            case 'B':
                lastLetter = 'A'
            case 'C':
                lastLetter = 'B'
    elif what == 'Z': # Win
        match firstLetter:
            case 'A':
                lastLetter = 'B'
            case 'B':
                lastLetter = 'C'
            case 'C':
                lastLetter = 'A'
        score += 6
    match lastLetter:
            case 'A':
                score += 1
            case 'B':
                score += 2
            case 'C':
                score += 3

print(score)
