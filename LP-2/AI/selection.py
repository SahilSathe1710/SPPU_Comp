def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

n = int(input("Enter lenght of array: "))
arr = []
for _ in range(n):
    x = int(input("Enter element:"))
    arr.append(x)
print("Initial array: ",arr)
sorted = selection_sort(arr)
print("Sorted array: ",sorted)