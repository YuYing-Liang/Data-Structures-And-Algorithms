def ge_fw(matrix):
	#find first row with a non-zero entry and exchange with first row
	m = list(matrix)
	
	if len(m) < 1:
		return m

	for i in range(len(m)):
		if m[i][0] != 0:
			temp = m[i]
			m[i] = m[0]
			m[0] = temp
			break

	#add multiples of the first row to lower rows so that the lower entries ofthe first column are all zero
	#form the submatrix arising from deleting the first col and row and applying the forward step

	n_cols = len(m[0])
	n_rows = len(m)
	k = 0

	for x in range(n_cols):	
		for i in range(k + 1, len(m)):	#loop through rows			
			if m[i][x] == 0:
				for z in range(i, len(m)):
					if m[z][0] != 0:
						temp = m[z]
						m[z] = m[i]
						m[i] = temp
						break	
			
			factor = m[i][x]/m[k][x]

			#apply factor to columns of that row
			for j in range(x,len(m[i])):
				m[i][j] -= factor * m[k][j]
		k += 1
	return m

def ge_bw(matrix):
	m = list(matrix)
	
	if len(m) < 1:
		return m

	#starting with the last nonzero row, normalize the row by its first nonzero entry

	
	#find the last non-zero row
	lastNonZeroRow = -1

	for i in range(len(m)-1, -1, -1):
		for j in range(len(m[i])):
			if m[i][j] != 0:
				lastNonZeroRow = i
		if lastNonZeroRow > -1:
			break



	#you want the first nonzero column in the row to be one (multiply row by a nonzero factor)
	for j in range(lastNonZeroRow, -1, -1):		
		factor = 1
		factorFound = False
		for i in range(len(m[j])):
			if m[j][i] != 0 and not factorFound:
				factor = m[j][i]
				factorFound = True

			m[j][i] = m[j][i]/factor  


	#add multiples of this row to previous rows so that all the entries in the column containing leading 1s are zero
	for i in range(lastNonZeroRow, 0, -1):

		#find column that contains leading 1
		leadingOneCol = 0
	
		for j in range(len(m[i])):
			if m[i][j] == 1:
				leadingOneCol = j
				break


		for j in range(i-1, -1, -1):
			factor = m[j][leadingOneCol];
			for x in range(leadingOneCol, len(m[i]), 1):				
				m[j][x] -= factor * m[i][x]
				
	return m

