from example777.math_funcs import  sum_and_square_two_numbers
from example777.subpkg.advanced_math_funcs import sum_up_to_n

def test_sum_and_square_two_numbers():
    assert sum_and_square_two_numbers(3, 5) == 225

def test_sum_up_to_n():
    assert sum_up_to_n(5)==15