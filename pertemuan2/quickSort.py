import os 
os.system('cls')

def quickSort(arr):
    if len(arr) <= 1:
        return arr
	else:
		pivot = arr[0]

		left = [x for x in arr[1:] if x <= pivot] 
        
		right = [x for x in arr[1:] if x >= pivot]
        
		return quickSort(left) + [pivot] + quickSort(right)
    
arr = [11, 9, 0, 2, 4, 5]

print(f"List Sebelum di Sort {arr}")

result = quickSort(arr)

print(f"List setelah di sort {result}")