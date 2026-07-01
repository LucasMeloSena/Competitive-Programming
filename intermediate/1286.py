from io import StringIO
import sys

_input = """6
10
15 5
23 4
21 2
16 4
19 5
18 2
0"""

sys.stdin = StringIO(_input)

def knapsack(max_capacity, values, weights, n):
  dp = [[0 for _ in range(max_capacity+1)] for _ in range(n+1)]

  for i in range(1,n+1):
    weight = weights[i-1]
    value = values[i-1]

    for j in range(max_capacity+1):
      dp[i][j] = dp[i-1][j]

      if j >= weight:
        dp[i][j] = max(dp[i][j], dp[i-1][j-weight] + value)

  return dp[n][max_capacity]

while True:
  n = int(input())
  if n == 0:
    break

  max_capacity = int(input())
  values = []
  weights = []

  for _ in range(n): 
    value, weight = [int(item) for item in input().split()]
    values.append(value)
    weights.append(weight)

  res = knapsack(max_capacity, values, weights, n)
  print(f"{res} min.")