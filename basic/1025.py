import sys
from io import StringIO
from bisect import bisect_left

_input = """4 1
2
3
5
1
5
5 2
1
3
3
3
1
2
3
0 0
"""

sys.stdin = StringIO(_input)

def binary_search(nums, target):
  left = 0
  right = len(nums) - 1
  occurrence = -1

  while left <= right:
    middle = (left+right) // 2
    
    if nums[middle] == target:
      occurrence = middle
      right = middle - 1
    elif target > nums[middle]:
      left = middle + 1
    else:
      right = middle - 1

  return occurrence

count = 1

while True:
  n, q = [int(item) for item in input().split()]
  if n == 0 and q == 0:
    break

  print(f"CASE# {count}:")
  
  marbles = [int(input()) for _ in range(n)]
  queries = [int(input()) for _ in range(q)]

  marbles.sort()

  for query in queries:
    # index = bisect_left(marbles, query)
    index = binary_search(marbles, query)
    #if index < len(marbles) and marbles[index] == query:
    if index != -1:
      print(f"{query} found at {index+1}")
    else:
      print(f"{query} not found")

  count += 1