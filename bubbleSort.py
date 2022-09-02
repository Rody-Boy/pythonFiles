def bubbleSort(arr):
    num = len(arr)
    for i in range(num-1):
        for j in range(0, num-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
arr = [5,4,3,2,1,9,8,7,6]
arr1 = [5,4,3,2,1,9,8,7,6]
bubbleSort(arr)
 
print("Unsorted array is: ", (arr1))
print ("Sorted array is: ", (arr))

