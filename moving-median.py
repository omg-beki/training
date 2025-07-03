def MovingMedian(arr):
  "Function accepts a 1D array and computes the median of the first value's sliding window across the array."
  N = arr[0]
  nums = arr[1:]
  res = list()
  for i in range(len(nums)):
    window = nums[max(0, i-N+1):i+1]
    win_sorted = sorted(window)
    L = len(win_sorted)
    if L % 2 == 1:
      median = win_sorted[L//2]
    else:
      median = int((win_sorted[L//2 - 1] + win_sorted[L//2]) / 2)
    res.append(str(median))
  return ",".join(res)

print(MovingMedian(input()))
