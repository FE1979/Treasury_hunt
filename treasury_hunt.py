from sys import stdin, stdout


def read_treasury_table():

    treasury_table = []
    for line in stdin.readlines():
        treasury_table.append([int(x) for x in line.rstrip().split(' ')])

    return treasury_table


def lookup_hunt(treasury_table):
    """ Let find a treasury hunt """

    stack = []
    pointer = 11
    result = None

    def get_row(p):
        return p // 10 - 1

    def get_col(p):
        return p % 10 - 1


    while pointer not in stack:
        next_cell = treasury_table[get_row(pointer)][get_col(pointer)]
        if next_cell == pointer:
            result = f'HUNT {next_cell}'
            stack.append(pointer)
        else:
            stack.append(pointer)
            pointer = next_cell

    stack_string = " ".join(str(i) for i in stack)
    return f"{stack_string} {result or 'NO TREASURE'}"


stdout.write(lookup_hunt(read_treasury_table()) + "\n")
