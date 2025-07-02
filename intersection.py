def FindIntersection(strArr):
  "Function returns common values within a 2-D Array."
  jointArr = sorted(set(strArr[0].split(',')) & set(strArr[1].split(',')), key=int)
  return ",".join(jointArr)

print(FindIntersection(input()))
