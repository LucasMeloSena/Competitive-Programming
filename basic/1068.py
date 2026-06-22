while True:
  try:
    data = input()
    stack = []

    for char in data:
      if char == '(' or char == ')':
        if char == ')':
          stack.pop()
        else:
          stack.append(char)

    if stack:
      print('incorrect')
    else:
      print('correct')
  except EOFError:
    break
  except IndexError:
    print('incorrect')