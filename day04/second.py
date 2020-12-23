def valid(entry):
    keys = entry.keys()

    # Too many keys missing
    if len(keys) < 7:
        return -1

    # Key other than cid missing
    if len(keys) == 7 and 'cid' in keys:
        return -2
    
    # Birth year invalid
    if not (1920 <= int(entry['byr']) <= 2002):
        return -3

    # Issue year invalid
    if not (2010 <= int(entry['iyr']) <= 2020):
        return -4

    # Expiration year invalid
    if not (2020 <= int(entry['eyr']) <= 2030):
        return -5

    # Height invalid
    if 'cm' in entry['hgt']:
        if not (150 <= int(entry['hgt'][:-2]) <= 193):
            return -6
    else:
        if not (59 <= int(entry['hgt'][:-2]) <= 76):
            return -7

    # Hair color invalid
    if entry['hcl'][0] != "#":
        return -8
    valid_list = list('0123456789abcdef')
    for c in entry['hcl'][1:]:
        if c not in valid_list:
            return -9

    # Eye color invalid
    valid_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if entry['ecl'] not in valid_list:
        return -10

    # Passport ID invalid
    if len(entry['pid']) != 9:
        return -11

    return 1

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
    validity = valid(entry)
    if validity > 0:
        valid_count += 1

print("{} valid passports".format(valid_count))
