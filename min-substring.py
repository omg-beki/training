from collections import Counter

def MinWindowSubstring(strArr):
  "Function takes a 2D array of strings and returns a window from the first string which contains all characters in the second."
  N, K = strArr
  need = Counter(K)
  missing = len(K)
  left = start = end = 0
  min_len = float('inf')
  window = {}

  for right, char in enumerate(N):
    if need[char] > 0:
      window[char] = window.get(char, 0) + 1
      if window[char] <= need[char]:
        missing -= 1
    while missing == 0:
      if right - left + 1 < min_len:
        start, end = left, right + 1
        min_len = right - left + 1
      lchar = N[left]
      if need[lchar] > 0:
        window[lchar] -= 1
        if window[lchar] < need[lchar]:
          missing += 1
      left += 1

  return N[start:end] if min_len != float('inf') else ""

print(MinWindowSubstring(input()))
