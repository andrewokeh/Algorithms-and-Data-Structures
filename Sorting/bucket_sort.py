def bucket_sort(arr: list[int]) -> list[int]:
    # Assuming arr contains numbers from 0 to n
    counts = [0] * (max(arr) + 1)

    for n in arr:
        counts[n] += 1

    i = 0
    for n in range(len(counts)):
        for _ in range(counts[n]):
            arr[i] = n
            i += 1

    return arr
  
