def NumberStream(strParam):
"Function takes in a string of digits 2-9 and returns true if their value matches their consecutive repetition."
  for digit in range(2,10):
    streak = str(digit) * digit
    if streak in strParam:
      return True
  return False

print(NumberStream(input()))
