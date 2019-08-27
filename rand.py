from sys import stdout, stderr
from random import randrange



treasury_table = [[randrange(1,6)*10 + randrange(1,6) for i in range(5)] for j
                 in range(5)]

for i in treasury_table:
    for j in i:
        stdout.write(str(j) + " ")
    stdout.write("\n")
