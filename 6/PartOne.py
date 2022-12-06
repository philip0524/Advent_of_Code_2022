data = open('input.txt', 'r').read()

for index, x in enumerate(data):
    if index >= 3:
        zero = data[index-3]
        one = data[index - 2]
        two = data[index - 1]
        three = data[index]
        
        arr = [zero, one, two, three]
        if arr.count(zero) != 1:
            continue
        elif arr.count(one) != 1:
            continue
        elif arr.count(two) != 1:
            continue
        elif arr.count(three) != 1:
            continue
        else: 
            print(index + 1)
            break  
