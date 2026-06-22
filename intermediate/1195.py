from io import StringIO
import sys

_input = """2
3
5 2 7
9
8 3 10 14 6 4 13 7 1
"""

sys.stdin = StringIO(_input)

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def insert(tree, num):
  new_node = Node(num)
  
  if tree is None:
    return new_node
  
  aux = tree
  while True:
    if num < aux.val:
      if aux.left is None:
        aux.left = new_node
        break
      aux = aux.left
    else:
      if aux.right is None:
        aux.right = new_node
        break
      aux = aux.right

  return tree

def pre_order(tree, values):
  if tree is None: 
    return []
  
  values.append(tree.val)
  pre_order(tree.left, values)
  pre_order(tree.right, values)

  return values

def in_order(tree, values):
  if tree is None: 
    return []
  
  in_order(tree.left, values)
  values.append(tree.val)
  in_order(tree.right, values)

  return values

def post_order(tree, values):
  if tree is None: 
    return []
  
  post_order(tree.left, values)
  post_order(tree.right, values)
  values.append(tree.val)

  return values

test_cases = int(input())

for i in range(1, test_cases+1):
  _ = int(input())
  numbers = [int(item) for item in input().split()]
  
  tree = None

  for num in numbers:
    tree = insert(tree, num)

  print(f"Case {i}:")
  print(f"Pre.: {' '.join([str(item) for item in pre_order(tree, [])])}")
  print(f"In..: {' '.join([str(item) for item in in_order(tree, [])])}")
  print(f"Post: {' '.join([str(item) for item in post_order(tree, [])])}")
  print()