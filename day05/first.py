def halfway(lo, hi):
    rng = hi - lo
    return lo + rng // 2

def binary_search(chars, lo, hi):
    cur = -1
    for char in chars:
        if char in ['B', 'R']:
            cur = lo = halfway(lo, hi) + 1
        else:
            cur = hi = halfway(lo, hi)
    
    return cur


#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    entries = [(l[:7], l[-3:]) for l in lines]

ids = []
max_id = -1
for entry in entries:
    row = binary_search(entry[0],1,128) - 1
    col = binary_search(entry[1],1,8) - 1

    uid = row * 8 + col
    ids.append(uid)
    if uid > max_id:
        max_id = uid

print(max_id)
