def search_array(arr: list[int], target: int) -> int:
    """
    Searches a sorted array for a target and returns the index of that target.

    If the target is not found, returns -1.

    :param arr: List of integers, the array to be searched.
    :param target: The integer value to search for.
    :return: The index of the target if found, otherwise -1.
    :rtype: int
    """

    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if target > arr[mid]:
            l = mid + 1
        elif target < arr[mid]:
            r = mid - 1
        else:
            return mid

    return -1
