from io import StringIO
import sys

_input = """1
2
3
4
5
0
"""

sys.stdin = StringIO(_input)

while True:
  n = int(input())
  array = [[0 for _ in range(n)] for _ in range(n)]
  
  if n == 0:
    break
  
  for row in range(n):
    for col in range(n):
      if row == 0 and col == 0: 
        array[row][col] = 1
      elif row == 0:
        prev = array[row][col-1]
        new = prev * 2
        array[row][col] = new
      else:
        prev = array[row-1][col]
        new = prev * 2
        array[row][col] = new

  biggest = array[n-1][n-1]
  biggest_size = len(str(biggest))
  
  for i in range(n):
    print(" ".join([f"{item:{biggest_size}}" for item in array[i]]))
  print()