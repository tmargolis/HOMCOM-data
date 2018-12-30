import random
import os

directory = "/Users/tmg/Documents/HOMCOM/HOMCOM-data/input/golden girls"
weighted_choices = [('LEADMALE', 4), ('LEADFEMALE', 4), ('SUPMALE', 2), ('SUPFEMALE', 2), ('OTHERMALE', 1), ('OTHERFEMALE', 1)]
characters = [val for val, cnt in weighted_choices for i in range(cnt)]
print random.choice(characters)

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
		with open(directory + "/" + filename) as fp:
		    lines = fp.read().splitlines()
		with open(directory + "/" + filename, "w") as fp:
		    for line in lines:
		    	r = random.randint(0,5)
		        print >>fp, random.choice(characters) + ":" + line
    else:
        continue

