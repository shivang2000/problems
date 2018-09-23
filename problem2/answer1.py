def monkey_trouble_me_1(a_smile, b_smile):
  if (a_smile == True and b_smile == True):
    return True
  elif (a_smile == False and b_smile == False):
    return True 
  else :
    return False

def monkey_problem_me_2(a_smile, b_smile):
    if (a_smile == b_smile):
        return True
    else :
        return False

def monkey_trouble_website_solution(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False