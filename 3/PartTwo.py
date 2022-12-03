file = open('input.txt', 'r')
rucksacks = file.read().splitlines()

# ord(kleinbuchstabe - 96)
# ord(Großbuchstabe - 38)
score = 0


for index, elem in enumerate(rucksacks):
    if index % 3 == 0:
        for letter in elem:
            if rucksacks[index + 1].find(letter) != -1 and rucksacks[index + 2].find(letter) != -1:
                if letter.islower():
                    score += ord(letter) - 96
                elif letter.isupper():
                    score += ord(letter) - 38
                break

print(score)