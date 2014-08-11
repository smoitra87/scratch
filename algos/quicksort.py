import random

def quicksort(arr) : 
	if not arr : 
		return
	quicksort_sub(arr, 0, len(arr)-1)
	

def quicksort_sub(arr, start, end):
	if start >= end : 
		return
	
	pivot_idx = random.randint(start, end)	
	pivot_idx = partition(arr, start, end, pivot_idx)	

	quicksort_sub(arr, start, pivot_idx-1)
	quicksort_sub(arr, pivot_idx+1, end)


def partition(arr, start, end, pivot_idx) : 
	startIdx =  start
	swap(arr, pivot_idx, end)	 
	for nextIdx in range(start, end):
		if arr[nextIdx] < arr[end] : 
			swap(arr, nextIdx, startIdx)
			startIdx += 1
	swap(arr, startIdx, end)
	return startIdx

def swap(arr, i, j) : 
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


if __name__ == '__main__' : 
	arr = range(10) ; random.shuffle(arr)
	print(arr)
	quicksort(arr)
	print(arr)
