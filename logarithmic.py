"""
A logarithmic algorithm halves the list every time its run. A logarithmic algorithm is an algorithm that runs in log time with respect to its input size. This means that the size of the input increases, the running time of the algorithm increases logarithmically.
In Big O notation, log time complexity is represented as O(log n), where n is the size of the input. 
Log time is more efficient than linear time O(n) but less efficient than constant time O(1). 
"""

# Simple Binary Search 
# arr = [1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 1, 5, 6, 4, 3, 4, 2, 1, 10, 11, 20, 21, 11, 15, 14, 12]

# def binarySearch(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False

# print(binarySearch(arr, 5))
# print(binarySearch(arr, 50))


# Big Binary Search 
import time

numbers = [i for i in range(1, 1000001)]

def binary_search(numbers, target):
    low, high = 0, len(numbers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1
    return False  # Moved this line one level back in indentation

start_time = time.time()
result = binary_search(numbers, 950)  # Measure time for this execution
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.5f} seconds")
print(result)