num1 = input()
import random
x = []
y = []
z = []
u = 1
for i in range (0, num1) :
	rand = random.randint(1, num1)
	x.append ( rand )
for i in range (0, num1) :
	rand1 = random.randint(1, num1)
	y.append ( rand1 )
	z.append (x[i] / y[i])
print x
print y
print z
