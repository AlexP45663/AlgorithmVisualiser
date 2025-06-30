from utils import swap

def bubble_sort(list: list, ascending: bool = True) -> list:
    """
    sorts a list using the bubble sort algorithm, 
    in either ascending or descending order

    Args:
        list (list): the list to be sorted
        ascending (bool, optional): true for ascending order, false for descending order. Defaults to True.

    Returns:
        list: the sorted list
    """
    
    #outer loop to iterate the algorithm n-1 times (where n is the number of elements in the list)
    for i in range(len(list)-1):
  
        #initialise a boolean variable to keep track of wether swaps have occurred
        swapped = False
        
        #loop to compare consecutive elements that arent already in the correct positions
        for j in range(len(list) -1 -i):
            
            #compare consecutive elements and swap them if they are in the wrong order, marking that a swap has taken place
            if(list[j] > list[j+1]) and ascending:
                swap(list, j, j+1)
                swapped = True
            elif(list[j] < list[j+1]) and not ascending:
                swap(list, j, j+1)
                swapped = True
        
        #if no swaps have occurred, the list is already sorted and we can stop the algorithm execution
        if swapped == False:
            break
    
    return list

def selection_sort(list: list, ascending: bool =True) -> list:
    """
    sorts a list using the selection sort algorithm, 
    in either ascending or descending order

    Args:
        list (list): the list to be sorted
        ascending (bool, optional): true for ascending order, false for descending order. Defaults to True.

    Returns:
        list: the sorted list
    """
    
    #outer loop to loop throung every element of the list except the last
    for i in range(len(list)-1):
        
        #setting the selected index to be the current i
        selected = i
        
        #looping through each element after i
        for j in range(i+1, len(list)):
            
            #if ascending order, find the index of the smallest number from i onwards and store it in selected
            if (list[j] < list[selected]) and ascending:
                selected = j
            #if descending order, find the index of the largest number from i onwards and store it in selected
            elif (list[j] > list[selected]) and not ascending:
                selected = j
        #swap the element at i with the element at the selected index
        swap(list, i, selected)
    return list
                
            
            
                

        