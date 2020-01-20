from ge import *

def main():
	m = [[0.0,0.0], [5.0,6.0], [8.0,9.0]];
	n = [[2.0,3.0,4.0,5.0],[0.0,0.0,5.0,0.0],[4.0,5.0,7.0,9.0]];

	m = ge_fw(m)
	m = ge_bw(m)

	n = ge_fw(n)
	n = ge_bw(n)

	printMatrix(m)
	printMatrix(n)

	return True

def printMatrix(m):
	for i in m:
		string = ""
		for j in i:
			string += str(j) + " "
		print(string)
	return True

main()
