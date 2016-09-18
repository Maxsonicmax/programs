import curses
num1 = raw_input()
u = []
u.append(num1)
num2 = int(num1)
for i in range (0, 3) :
	if u[i] == 0 :
		print " **** "
		print "*    *"
		print "*    *"
		print "*    *"
		print " **** "
	elif u[i] == 1 :
		print "*"
		print "*"
		print "*"
		print "*"
		print "*"
	elif u[i] == 2 :
		print " **** "
		print "*    *"
		print "    * "
		print "   *  "
		print "  *   "
		print " *    "
		print "******"
	elif u[i] == 3 :
		print " **** "
		print "*    *"
		print "    * "
		print "   *  "
		print "    * "
		print "*    *"
		print " **** "
	elif u[i] == 4 :
		print "*    *"
		print "*    *"
		print "*    *"
		print "******"
		print "     *"
		print "     *"
		print "     *"
	elif u[i] == 5 :
		print "******"
		print "*"
		print "*"
		print "******"
		print "     *"
		print "*    *"
		print " **** "
	elif u[i] == 6 :
		print " *****"
		print "*"
		print "*"
		print "******"
		print "*    *"
		print "*    *"
		print " **** "
	elif u[i] == 7 :
		print "******"
		print "     *"
		print "     *"
		print "     *"
		print "     *"
		print "     *"
	elif u[i] == 8 :
		print " **** "
		print "*    *"
		print "*    *"
		print " **** "
		print "*    *"
		print "*    *"
		print " **** "
	elif u[i] == 9 :
		print " **** "
		print "*    *"
		print "*    *"
		print "******"
		print "     *"
		print "     *"
		print "***** "
