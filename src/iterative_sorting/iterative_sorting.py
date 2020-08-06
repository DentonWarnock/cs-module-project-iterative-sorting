# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        
        # find the minimum element in remaining unsorted array
        for next_index in range(cur_index + 1, len(arr)):
            if arr[next_index] < arr[smallest_index]:
                smallest_index = next_index
                
        # swap the found minimum element with the first element
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # we are done IF a loop through and nothing happens
    # loop through all elements
    for index in range(len(arr) - 1):
        # loop through unsorted items (exclude last items that are already sorted)
        for cur_index in range(len(arr) - index - 1):
            # if first item is greater than first item, swap them
            if arr[cur_index] > arr[cur_index + 1]:
                # swap the items
                arr[cur_index], arr[cur_index + 1] = arr[cur_index + 1], arr[cur_index]                
    # return sorted arr
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
