def BracketMatcher(strParam):
  "Function checks for pairs of brackets in a string."
  left, right = 0, 0
  for char in strParam:
    if char == '(':
      left += 1
    if char == ')':
      right += 1
  if left == right:
    return 1
  else:
    return 0

print(BracketMatcher(input()))
