# Selection sort in python

def selectionSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(len(arr)):
        
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
selectionSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i]),