def QuestionsMarks(strParam):
  "Function checks if a string contains 3 question marks between 2 numbers and checks their sum."
  
  numbers, bool, all_bool = list(), False, True
  value_before, value_after = None, None
  
  for index, char in enumerate(strParam):
    if char.isdigit():
      numbers.append((index, int(char)))
  
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i][1] + numbers[j][1] == 10:
        value_before, value_after = numbers[i][0], numbers[j][0]
        if strParam[value_before+1:value_after].count('?') == 3:
          bool = True
        else:
          all_bool = False
  if all_bool:
    return bool
  else:
    return False

print(QuestionsMarks(input()))
