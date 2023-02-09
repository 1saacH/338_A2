import random
import json

file = open("ex2.json")
lists = json.load(file)
shuffled = []

for array in lists:
    listcopy = array
    random.shuffle(listcopy)
    shuffled.append(listcopy)


newfile = json.dumps(shuffled, indent=4)

with open("ex2.5.json", "w") as outfile:
    outfile.write(newfile)