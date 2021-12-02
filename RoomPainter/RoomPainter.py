def totalAreaOfWall():
    total = 0
    numWalls = int(input('How many walls do you have? '))
    for i in range(numWalls):
        base = int(input(f'\nEnter the base of wall {i+1}: '))
        height = int(input(f'Enter the height of wall {i+1}: '))
        areaWall = base*height
        total += areaWall
    return total
def costOfPaint():
    litres = int(input('\nEnter the litres of paint you have: '))
    cost = int(input('What is the price of paint per litre? '))
    costPaint = litres*cost
    return costPaint
def finalCost(totalArea, paintCost):
    final = totalArea*paintCost
    return final

totalArea = totalAreaOfWall()
costPaint = costOfPaint()
print(f'The final cost of everything will be {finalCost(totalArea, costPaint)}.')