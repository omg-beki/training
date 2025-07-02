def LongestWord(sen):
  "Function returns the longest word in a sentence."
  longest = str()
  for word in sen:
    if word.isalpha() or word.isnumeric():
      longest += word
    else:
      longest += " "
  sen = max(longest.split(), key=len)
  return sen

print(LongestWord(input()))
