import random
import pytest

from algorithms.sorting_algorithms import *

algorithms = [bubble_sort, selection_sort]



@pytest.mark.parametrize("sort_algorithm", algorithms)
def test_sort(sort_algorithm):
    
    random_list = [random.randint(0, 100) for _ in range(100)]
    random_negative_list = [random.randint(-100, 0) for _ in range(100)]
    empty_list = []
    duplicates_list = [0, 12, 12, 2, 2, 6, 75, 75, 75, 33, 22, 11, 22, 17]  
    mixed_list = [12, -7, 34, -21, 0, 8, -13, 45, -2, 19, -30, 27, -11, 6, -5, 23, -16, 10, -3, 4]  
    
    #test case 1: randomly generated list of positive intgers sorted in ascending order
    assert sort_algorithm(random_list.copy()) == sorted(random_list), \
        f"Failed on positive random list (ascending): \
            {sort_algorithm(random_list.copy())} vs {sorted(random_list)}"
        
    #test case 2: randomly generated list of positive intgers sorted in descending order
    assert sort_algorithm(random_list.copy(), False) == list(reversed(sorted(random_list))), \
        f"Failed on positive random list (descending): \
            {sort_algorithm(random_list.copy(), False)} vs {list(reversed(sorted(random_list)))}"
        
    #test case 3: randomly generated list of negative intgers sorted in ascending order
    assert sort_algorithm(random_negative_list.copy()) == sorted(random_negative_list), \
        f"Failed on negative random list (ascending): \
            {sort_algorithm(random_negative_list.copy())} vs {sorted(random_negative_list)}"
        
    #test case 4: randomly generated list of negative intgers sorted in descending order
    assert sort_algorithm(random_negative_list.copy(), False) == list(reversed(sorted(random_negative_list))), \
        f"Failed on negative random list (descending): \
            {sort_algorithm(random_negative_list.copy(), False)} vs {list(reversed(sorted(random_negative_list)))}"
    
    #test case 5: empty list sorted in ascending order
    assert sort_algorithm(empty_list.copy()) == empty_list, \
        f"Failed on empty list (ascending): \
            {sort_algorithm(empty_list.copy())} vs {empty_list}"
        
    #test case 6: empty list sorted in descending order
    assert sort_algorithm(empty_list.copy(), False) == empty_list, \
        f"Failed on empty list (descending): \
            {sort_algorithm(empty_list.copy(), False)} vs {empty_list}"
      
    #test case 7: list with dupicate entries sorted in ascending order
    assert sort_algorithm(duplicates_list.copy()) == sorted(duplicates_list), \
        f"Failed on duplicates list (ascending): \
            {sort_algorithm(duplicates_list.copy())} vs {sorted(duplicates_list)}"
        
    #test case 8: list with dupicate entries sorted in descending order
    assert sort_algorithm(duplicates_list.copy(), False) == list(reversed(sorted(duplicates_list))), \
        f"Failed on duplicates list (descending): \
            {sort_algorithm(duplicates_list.copy(), False)} vs {list(reversed(sorted(duplicates_list)))}"
    
    #test case 9: list with positive and negative integers sorted in ascending order
    assert sort_algorithm(mixed_list.copy()) == sorted(mixed_list), \
        f"Failed on mixed positive and negative integers list (ascending): \
            {sort_algorithm(mixed_list.copy())} vs {sorted(mixed_list)}"
        
    #test case 10: list with positive and negative integers sorted in descending order
    assert sort_algorithm(mixed_list.copy(), False) == list(reversed(sorted(mixed_list))), \
        f"Failed on mixed positive and negative integers list (descending): \
            {sort_algorithm(mixed_list.copy(), False)} vs {list(reversed(sorted(mixed_list)))}"
        
    print(f"All tests passed for {sort_algorithm.__name__}!")

