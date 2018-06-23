
def binary_search_first_greater(nums, target):
    """
    Search for the smallest value in a sorted list strictly greater than the target.
    :param nums: A sorted list of numbers.
    :param target: The value to be searched for.
    :return: The smallest value in the list strictly greater than target. If no number is greater than the target,
    None is returned.
    """
    left, right = 0, len(nums)      # the inclusive range of indices that could contain the result index

    while left < right:             # if left == right, search range contains one index so result has been found

        mid = (left + right) // 2
        mid_value = nums[mid]

        if target >= mid_value:     # if equal, mid is not greater than target os search RHS excluding mid
            left = mid + 1
        else:                       # mid remains a candidate, search LHS including mid
            right = mid

    return nums[left] if left != len(nums) else None


search_list = list(range(5, 15))
target = 11
print(binary_search_first_greater(search_list, target))