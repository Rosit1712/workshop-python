for line in open('workfile.txt'):
    print(line, end="")

with open('workfile.txt') as f:
    for line in f:
        print(line, end="")