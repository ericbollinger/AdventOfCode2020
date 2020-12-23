def get_content_count(allowed, outer_color):
    result = 0
    if allowed[outer_color] == []:
        return 0
    for inner in allowed[outer_color]:
        # Add number of bags at current level/color
        result += inner['count']
        # Add number of nested bags
        result += inner['count'] * get_content_count(allowed, inner['color'])
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
    allowed[outer_color] = []

    contents = contain_split[1][:-1]
    if contents == "no other bags":
        continue

    for sub in contents.split(", "):
        sub = sub.replace(" bags", '')
        sub = sub.replace(" bag", '')

        count = sub[0]
        inner_color = sub[2:]

        allowed[outer_color].append({"color":inner_color, "count":int(count)})

result = get_content_count(allowed, "shiny gold")
print(result)
