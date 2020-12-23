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

found = False
for x in range(0, len(lines)):
    if found:
        break

    for y in range(x+1, len(lines)):
        if found:
            break

        total = 0
        for cur in range(x, y+1):
            total += lines[cur]

            if total == target:
                print("Numbers {} through {} add up to {}.".format(lines[x], lines[y], target))
                numbers = lines[x:y+1]
                numbers.sort()
                lo = numbers[0]
                hi = numbers[len(numbers)-1]
                print("Low: {}, High: {}, Sum: {}".format(lo, hi, lo+hi))
                found = True
                break
            if total > target:
                break

if not found:
    print("Nothing was found...?")
