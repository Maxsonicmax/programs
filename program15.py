num = str(raw_input())
x = len(num)
num2 = x//1
num3 = []
num3.append(num2)
num1 = int(num2)
for i in range(0, x):
	if num[i] == '0' :
		print
	elif num[i] == '1' :
		print '*'
	elif num[i] == '2' :
		print '**'
	elif num[i] == '3' :
		print '***'
	elif num[i] == '4' :
		print '****'
	elif num[i] == '5' :
		print '*****'
	elif num[i] == '6' :
		print '******'
	elif num[i] == '7' :
		print '*******'
	elif num[i] == '8' :
		print '********'
	elif num[i] == '9' :
		print '*********'


