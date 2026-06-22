import string
from io import StringIO
import sys

_input = """5
2
CBA
DDD
1
Z
6
A
B
C
D
E
F
6
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1
ZZZZZZZZZZ
"""
sys.stdin = StringIO(_input)

test_cases = int(input())
result = []

for i in range(test_cases):
    lines = int(input())
    _hash = 0
    for j in range(0,lines):
        _str = input()
        for key, char in enumerate(_str):
          alphabet_index = string.ascii_uppercase.index(char)
          _hash += alphabet_index + j + key
    result.append(_hash)
          
for num in result:
  print(num)