import pytest

def multiply_with_reverse(nums):
    return [num * int(str(num)[::-1]) for num in nums]

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 20, 30, 40, 50], [10, 40, 90, 160, 250]),
    ([100, 200, 300, 400, 500], [100, 400, 900, 1600, 2500]),
])
def test_multiply_with_reverse(nums, expected):
    assert multiply_with_reverse(nums) == expected
