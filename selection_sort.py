# Selection sort

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest, smallest_index = arr[i], i
	return smallest_index


def findBiggest(arr):
	biggest = arr[0]
	biggest_index = 0
	for i in range(len(arr)):
		if arr[i] > biggest:
			biggest, biggest_index = arr[i], i
	return biggest_index

def selectionSort(arr, increasing = True):
	"""Selection sort algorithm in ascending or descending order.

	Args:
    	arr: array
    	increasing (bool): if True, it will sort in increasing order. Otherwise, if False, it will sort in decreasing order. True is the default.

    Returns:
    	sorted array
	"""
	newArray = []
	if increasing:
		for i in range(len(arr)):
			smallest = findSmallest(arr)
			newArray.append(arr.pop(smallest))
	else:
		for i in range(len(arr)):
			biggest = findBiggest(arr)
			newArray.append(arr.pop(biggest))

	return newArray

if __name__ == '__main__':
	# execute only if run as a script
	print('Sorted array:')
	print(selectionSort([4, 7, 0, 100, 1, 8, 3, 2], increasing = False))