import coreAdventOfCode as c
import re



# data = "Card   1: 98 16 95 90 53 33 43  7 46 45 | 85 15 78 57 34 10 46 90 33 13  8 54  4 37 25 63 55 41  7 82 69 16 30 76  2\nCard   2: 55 34 32 64 52 76 54  8 36 94 | 94 95 76 66 38 26 80 54 32 91 19 64 21 55 36 96 52 82 15 56 70 89 46 71 74\nCard   3: 35 26 78 89 82 92 37 10  3 43 | 41 81 62 52 92 63 26 57 28 55 93 30 72 71 99 84 96 60 82 78 73 65 43 50 25\nCard   4: 71 27 75 73 79 83 44 55 31 49 | 74 79 17 38 28 41 88 25 61 55 12 40 43 44  6 73 71 83 49 75 67 80 27 10 31\nCard   5: 26 10 58 57 85 65 42 23 97 30 | 65 26 85 97 31 10 23 88 58 16 80 22 67 44  7 77 30 69 34 42 24 57 66 27 99\nCard   6: 56 24 39 96 36 46 48 94 30 58 | 16 24 99 48 73 30 91  7 87 57 23 49 69 39 94 63 17 58 56  9 34 36 31 46 96\nCard   7: 82 75 29 17 66 41 25 52 98  5 | 30 41 73 66 25 57 47 22 89 34 75 21  5 63 90 85 13 38 82 17 29 71 98 52  1\nCard   8: 45 56 10 72 89 61 64 32 82  7 | 64 32 45 67 84 28  2 56 10 82 55 72  6 61 97 91 89  7 22 70 88  3 41 98 13\nCard   9: 92 39 44 48 96 72 43 78 98 86 | 76 87  9 45 98 47 31 44 34 92 43 54 72 39 50 96 77 86 62 13 16  6 78 48  8\nCard  10: 66 44 15 56 88 27 54 51  5 92 | 44 92 18 56 22 85 40 76 90 83  5 13 35 59 27 65 62 15 95 94 81 39 88 54  6"

# data = c.get_input(4).split('\n')
# data.pop()
# result = 0
# for card in data:
#     winningNumbers = re.findall("(?<=\:)(.*?)(?=\|)",card)[0].strip().replace('  ', ' ').split(' ')
#     numbers = re.findall("(?<=\|).*",card)[0].strip().replace('  ', ' ').split(' ')
#     findedNumbers = list(filter(lambda x: x in winningNumbers,numbers))
#     if len(findedNumbers) > 0:
#         if(len(findedNumbers) == 1):
#             result+=1
#         else:
#             tmpResult = 1
#             for num in range(len(findedNumbers)-1):
#                 tmpResult *= 2
#             result += tmpResult

# # c.submit(4,1,result)

# Part 2

data = c.get_input(4).split('\n')
# data = data.split('\n')
data.pop()
cardIndex = 0
cardDic = [1]*len(data)
for card in data:
    winningNumbers = re.findall("(?<=\:)(.*?)(?=\|)",card)[0].strip().replace('  ', ' ').split(' ')
    numbers = re.findall("(?<=\|).*",card)[0].strip().replace('  ', ' ').split(' ')
    findedNumbers = list(filter(lambda x: x in winningNumbers,numbers))
    if len(findedNumbers) > 0:
       i = cardIndex+1
       for num in range(len(findedNumbers)):
           cardDic[i] += cardDic[cardIndex] 
           i += 1
    cardIndex += 1

print("some du tableau ",sum(cardDic))
c.submit(4,2,sum(cardDic))

#Gagne un copies des cartes suivantes en fonctions du nombre du numéro gagnant trouvé (les copies font aussi gagner des cartes)
# data = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n"
#Card 1 -> 1
#Card 2 -> 2
#Card 3 -> 4
#Card 4 -> 8
#Card 5 -> 14
#Card 6
#attented result 30 