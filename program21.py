n = str(raw_input())
num = len(n)
x = 0
y = 0
u = 0
t = 0
for i in range (0, num) :
	if n[i] == '0' :
		x = x + 1
		y = x
	elif n[i] == '1' :
		x = 0
print y
#sldfsgsdfg
