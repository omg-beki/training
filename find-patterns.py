def QuestionsMarks(strParam):
  "Function checks if a string contains 3 question marks between 2 numbers and checks their sum."
  
  def CheckSum(first_value, second_value):
    "Function checks the value of two numbers and returns True if they total 10."
    if first_value + second_value == 10:
      return True
    else: return False

  count_marks, bool = 0, False
  value_before, value_after = None, None
  
  for letter in strParam:
    if letter == '?':
      count_marks += 1
    elif letter.isnumeric():
      if value_before is None:
        value_before = int(letter)
      elif value_before and value_after is None:
        value_after = int(letter)
      if count_marks >= 3 and CheckSum(value_before, value_after):
        bool = True
      else:
        count_marks = 0

  return bool

print(QuestionsMarks(input()))
