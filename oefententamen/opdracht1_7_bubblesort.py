def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return(arr)

print(bubble_sort([3,5,3,6,3]))

