#with open("demo2.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.readlines()
    adapters = [int(l.strip()) for l in lines]
    adapters.sort()

lo = adapters[0]
hi = adapters[len(adapters)-1]

# Add the outlet and your device to list
adapters.insert(0, 0)
adapters.append(hi+3)

diffs = [0, 0, 0]

for i in range(1, len(adapters)):
    x = adapters[i-1]
    y = adapters[i]

    diff = y - x
    diffs[diff-1] += 1

print(diffs)
print("{} * {} = {}".format(diffs[0], diffs[2], diffs[0]*diffs[2]))
