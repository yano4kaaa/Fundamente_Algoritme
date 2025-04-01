import timeit

arr = [2, 3, 4, 10, 40]
x = 40
iterator = 0

def binary_search(arr, low, high, x, iterator):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            iterator += 1
            return mid, iterator
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            iterator += 1
            return binary_search(arr, low, mid - 1, x, iterator)
 
        # Else the element can only be present in right subarray
        else:
            iterator += 1
            return binary_search(arr, mid + 1, high, x, iterator)
 
    else:
        # Element is not present in the array
        return -1


def fun():
        return binary_search(arr, 0, len(arr)-1, x, iterator)

start = timeit.default_timer()
print(f"The start time is: {start}")
result = fun()
print(f"The difference of time is: {timeit.default_timer() - start}")
 
 
if  result != -1:
    print("Element is present at index", str(result[0]))
    print("Amount of iterations:", str(result[1]))
else:
    print("Element is not present in array")