file = open('input.txt', 'r').read().replace('move ', '').replace('from ', '').replace('to ', '').splitlines()

crates = []
# Fill crates with input
for x in range(0, 9):
    crates.append([])

for elem in file[:10]:
    for index, x in enumerate(elem):
        if x.isupper():
            crates[int(file[8][index]) - 1] += x

# Reverse crate elements
for index, x in enumerate(crates):
    crates[index] = x[::-1]

# Fill anweisungen
anweisungen = [[],[],[]]
for elem in file[10:]:
    num = ''
    which = 0
    elem += ' '
    for x in elem:
        if x != ' ':
            num += x
        else:
            anweisungen[which].append(int(num))
            which += 1
            num = ''

print(crates)

# Move crates
for index, x in enumerate(anweisungen[0]):
    move = anweisungen[0][index]
    origin = anweisungen[1][index]
    to = anweisungen[2][index]
    payload = []
    for times in range(1, move + 1):
        payload.append(crates[origin -1][-1])
        crates[origin -1] = crates[origin -1][:-1]
    payload.reverse()
    for item in payload:
        crates[to - 1] += item


solution = ''
for x in crates:
    solution += x[-1]
        
print(solution)