num = raw_input()
num1 = len(num)
x = 0
y = 1
for i in range(0, num1) :
	if i%2 == 0 :
		x = x + int(num[i])
	else :
		y = y * int(num[i])
print x
print y
