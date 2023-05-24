def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if(array[j] <= pivot):
			i = i + 1
			array[i], array[j] = array[j], array[i]
	array[i + 1], array[high] = array[high], array[i + 1]
	return i + 1
	
def sort(array):
	stack = [(0, len(array) - 1)]
	while stack:
		low, high = stack.pop()
		if low < high:
			pi = partition(array, low, high)
			stack.append((low, pi - 1))
			stack.append((pi + 1, high))