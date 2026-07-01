import sys
from io import StringIO
import math

_input = """4
123321
123
103
1000000007
"""

sys.stdin = StringIO(_input)

test_cases = int(input())

def is_prime(n):
  if n == 2:
    return True
  
  num = 3
  while num < math.sqrt(n):
    if n % num == 0:
      return False
    num += 2

  return True

for _ in range(test_cases):
  n = int(input())
  if is_prime(n):
    print("Prime")
  else:
    print("Not Prime")