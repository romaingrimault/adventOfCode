import coreAdventOfCode as c

data = c.get_input(3)

lines = data.split('\n')
lines.pop()
def generateArr(Lines):
    rowsNumber = len(Lines)
    colsNumber = len(Lines[0])
    array = [[0] * colsNumber for _ in range(rowsNumber)]
    row = 0
    for line in Lines:
        col = 0
        for char in line:
            array[row][col] = char
            col += 1
        row += 1
    return array

def printArr(tab):
    for line in tab:
        print(line)

def parseArray(tab):
    numbers = {}
    row = 0
    for line in tab:
        col = 0
        number = ''
        startX = 0
        try:
            for char in line:
                if char.isdigit():
                    if(number == ''):
                        startX= col
                    number += char
                elif number != '':
                    numbers.update({len(numbers):{'number':number,'line':row,'start':startX,'end':col}})
                    number = ''
                    startX = 0
                col += 1
        except:
            print(f"error at row {row} and col {col}")
        row += 1
    return numbers

def isSymbolNear(tab,x,y,maxX):
    
    dic=['*','&','+','-','#','@','$','/','%','=']
    # ligne du haut
    # if y>5:
    #     return False
    # else:
    #     print(f"deal with: { tab[y][x]}")

    if x - 1 > 0 and y - 1 > 0 and tab[y - 1][x - 1] in dic:
        # print(f'find: {tab[y - 1][x - 1]} at x: {x - 1} and y: {y - 1}')
        return True
    elif y - 1 > 0 and tab[y - 1][x] in dic:
        # print(f'find: {tab[y - 1][x]} at x: {x} and y: {y - 1}')
        return True
    elif x + 1 < 140 and y - 1 > 0 and tab[y - 1][x + 1] in dic:
        # print(f'find: {tab[y - 1][x + 1]} at x: {x + 1} and y: {y - 1}')
        return True
    # ligne du milieu
    elif x - 1 > 0 and tab[y][x - 1] in dic:
        # print(f'find: {tab[y][x - 1]} at x: {x - 1} and y: {y}')
        return True
    elif x + 1 < 140 and tab[y][x + 1] in dic:
        # print(f'find: {tab[y][x + 1]} at x: {x + 1} and y: {y}')
        return True
    # ligne du bas
    elif x - 1 > 0 and y + 1 < len(tab[0]) and tab[y + 1][x - 1] in dic:
        # print(f'find: {tab[y + 1][x - 1]} at x: {x - 1} and y: {y + 1}')
        return True
    elif y + 1 < len(tab[0]) and tab[y + 1][x] in dic:
        # print(f'find: {tab[y + 1][x]} at x: {x} and y: {y + 1}')
        return True
    elif x + 1 < 140 and y + 1 < len(tab[0]) and tab[y + 1][x + 1] in dic:
        # print(f'find: {tab[y + 1][x + 1]} at x: {x + 1} and y: {y + 1}')
        return True
    elif x+1 < maxX:
        return isSymbolNear(tab,x+1,y,maxX)
    else:
        return False
arr = generateArr(lines)


numberDictionary = parseArray(arr)

result = 0
for elem in numberDictionary:
    if isSymbolNear(arr,numberDictionary[elem]['start'],numberDictionary[elem]['line'],numberDictionary[elem]['end']):
        print(numberDictionary[elem])
        result += int(numberDictionary[elem]['number'])
print(result)
# c.submit(3,1,result)



# [x - 1][y - 1] | [x][y - 1] | [x + 1][y - 1] 
# [x - 1][y]     | [x][y]   | [x + 1][y] 
# [x - 1][y + 1] | [x][y + 1] | [x + 1][y + 1] 