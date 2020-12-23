#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [int(l.strip()) for l in lines]

data = list(enumerate(lines))
size = len(lines)

for i,x in data:
    for j in range(i+1, size):
        for k in range(j+1, size):
            if (x + lines[j] + lines[k] == 2020):
                y = lines[j]
                z = lines[k]
                product = x * y * z
                print("{} + {} + {} = 2020, so {} * {} * {} = {}!".format(
                        x, y, z, x, y, z, product))
                exit()
