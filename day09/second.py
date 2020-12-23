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
        target = lines[i]
        print("Rule failed for {}!".format(target))
        break

start = 0
end = 2

while (start < len(lines)-1) and (end < len(lines)):
    cur = lines[start:end]
    total = sum(cur)

    if total > target:
        start += 1
    elif total < target:
        end += 1
    else:
        print("Numbers {} through {} add up to {}.".format(lines[start], lines[end-1], total))
        cur.sort()
        lo = cur[0]
        hi = cur[len(cur)-1]
        print("Low: {}, High: {}, Sum: {}".format(lo, hi, lo+hi))
        break
