def CodelandUsernameValidation(strParam):
  "Function checks a username candidate meets requirements."
  if len(strParam) < 4 or len(strParam) > 25:
    return False
  if not strParam[0].isalpha:
    return False
  if not (strParam.isalnum or strParam.__contains__('_')):
    return False
  if strParam.endswith('_'):
    return False
  return True

print(CodelandUsernameValidation(input()))
