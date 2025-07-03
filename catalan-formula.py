import math

def BracketCombinations(num):
  "Function returns the Catalan Number Formula for 'num' pairs of brackets."
  return math.comb(2*num, num) // (num + 1)

print(BracketCombinations(input()))
