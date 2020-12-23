#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    instructions = [l.strip() for l in lines]

hits = [0 for i in range(0, len(instructions))]
acc = 0
i = 0
while True:
    if hits[i]:
        print("Line {} hit multiple times!!! acc={}".format(i+1, acc))
        break

    hits[i] += 1

    cmd = instructions[i]
    split = cmd.split(' ')
    op = split[0]

    if op in ["jmp", "acc"]:
        sign = split[1][0]
        num = int(split[1][1:])

        if op == "jmp":
            i = i + num if (sign == "+") else i - num
            continue
        else:
            acc = acc + num if (sign == "+") else acc - num
    i += 1
