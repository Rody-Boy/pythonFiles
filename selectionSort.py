arr= [5,4,3,2,1,9,8,7,6]
arr1 = [5,4,3,2,1,9,8,7,6]

for i in range(len(arr)): 
    num= i
    for j in range(i+1, len(arr)): 
        if arr[num] > arr[j]: 
            num = j 
            
    arr[i], arr[num] = arr[num], arr[i] 
  
print ("Unsorted array is:", (arr1)) 
print ("Sorted array is:", (arr)) 
