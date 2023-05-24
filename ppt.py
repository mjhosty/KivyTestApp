
def insertionSort(array):
	step = 1
	for i in range(len(array) - 1):
		key = array[step]
		j = step - 1
		
		while(j >= 0 and key < array[j]):
			array[j + 1] = array[j]
			j = j -1
		
		array[j + 1] = key
		step = step + 1



def main():
	a = "Hello"
	b = "Ahh"
	
	print(a > b)
main()

