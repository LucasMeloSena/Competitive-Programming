import math

test_cases = int(input())

for _ in range(test_cases):
  values = [int(item) for item in input().split()]
  greater_divider = math.gcd(values[0],values[1])
  print(greater_divider)