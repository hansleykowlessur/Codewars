import math
import itertools

def square_sums(num):
    """
    Write function that, given an integer number N, returns array of integers 1..N 
    arranged in a way, so sum of each 2 consecutive numbers is a square.
    """
    result = []

    try:
        list_of_number = [ *range(1, num + 1, 1) ]
        
        all_possible_values = itertools.permutations(list_of_number)
        for x in list(all_possible_values):
            for index,count in enumerate(list(x)):
                if  index == len(x):
                  break
                else:
                    print((math.sqrt(x[index]) + x[index+1]).is_integer())
            else:
                continue
            break
    finally:
        return result


square_sums(5)