import random
import pytest

from algorithms.sorting_algorithms import *

algorithms = [bubble_sort]



@pytest.mark.parametrize("sort_algorithm", algorithms)
def test_sort(sort_algorithm):
    
    #test case 1: randomly generated list of positive intgers sorted in ascending order
    random_list = [random.randint(0, 100) for _ in range(20)]
    assert sort_algorithm(random_list.copy()) == sorted(random_list), \
        f"Failed on random list: {sort_algorithm(random_list.copy())} vs {sorted(random_list)}"
        
    print(f"All tests passed for {sort_algorithm.__name__}!")

