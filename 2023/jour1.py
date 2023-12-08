import coreAdventOfCode as c
import re
number_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def get_numbers(inp):
    # numbers = re.findall('[0-9]',inp)
    # # part 2
    numbers = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]))',inp)
    length = len(numbers)
    if(length > 0):
        if numbers[0].isdigit():
            first_number = numbers[0]
        else:
            first_number = number_mapping.get(numbers[0])
        if numbers[-1].isdigit():
            last_number = numbers[-1]
        else:
            last_number = number_mapping.get(numbers[-1])
        number = first_number + last_number
        return int(number)
    else:
        return 0
i = c.get_input(1)
lines = i.split('\n')
result = 0
for line in lines:
    result += get_numbers(line)
print(result)
# c.submit(1,1,result)
# c.submit(1,2,result)
