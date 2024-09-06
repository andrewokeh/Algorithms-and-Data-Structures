def quick_sort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] <= pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    arr[e] = arr[left]
    arr[left] = pivot

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)

    return arr
  
