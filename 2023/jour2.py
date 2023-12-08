import coreAdventOfCode as c

inpute = c.get_input(2)
# Part 1
# lines = inpute.split('\n')
# result = 0
# for line in lines:
#     if(len(line.split(':')) > 1): 
#         values = line.split(':')
#         grabs = values[1].split(';')
#         possibleGame = True
#         for grab in grabs:
#             if(possibleGame == False):
#                 continue
#             cubes = grab.split(',')
#             for cube in cubes:
#                 cube = cube.strip()
#                 cubeArray = cube.split(' ')
#                 if((cubeArray[1] == "green" and int(cubeArray[0]) > 13) or (cubeArray[1] == "red" and int(cubeArray[0]) > 12) or (cubeArray[1] == "blue" and int(cubeArray[0]) > 14)):
#                     possibleGame = False
#                     continue
#         if(possibleGame):
#             print(values[0])
#             result += int(values[0].split(' ')[1])
# c.submit(2,1,result)

# Part 2
lines = inpute.split('\n')
result = 0
power = []
for line in lines:
    if(len(line.split(':')) > 1): 
        values = line.split(':')
        grabs = values[1].split(';')
        lessRed = 0
        lessBlue = 0
        lessGreen = 0
        for grab in grabs:
            cubes = grab.split(',')
            for cube in cubes:
                cube = cube.strip()
                cubeArray = cube.split(' ')
                if cubeArray[1] == "green" and int(cubeArray[0]) > lessGreen:
                    lessGreen = int(cubeArray[0])
                elif cubeArray[1] == "red" and int(cubeArray[0]) > lessRed:
                    lessRed = int(cubeArray[0])
                elif cubeArray[1] == "blue" and int(cubeArray[0]) > lessBlue:
                    lessBlue = int(cubeArray[0])
        power.append(lessBlue * lessGreen * lessRed)

result = (sum(power))
print(result)
c.submit(2,2,result)
