def hanoi(n,start,tmp,final):
	if n > 0:
		hanoi(n - 1, start, final, tmp)
		final.append(start.pop())
		hanoi(n - 1, tmp, start, final)
		print(start,tmp,final)
		return True
	else:
		return True

def partition(n, p):
	lower = []
	upper = []

	for i in n:
		if i < p:
			lower += [i]
		else:
			upper += [i]
	return (lower, upper)

def quicksort(nums):
	if len(nums) <= 1:
		return nums

	pivot = nums[0]
	(part1, part2) = partition(nums[1:len(nums)], pivot)
	part1 = quicksort(part1)
	part2 = quicksort(part2)
	
	print("after:")
	print(part1, pivot, part2)
	return part1 + [pivot] + part2
