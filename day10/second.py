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

# Work backward to determine how many possibilities there are from the back
# of the list. The last element obviously only has 1 option, so hardcode that.
possible = [0 for i in range(0, len(adapters))]
possible[len(possible)-1] = 1

# Iterate from the second-to-last element to the first element
for i in range(len(adapters)-1, -1, -1):
    # For each element that can be jumped to, add its possiblities to the
    # current element, as they are possible branches
    for n in range(1,4):
        if i+n in range(0, len(adapters)):
            if 1 <= (adapters[i+n] - adapters[i]) <= 3:
                possible[i] += possible[i+n]

# By the end, the first element will have all possibilities accounted for
print("{} arrangements possible".format(possible[0]))
