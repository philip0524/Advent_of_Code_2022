data = open('input.txt', 'r').read()

for index, x in enumerate(data):
    if index >= 14:
        arr = []
        for elem in data[index - 14:index]:
            arr.append(elem)
        counts = []
        for each in arr:
            counts.append(arr.count(each))
        
        if counts.count(counts[0]) == len(counts):
            print(len(counts))
            print(index)
            break
