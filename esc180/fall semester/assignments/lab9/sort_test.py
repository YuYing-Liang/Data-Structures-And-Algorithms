from sort import *

def main():
	nums = [3,5,4,2,1];
	nums2 = [8,3,5,0,9,1,6];

	#print original
	print(nums)
	print(nums2)
	#print new
	nums = bubbleSort(nums)[1]
	print(nums)
	nums2 = bubbleSort(nums2)[1]
	print(nums2)
main()
