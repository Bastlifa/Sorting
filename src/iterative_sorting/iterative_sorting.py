# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_happened = True
    while(swap_happened):
        swap_happened = False
        for i in range(len(arr) - 1):
            if arr[i+1] < arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swap_happened = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # find largest number in array
    data_range = maximum
    if data_range == -1:
        for i in arr:
            if i > data_range:
                data_range = i
    # Make list of 0's, length is max data val
    data_arr = [0 for i in range(data_range + 1)]

    # loop over arr, if <0, error
    # add 1 to data_arr at arr[i] 
    for i in range(len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            data_arr[arr[i]] += 1

    # Starting at index 1, add previous number to current index val
    for i in range(1, data_range + 1):
        data_arr[i] += data_arr[i-1]
    
    output = [*arr]

    for i in range(len(arr)):
        output[data_arr[arr[i]] -1]  = arr[i]
        data_arr[arr[i]] -= 1

    return output

a = [1,5,6,7,3,1,0,4,7,0]
print(count_sort(a))