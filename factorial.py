def FirstFactorial(num):
  "Function returns the factorial of a number."
  if num != 1:
    num *= FirstFactorial(num - 1)
  return num

print(FirstFactorial(input()))
