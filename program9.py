import random
som = random.randint(0,9)
son = random.randint(0,9)
sans = random.randint(0,9)
score = 0
x = (som)
y = (son)
z = (sans)
print x, y, z
if x == y or y == z or x == z :
	score += 10
	print score
elif x == y and y == z :
	score += 30
	print score
	
