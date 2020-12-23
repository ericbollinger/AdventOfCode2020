class Entry:
    def __init__(self, text):
        parts = text.split()

        rang = parts[0].split('-')
        self.low = int(rang[0])
        self.high = int(rang[1])

        self.req = parts[1].split(':')[0]

        self.pw = parts[2]

    def valid(self):
        occ = self.pw.count(self.req)
        if (occ >= self.low and occ <= self.high):
            return True
        return False

#with open('demo.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    entries = [Entry(l) for l in lines]

count = 0
for entry in entries:
    occ = entry.pw.count(entry.req)
    if entry.valid():
        count += 1
        #print("Valid: {}".format(entry.pw))

print(count)
