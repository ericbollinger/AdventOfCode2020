def valid(entry):
    keys = entry.keys()
    
    if len(keys) == 8:
        return True

    if len(keys) == 7 and 'cid' not in keys:
        return True

    return False

#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

# Convert input into list of dicts
entries = []
entry = {}
for line in lines:
    if line == "":
        entries.append(entry)
        entry = {}
        continue
    
    data = line.split()
    for d in data:
        kv = d.split(':')
        entry[kv[0]] = kv[1]

# Add last entry, since input doesn't end with a blank line
entries.append(entry)

valid_count = 0
for entry in entries:
    if valid(entry):
        valid_count += 1

print("{} valid passports".format(valid_count))
