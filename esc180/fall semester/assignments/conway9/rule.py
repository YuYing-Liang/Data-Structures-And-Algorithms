def rule(a_value, a_list):
	sumList = 0;

	for i in a_list:
		sumList += i

	if a_value == 1:
		if sumList == 2 or sumList == 3:
			return 1
		else:
			return 0
	else:
		if sumList == 3:
			return 1
		else:
			return 0		
