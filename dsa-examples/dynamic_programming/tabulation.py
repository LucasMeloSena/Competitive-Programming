def fib(n):
  table = [0 for _ in range(n+1)]
  table[1] = 1

  for i in range(0, n+1):
    if i + 1 <= len(table) - 1:
      table[i+1] += table[i]
    if i + 2 <= len(table) - 1:
      table[i+2] += table[i]

  return table[n]

print(f"Fib: {fib(6)}")
print(f"Fib: {fib(50)}\n")

def grid_traveler(i, j):
  i += 1
  j += 1
  table = [[0 for _ in range(i)] for _ in range(j)]
  table[1][1] = 1

  for m in range(i):
    row_in_bounds = m + 1 <= (len(table) - 1)
    for n in range(j):
      col_in_bounds = n + 1 <= (len(table[0]) - 1)
      if row_in_bounds:
        table[m+1][n] += table[m][n]
      if col_in_bounds:
        table[m][n+1] += table[m][n]

  print("\n".join(str(row) for row in table))
  return table[i-1][j-1]

print(f"Grid traveler: {grid_traveler(3,3)}\n")

def can_sum(target_value, nums):
  arr = [False for _ in range(target_value + 1)]
  arr[0] = True

  for index, _ in enumerate(arr):
    if arr[index]:
      for _, num in enumerate(nums):
        new_index = index + num
        index_in_bounds = (new_index) < len(arr)
        if index_in_bounds:
          arr[new_index] = True

  return arr[target_value]

print(f"Can sum? {can_sum(7, [2,3])}")
print(f"Can sum? {can_sum(7, [5,3,4,7])}")
print(f"Can sum? {can_sum(7, [2,4])}")
print(f"Can sum? {can_sum(7, [2,3,5])}")
print(f"Can sum? {can_sum(300, [7,14])}\n")

def how_sum(target_value, nums):
  arr = [None for _ in range(target_value+1)]
  arr[0] = []
  
  for index, _ in enumerate(arr):
    if arr[index] != None:
      for _, num in enumerate(nums):
        new_index = index + num
        index_in_bounds = new_index < len(arr)
        if index_in_bounds:
          arr[new_index] = arr[index] + [num] if arr[index] != None else [num]

  return arr[target_value]

print(f"How sum: {how_sum(7, [2,3])}")
print(f"How sum: {how_sum(7, [5,3,4,7])}")
print(f"How sum: {how_sum(7, [2,4])}")
print(f"How sum: {how_sum(8, [2,3,5])}")
print(f"How sum: {how_sum(300, [7,14])}\n")

def best_sum(target_value, nums):
  arr = [None for _ in range(target_value+1)]
  arr[0] = []
  
  for index, _ in enumerate(arr):
    if arr[index] != None:
      for _, num in enumerate(nums):
        new_index = index + num
        index_in_bounds = new_index < len(arr)
        if index_in_bounds:
          new_array = arr[index] + [num] if arr[index] != None else [num]

          if not arr[new_index] or len(new_array) < len(arr[new_index]):
            arr[new_index] = new_array
            
  return arr[target_value]

print(f"Best sum: {best_sum(7, [5,3,4,7])}")
print(f"Best sum: {best_sum(8, [2,3,5])}")
print(f"Best sum: {best_sum(8, [1,4,5])}")
print(f"Best sum: {best_sum(100, [1,2,5,25])}")