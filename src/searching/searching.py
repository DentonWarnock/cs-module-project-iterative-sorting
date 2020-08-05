def linear_search(arr, target):
    # Your code here
    # loop through all items in array
    for i in range(len(arr)):
        # if item == target - return item's index
        if (arr[i] == target):
            return i        
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # assume list is pre sorted
    # set variables for beginning and end of the array
    low = 0
    high = len(arr) - 1
    # start looping
    while low <= high:
        # find array mid point index - round down to nearest integer
        mid = (low + high) // 2
        # if middle index == target return middle index
        if arr[mid] == target:
            return mid
        # if middle index is greater than target - reset the high to the middle index - 1
        if arr[mid] > target:
            high = mid - 1
        # otherwise middle index is less than target - reset the low to the middle index + 1
        else:
            low = mid + 1
    # if we exit the loop withouth returning the mid index then we have not found our item
    return - 1
            
        
    

    return -1  # not found
