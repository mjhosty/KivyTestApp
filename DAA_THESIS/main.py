import time
import quicksort as qs
import insertionsort as ins
import random as rand

def sort(array):
	for step in range(1, len(array)):
		key = array[step]
		j = step - 1
		while(j >= 0 and key.get("Time", 0) < array[j].get("Time", 0)):
			array[j + 1] = array[j]
			j = j -1
			
		array[j + 1] = key


def main():
	array = []
	
	for i in range(0, 1000):
		array.append(str(rand.random()))
	
	time_el = [[]]
	
	start = time.time_ns()
	qs.sort(array)
	end = time.time_ns()
	qs_time = end - start
	
	array.clear()
	
	for i in range(0, 1000):
		array.append(str(rand.random()))
	
	start = time.time_ns()
	ins.sort(array)
	end = time.time_ns()
	ins_time = end - start
	
	table = []
	
	table.append({"Algorithm" : "Quick Sort", "Time" : int(qs_time)})
	table.append({"Algorithm" : "Insertion Sort", "Time" : int(ins_time)})
	
	sort(table)
	
	for i in table:
		print(i)
		
		
	
main()