#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines.append('')
    
groups = []
group = []
for line in lines:
    if line == '':
        groups.append(list(set(group)))
        group = []

    group = group + list(line)

total = 0
for group in groups:
    total += len(group)

print(total)
