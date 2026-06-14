import sys
from io import StringIO
import math

_input = """3 4 5
6 8 10
5 13 12
4 5 6"""

sys.stdin = StringIO(_input)

while True:
  try:
    values = [int(item) for item in input().split()]
    condition_1 = math.pow(values[0], 2) == math.pow(values[1], 2) + math.pow(values[2], 2)
    condition_2 = math.pow(values[1], 2) == math.pow(values[0], 2) + math.pow(values[2], 2)
    condition_3 = math.pow(values[2], 2) == math.pow(values[0], 2) + math.pow(values[1], 2)
    if condition_1 or condition_2 or condition_3:
      if math.gcd(values[0], values[1], values[2]) == 1:
        print("tripla pitagorica primitiva")
      else:
        print("tripla pitagorica")
    else:
      print("tripla")
  except EOFError:
    break