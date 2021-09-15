def generate_range(min, max, step):
    """
    Implement a function named generateRange(min, max, step), 
    which takes three arguments and generates a range of integers from min to max, 
    with the step. 
    The first integer is the minimum value,
    the second is the maximum of the range 
    and the third is the step. (min < max)
    """
    list_of_range = []
    try:
        # Unpack list using *
        list_of_range = [*range(min, max, step)]

    finally:
        return list_of_range
