def insertion_sort(arr: list[int]) -> list[int]:
    # Traverse through array starting from 1
    for i in range(1, len(arr)):
        j = i - 1
        while arr[j + 1] < arr[j] and j >= 0:
            # Swap arr[j] and arr[j + 1] since they are out of order
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr
