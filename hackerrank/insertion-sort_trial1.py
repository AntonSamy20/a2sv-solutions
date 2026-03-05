def insertionSort1(n, arr):
    key = arr[n-1]
    i = n-2
    
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
    
    arr[i+1] = key
    print(*arr)