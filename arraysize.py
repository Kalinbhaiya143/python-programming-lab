
def combinationUtil(arr, n, r,
					index, data, i):
	# Current combination is
	# ready to be printed,
	# print it
	if(index == r):
		for j in range(r):
			print(data[j], end = " ")
		print(" ")
		return

	# When no more elements
	# are there to put in data[]
	if(i >= n):
		return

	# current is included,
	# put next at next
	# location
	data[index] = arr[i]
	combinationUtil(arr, n, r,
					index + 1, data, i + 1)
	
	# current is excluded,
	# replace it with
	# next (Note that i+1
	# is passed, but index
	# is not changed)
	combinationUtil(arr, n, r, index,
					data, i + 1)


# The main function that
# prints all combinations
# of size r in arr[] of
# size n. This function
# mainly uses combinationUtil()
def printcombination(arr, n, r):

	# A temporary array to
	# store all combination
	# one by one
	data = list(range(r))
	
	# Print all combination
	# using temporary
	# array 'data[]'
	combinationUtil(arr, n, r,
					0, data, 0)


arr = [10, 20, 30, 40, 50]

r = 3
n = len(arr)
printcombination(arr, n, r)
