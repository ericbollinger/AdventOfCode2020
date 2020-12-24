floor = 0
empty = 1
taken = 10
adj_coords = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def setup(c):
    if c == '.':
        return floor
    elif c == 'L':
        return empty

def adj_score(grid,row,col):
    score = 0
    for adj in adj_coords:
        cmp_row = row + adj[0]
        if cmp_row < 0 or cmp_row >= len(grid):
            continue
        cmp_col = col + adj[1]
        if cmp_col < 0 or cmp_col >= len(grid[row]):
            continue
        score += grid[cmp_row][cmp_col]
    return score

#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [list(l) for l in lines]
    grid = [[setup(seat) for seat in row] for row in lines]

changes = 100
iterations = 0

while changes > 0:
    iterations += 1
    changes = 0
    new_grid = [[0 for seat in row] for row in lines]
    for row in range (0, len(grid)):
        for col in range(0, len(grid[row])):
            new_grid[row][col] = grid[row][col]

            seat = grid[row][col]
            if seat == empty and adj_score(grid, row, col) < 10:
                new_grid[row][col] = taken
                changes += 1
            elif seat == taken and adj_score(grid, row, col) >= 40:
                new_grid[row][col] = empty
                changes += 1
    grid = new_grid

taken_seats = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid[row][col] == taken:
            taken_seats += 1
print("Seats taken: {}".format(taken_seats))
print("It took {} iterations".format(iterations))
