class Entry:
    def __init__(self, text):
        parts = text.split()

        positions = parts[0].split('-')
        self.pos1 = int(positions[0]) - 1
        self.pos2 = int(positions[1]) - 1

        self.req = parts[1].split(':')[0]

        self.pw = parts[2]

    def valid(self):
        return (self.pw[self.pos1] == self.req) ^ (self.pw[self.pos2] == self.req)

        
#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    entries = [Entry(l) for l in lines]

count = 0
for entry in entries:
    if entry.valid():
        count += 1
        #print("Valid: {}".format(entry.pw))

print(count)
