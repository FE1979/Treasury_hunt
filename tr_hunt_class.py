from sys import stdin, stdout


class ReadTreasury():


    def get():

        treasury_table = []
        for line in stdin.readlines():
            treasury_table.append([int(x) for x in line.rstrip().split(' ')])

        return treasury_table


class HuntLookup():


    def __init__(self, treasury_table):
        self.treasury_table = treasury_table
        self.stack = []
        self.pointer = 11


    def get_hunt(self):
        """ Let find a treasury hunt """

        row = self.pointer // 10 - 1
        col = self.pointer % 10 - 1

        next_cell = treasury_table[row][col]
        if next_cell == self.pointer:
            result = f'HUNT {next_cell}\n'
        elif next_cell in self.stack:
            result = 'NO TREASURE\n'
        else:
            self.stack.append(self.pointer)
            self.pointer = next_cell
            for i in self.stack:
                stdout.write(f"{i} ")
            stdout.write("\n")
            result = self.get_hunt()

        return result


treasury_table = ReadTreasury.get()
hunt = HuntLookup(treasury_table)
stdout.write(hunt.get_hunt())
