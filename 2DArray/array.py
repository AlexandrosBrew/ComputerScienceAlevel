array = []

for i in range(10):
    tempArray = []
    for x in range(10):
        tempArray.append(i+x)
    array.append(tempArray)

for r in range(len(array)):
    for c in range(len(tempArray)):
        print(f'The row number is: {r}, the colomn number is: {c}, and the value is: {array[r][c]}')
