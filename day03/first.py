#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    grid = [list(l) for l in lines]

# Count starts at (1,3)
count = 0
col = 3
for row in range(1, len(grid)):
    if col >= len(grid[row]):
        # Wrap around if column goes beyond right-hand boundary
        col = col % len(grid[row])

    if grid[row][col] == "#":
        count += 1
        #print("Tree at ({},{})".format(row, col))

    col += 3

print(count)
