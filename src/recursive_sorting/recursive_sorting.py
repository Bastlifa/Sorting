# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(len(merged_arr)):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1: 
        return arr
    if len(arr) == 0:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_sort(left) or left
    right = merge_sort(right) or right

    arr = merge(left, right)
    
    return arr

# print(merge_sort([4, 2, 3, 1, 0, 9, 5, 4, 2, 0, 1, 8, 7]))

# STRETCH: implement an in-place merge sort algorithm
# pass on that
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
