def binary_search(arr, value):
    low = 0
    high = len(arr)
    while low <= high:
      mid = (low + high) // 2
      i = mid
      if arr[mid] == value:
          return i
      else:
        if arr[mid] < value:
          low = mid + 1
        elif arr[mid] > value:
          high = mid - 1
        else:
          return -1
    return arr

