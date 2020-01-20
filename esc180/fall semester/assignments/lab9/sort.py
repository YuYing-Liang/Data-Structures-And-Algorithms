def bubbleSort(a):
	swapped = True
	array = list(a)
	n = len(array)

	try:
		if n < 1:
			return [False, array]
	
		while swapped:
			swapped = False
			for i in range(1,n):
				if array[i-1] > array[i]:
					temp = array[i-1]
					array[i-1] = array[i]
					array[i] = temp
					swapped = True
	
		return [True, array]
	except:
		return [False, array]

 				
