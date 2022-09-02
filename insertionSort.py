def insertionSort(arr): 
    for i in range(1, len(arr)): 
        num = arr[i] 
        j = i-1
        while j >=0 and num < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                arr[j+1] = num
                
arr = [5,4,3,2,1,9,8,7,6]
arr1 = [5,4,3,2,1,9,8,7,6] 
insertionSort(arr) 
print("Unsorted array is: ", (arr1))
print ("Sorted array is: ", (arr))

