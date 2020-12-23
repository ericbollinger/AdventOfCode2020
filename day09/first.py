#length = 5
length = 25

#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [int(l.strip()) for l in lines]

for i in range(length, len(lines)):
    prev = lines[i-length:i]

    found = False
    for x in range(0, length):
        if found:
            break
        for y in range(x+1, length):
            if lines[i] == prev[x] + prev[y]:
                found = True
                break

    if not found:
        print("Rule failed for {}!".format(lines[i]))
        break
