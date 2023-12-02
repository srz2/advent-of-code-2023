# Steven Zilberberg
# 12/1/23
# Advent of Code - Day 1
# 
# From the input, each line contains a string. Each
# The numbers which are first and last on the line should be combined
# to get the actual value which is summated

def get_first_number(line: str) -> str:
    for c in line:
        if c.isdigit():
            return c
    return None
    
def get_last_number(line: str) -> str:
    for c in reversed(line):
        if c.isdigit():
            return c
    return None
    
def main():
    file_name = 'data/input1.dat'
    input_file = open(file_name, 'r')
    
    total = 0
    for raw_line in input_file:
        line = raw_line.rstrip()
        first = get_first_number(line)
        last = get_last_number(line)

        # Error Check
        if first is None or last is None:
            print('Uh-oh: ', line)

        value = int(first + last)
        print(value)
        total += value
    print('Result', total)

main()