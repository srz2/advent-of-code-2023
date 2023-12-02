# Steven Zilberberg
# 12/1/23
# Advent of Code - Day 1
# 
# From the input, each line contains a string. Each
# The numbers which are first and last on the line should be combined
# to get the actual value which is summated
# NOW numbers can be spelled out (one - nine)

recognized_numbers = [
                    {"name": "one", "value": 1},
                    {"name": "two", "value": 2},
                    {"name": "three", "value": 3},
                    {"name": "four", "value": 4},
                    {"name": "five", "value": 5},
                    {"name": "six", "value": 6},
                    {"name": "seven", "value": 7},
                    {"name": "eight", "value": 8},
                    {"name": "nine", "value": 9}]

# These "GET" methods return an array:
# [string, index]
#   - value: Is the value of the number parsed as a string
#   - index: The index in the string where the value was parsed

def get_spelled_numbers(line: str):
    spelled_numbers = []

    for index in range(len(line)):
        if line[index].isdigit():
            continue
        for num_pair in recognized_numbers:
            num = num_pair['name']
            remaining_line = line[index:len(num) + index]
            if remaining_line.startswith(num):
                spelled_numbers.append([str(num_pair['value']), index])

    return spelled_numbers

def get_first_number(line: str):
    index = -1
    for c in line:
        index += 1
        if c.isdigit():
            return [c, index]
    return None
    
def get_last_number(line: str):
    index = -1
    for c in reversed(line):
        index += 1
        if c.isdigit():
            return [c, len(line) - index]
    return None

def main():
    file_name = 'data/input.dat'
    input_file = open(file_name, 'r')
    
    total = 0
    for raw_line in input_file:
        line = raw_line.rstrip()
        # print(line)

        spelled_numbers_pairs = get_spelled_numbers(line)
        first_pair = get_first_number(line)
        last_pair = get_last_number(line)

        # Determine which found values are used: ascii or digits
        if (first_pair is not None and len(spelled_numbers_pairs) > 0):
            if (first_pair[1] < spelled_numbers_pairs[0][1]):
                # print('Use digit', first_pair[0])
                first = first_pair[0]
            else:
                # print('Use ascii', spelled_numbers_pairs[0][0])
                first = spelled_numbers_pairs[0][0]
        elif (first_pair is not None):
            first = first_pair[0]
        else:
            first = spelled_numbers_pairs[0][0]
        
        if (last_pair is not None and len(spelled_numbers_pairs) > 0):
            if (last_pair[1] > spelled_numbers_pairs[-1][1]):
                # print('Use digit', last_pair[0])
                last = last_pair[0]
            else:
                # print('Use ascii', spelled_numbers_pairs[-1][0])
                last = spelled_numbers_pairs[-1][0]
        elif (last_pair is not None):
            last = last_pair[0]
        else:
            last = spelled_numbers_pairs[-1][0]

        # print(f'First:{first_pair} Last:{last_pair}, Spelled:{spelled_numbers_pairs}')
        # print(f'{first}{last}')
        # break

        # Error Check
        if first is None or last is None:
            print('Uh-oh: ', line)

        value = int(first + last)
        # print(value)
        total += value
    print('Result', total)

main()