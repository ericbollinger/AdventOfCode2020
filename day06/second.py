#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines.append('')
    
groups = []
group = None
lost_cause_flag = False
for line in lines:
    if line == '':
        groups.append(list(group))
        group = None
        lost_cause_flag = False
        continue

    if lost_cause_flag:
        continue

    if group == None:
        group = set(list(line))
    elif len(group) == 0:
        # If this case is reached, then there were two people who had
        # no entries in common, and thus there will be no intersection
        # overall, so it should be completely skipped.
        lost_cause_flag = True
    else:
        group = group.intersection(set(list(line)))

total = 0
for group in groups:
    total += len(group)

print(total)
