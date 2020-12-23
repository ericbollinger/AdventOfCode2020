def get_containers(allowed, inner):
    result = set()
    for outer in allowed[inner]:
        result.add(outer)
        result.update(list(get_containers(allowed, outer)))
    return result
        
#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

# Dictionary showing all colors that can contain each color
# i.e. "white" : ["black", "red"] means black and red can hold white
allowed = {}

for line in lines:
    contain_split = line.split(" bags contain ")
    outer_color = contain_split[0]

    # Establish all bag colors, even if they don't have any contents
    if outer_color not in allowed.keys():
        allowed[outer_color] = []

    contents = contain_split[1][:-1]
    if contents == "no other bags":
        continue

    for sub in contents.split(", "):
        sub = sub.replace(" bags", '')
        sub = sub.replace(" bag", '')

        inner_color = sub[2:]

        if inner_color not in allowed.keys():
            allowed[inner_color] = [outer_color]
        else:
            allowed[inner_color].append(outer_color)

result = get_containers(allowed, "shiny gold")
print(len(result))
