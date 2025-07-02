def FirstFactorial(num):

  if num != 1:
    num *= FirstFactorial(num - 1)
  return num

print(FirstFactorial(input()))
