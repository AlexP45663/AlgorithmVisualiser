
def swap(list: list, index1: int, index2: int) -> None:
    """
    function to swap 2 elements in a list given their indexes

    Args:
        list (list): the list in which the swap is to take place
        index1 (int): the index of the first element to be swapped
        index2 (int): the index of the second element to be swapped
    """
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
