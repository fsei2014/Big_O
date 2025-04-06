import time
import random
import sys

sys.setrecursionlimit(10000)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Generate random data
data = random.sample(range(1, 100000), 1000)
target = data[500]

# Pengujian waktu eksekusi
for algo, sort_func in zip(["Bubble Sort", "Merge Sort"], [bubble_sort, merge_sort]):
    test_data = data.copy()
    start = time.time()
    sort_func(test_data)
    end = time.time()
    print(f"{algo} execution time: {end - start:.5f} seconds")

# Binary Search membutuhkan data terurut
sorted_data = sorted(data)
start = time.time()
idx = binary_search(sorted_data, target)
end = time.time()
print(f"Binary Search found target at index {idx}, execution time: {end - start:.7f} seconds")
