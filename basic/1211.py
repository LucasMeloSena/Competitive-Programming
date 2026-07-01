import sys
from io import StringIO

_input = """2
12345
12354
3
535456
535488
835456"""

sys.stdin = StringIO(_input)

while True:
  try:
    n = int(input())
    numbers = []

    for _ in range(n):
      numbers.append(input())

    numbers.sort()
    length = len(numbers[0])
    economy = 0

    for i in range(1, n):
      num1 = numbers[i-1]
      num2 = numbers[i]

      for j in range(length):
        if num1[j] == num2[j]:
          economy += 1
        else:
          break

    print(economy)
  except EOFError:
    break