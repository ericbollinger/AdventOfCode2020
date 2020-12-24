floor = 0
empty = 1
taken = 10
adj_coords = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# Initialize scores
def init(c):
    if c == '.':
        return floor
    elif c == 'L':
        return empty

# Return value of first chair in the given direction
def score_in_direction(grid,row,col,row_dir,col_dir):
    cur_row = row + row_dir
    cur_col = col + col_dir
    while 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[cur_row]):
        if grid[cur_row][cur_col] == taken:
            return taken
        elif grid[cur_row][cur_col] == empty:
            return empty
        cur_row += row_dir
        cur_col += col_dir
    return 0

# Get score of all visible seats
def visible_score(grid,row,col):
    score = 0
    for adj in adj_coords:
        score += score_in_direction(grid,row,col,adj[0],adj[1])
    return score

#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [list(l) for l in lines]
    grid = [[init(seat) for seat in row] for row in lines]

changes = 100
iterations = 0

while changes > 0:
    iterations += 1
    changes = 0
    new_grid = [[0 for seat in row] for row in lines]
    for row in range (0, len(grid)):
        for col in range(0, len(grid[row])):
            # By default, copy value
            new_grid[row][col] = grid[row][col]

            seat = grid[row][col]
            # If no visible seats are taken, fill empty chair
            if seat == empty and visible_score(grid, row, col) < 10:
                new_grid[row][col] = taken
                changes += 1
            # If 5 or more visible seats are taken, leave chair
            elif seat == taken and visible_score(grid, row, col) >= 50:
                new_grid[row][col] = empty
                changes += 1
    grid = new_grid

# Count how many seats are filled after equilibrium is reached
taken_seats = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid[row][col] == taken:
            taken_seats += 1
print("Seats taken: {}".format(taken_seats))
print("It took {} iterations".format(iterations))
