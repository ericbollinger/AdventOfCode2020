#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    instructions = [l.strip() for l in lines]

num_instructions = len(instructions)

for changed in range(0, num_instructions):
    old = ""
    if "jmp" in instructions[changed]:
        old = instructions[changed]
        instructions[changed] = instructions[changed].replace("jmp", "nop")
    elif "nop" in instructions[changed]:
        old = instructions[changed]
        instructions[changed] = instructions[changed].replace("nop", "jmp")
    else:
        # nothing changed, so nothing will be different!
        continue

    hits = [0 for i in range(0, num_instructions)]
    acc = 0
    i = 0
    while True:
        # Goal: Hit one line beyond given instructions
        if i == num_instructions:
            print("Console booted successfully after changing line {}! acc={}".format(changed+1, acc))
            exit()

        # Out of bounds
        if not 0 <= i < num_instructions:
            break

        # Loop is detected
        if hits[i]:
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

    if old:
        instructions[changed] = old
