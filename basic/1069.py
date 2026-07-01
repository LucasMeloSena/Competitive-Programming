import sys
from io import StringIO

_input = """2
<..><.<..>>
<<<..<......<<<<....>"""

sys.stdin = StringIO(_input)

test_cases = int(input())

for _ in range(test_cases):
  chars = input()
  stack = []
  diamonds = 0

  for char in chars:
    if char == '<':
      stack.append(char)
    if len(stack) and char == '>':
      stack.pop()
      diamonds += 1

  print(diamonds)