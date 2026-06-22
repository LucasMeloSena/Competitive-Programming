import sys
from io import StringIO
  
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

    if n == 0:
        break

    for i in range(n):
        line = []

        for j in range(n):
            value = min(i, j, n - 1 - i, n - 1 - j) + 1
            line.append(f"{value:3}")

        print(" ".join(line))

    print()