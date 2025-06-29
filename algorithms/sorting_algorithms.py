
def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp


def bubble_sort(list, ascending=True):
    for i in range(len(list)-1):
  
        swapped = False
        for j in range(len(list) -1 -i):
            if(list[j] > list[j+1]):
                swap(list, j, j+1)
                swapped = True
        if swapped == False:
            break
    
    return list
                
            

        