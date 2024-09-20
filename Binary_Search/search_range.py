def search_range(low, high):
    while low <= high:
        mid = (low + high) // 2

        if is_correct(mid) > 0:
            high = mid - 1
        elif is_correct(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1


# This helper function will vary depending on scenario
def is_correct(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0
