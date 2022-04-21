def arithmetic_arranger(problems, con = False):
  # This checks the number of input problem
  if len(problems) > 5 :
    return('Error: Too many problems.')

  # Initialization of lists, strings
  f_oper = list()
  s_oper = list()
  opera = list()
  res = list()
  fline = str()
  sline = str()
  tline = str()
  aline = str()


  # Spliting the operands in the problems  
  for problem in problems:
    problem.lstrip()
    problem.rstrip()
    sproblem = problem.split(" ")
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
      return('Error: Numbers cannot be more than four digits.')
    if not (sproblem[1] == '+' or sproblem[1] == '-'):
      return('Error: Operator must be \'+\' or \'-\'.') 
    f_oper.append(sproblem[0])
    opera.append(sproblem[1])
    s_oper.append(sproblem[2])

  # The arithmetic operations
  counter = 0
  while counter < len(problems):
    try:
      a = int(f_oper[counter])
      b = int(s_oper[counter])
    except:
      return('Error: Numbers must only contain digits.')
    if opera[counter] == '+':
      res.append(str(a + b))
    elif opera[counter] == '-':
      res.append(str(a - b))
    
    # Finding the width of longest operand
    long = max(len(f_oper[counter]), len(s_oper[counter]))

    # Creation of first line
    for val in range((long + 2) - len(f_oper[counter])):
      f_oper[counter] = ' ' + f_oper[counter]
    fline = fline + f_oper[counter] + '    '

    # Creation of second line
    for val in range((long + 1)- len(s_oper[counter])):
      s_oper[counter] = ' ' + s_oper[counter]
    sline = sline + opera[counter] + s_oper[counter] + '    '

    # Creation of third line
    for val in range(long + 2):
      tline = tline + '-'
    tline = tline + '    '

    # Creation of fourth line
    for val in range((long + 2) - len(res[counter])):
      res[counter] = ' ' + res[counter]
    aline = aline + res[counter] + '    '

    counter = counter + 1

  # Final output
  fline = fline.rstrip()
  sline = sline.rstrip()
  tline = tline.rstrip()
  aline = aline.rstrip()
  if con == False:
    arranged_problems = fline + '\n' + sline + '\n' + tline
  elif con == True:
    arranged_problems = fline + '\n' + sline + '\n' + tline + '\n' + aline
  
  return arranged_problems