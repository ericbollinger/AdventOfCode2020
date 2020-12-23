with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [int(l.strip()) for l in lines]

data = list(enumerate(lines))
size = len(lines)

for i,x in data:
    for j in range(i+1, size):
        if (x + lines[j] == 2020):
            y = lines[j]
            product = x * y
            print("{} + {} = 2020, so {} * {} = {}!".format(x, y, x, y, product))
            exit()
