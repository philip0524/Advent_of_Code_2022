file = open('input.txt', 'r')
rucksacks = file.read().splitlines()

# ord(kleinbuchstabe - 96)
# ord(Großbuchstabe - 38)
score = 0

for elem in rucksacks:
    firstHalf = elem[:int(len(elem) / 2)]
    secondHalf = elem[int(len(elem) / 2):]
    for x in firstHalf:
        if secondHalf.find(x) != -1:
            sameLetter = secondHalf[secondHalf.find(x)]
            if sameLetter.islower():
                score += ord(sameLetter) - 96
            elif sameLetter.isupper():
                score += ord(sameLetter) - 38
            break
                
 

print(score)