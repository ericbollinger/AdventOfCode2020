#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    grid = [list(l) for l in lines]

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
results = []

for num_right,num_down in slopes:
    # Counting begins on second row
    count = 0
    col = num_right
    row = num_down
    while row < len(grid):
        if col >= len(grid[row]):
            # Wrap around if column goes beyond right-hand boundary
            col = col % len(grid[row])

        if grid[row][col] == "#":
            count += 1
            #print("Tree at ({},{})".format(row, col))

        row += num_down
        col += num_right

    results.append(count)

product = results[0]
for r in results[1:]:
    product *= r

print(results)
print("Product: {}".format(product))
