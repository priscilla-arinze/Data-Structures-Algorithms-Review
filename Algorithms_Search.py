"""
See Algorithms - Search Algorithms.ipynb for more interactive examples on all of these functions below
"""

###### LINEAR SEARCH ######
def linear_search(ls, target_element):
    for index in range(len(ls)):
        if ls[index] == target_element:
            return index
    
    return None ## if target_element is not found in list


## Informs user if target element is found in list or not
def linear_search_verify(index):
    if index is not None:
        print("Target element found at index #" + str(index))
    else:
        print("Target element is not found in list")





###### BINARY SEARCH ######
## Under the assumption that the list passed into the function is already sorted
## Looks for the target element in the list by dividing the list again and again until found, otherwise return None
def iterative_binary_search(sorted_list, target_element):
    first_element_index = 0 # O(1)
    last_element_index = len(sorted_list) - 1 # O(1)


    # Will keep repeating loop and "discarding" halves until the first element is greater than the last element if & when found
    # Otherwise, will return None
    while first_element_index <= last_element_index:

        ## Find middle elemnt with floor division (//) : rounds down to nearest whole number
        middle_element_index = (first_element_index + last_element_index) // 2  

        # best case scenario
        if sorted_list[middle_element_index] == target_element:
            return middle_element_index

        # ignore/"discard" left (lower) side of list if middle element is LESS than the target element (too low, seek out higher numbers)
        elif sorted_list[middle_element_index] < target_element:
            first_element_index = middle_element_index + 1  # change starting position for search
        
        # ignore/"discard" right (higher) side of list if middle element is GREATER than the target elemnt (too high, seek out lower numbers)
        else:
            last_element_index = middle_element_index - 1 # change ending position for search
    

    return None  ## if target_element is not found in list


## Informs user if target element is found in list or not
def iterative_binary_search_verify(index):
    if index is not None:
        print("Target element found at index #" + str(index))
    else:
        print("Target element is not found in list")



## Under the assumption that the list passed into the function is already sorted
## Looks for the target element in the list by dividing the list again and again until found, otherwise return None
def recursive_binary_search(sorted_list, target_element):
    
    if len(sorted_list) == 0:
        return False
    else:
        ## Find middle elemnt with floor division (//) : rounds down to nearest whole number
        middle_element_index = (len(sorted_list)) // 2  

         # best case scenario
        if sorted_list[middle_element_index] == target_element:
            return True
        else:
            ## RECURSIVE VERSION
            # if middle element is less/greater than target element, re-execute same function but with a sub-list: 
            if sorted_list[middle_element_index] < target_element: # ignore left side, seek out higher numbers
                # slice list starting at middle element up until the very end of the list
                return recursive_binary_search(sorted_list[middle_element_index+1 : ], target_element) 
            else: # ignore right side, seek out lower numbers
                # slice list starting at first element up until the middle element
                return recursive_binary_search(sorted_list[0 : middle_element_index], target_element) 
    

## Informs user if target element is found in list or not
def recursive_binary_search_verify(result):
    print("Target element found?", result)