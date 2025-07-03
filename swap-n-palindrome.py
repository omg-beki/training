def PalindromeSwapper(strParam):
  "Function returns a palindrome if any 2 adjacent letters can be swapped (or not) & achieve it."
  if strParam == strParam[::-1]:
    return strParam
  strList = list(strParam)
  for i in range(len(strList)-1):
    strList[i], strList[i+1] = strList[i+1], strList[i]
    if strList == strList[::-1]:
      return ''.join(strList)
    strList[i], strList[i+1] = strList[i+1], strList[i]
  return "-1"

print(PalindromeSwapper(input()))
