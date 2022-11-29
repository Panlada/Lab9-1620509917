# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [7,10,12,14,16,20,29,37]
target = 14
target1 = 29
# Function call
result = binary_search(arr, target)

result1 = binary_search(arr, target1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

if result != -1:
    print("Element is present at index", str(result1))
else:
    print("Element is not present in array")