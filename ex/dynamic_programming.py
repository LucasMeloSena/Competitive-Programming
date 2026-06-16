def fibo(n, memo):
  if n in memo: return memo[n]
  if n <= 2: return 1
  memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
  return memo[n]

n = fibo(50, {})
print(f"Fibonacci number at position 50: {n}")

def grid_traveler(i, j, memo={}):
  if (i,j) in memo: return memo[(i,j)]

  if i == 1 and j == 1: return 1
  if i == 0 or j == 0: return 0

  memo[(i,j)] = grid_traveler(i-1,j,memo) + grid_traveler(i,j-1,memo)
  return memo[(i,j)]

print(f"Different ways to travel a matrix of 18x18: {grid_traveler(18,18)}")

def can_sum(target_value, nums, memo={}):
  if target_value in memo: return memo[target_value]
  if target_value == 0: return True
  if target_value < 0: return False

  for num in nums:
    remainder = target_value - num
    if can_sum(remainder, nums, memo):
      memo[target_value] = True
      return True
  
  memo[target_value] = False
  return False

res = can_sum(7, [5,3,4,7])
print(f"Is it possible to sum? {res}")

def how_sum(target_value, nums, memo):
  if target_value in memo: return memo[target_value]
  if target_value == 0: return []
  if target_value < 0: return None

  for num in nums:
    remainder = target_value - num
    remainder_result = how_sum(remainder, nums, memo)
    if remainder_result != None:
      combination = remainder_result + [num]
      memo[target_value] = combination
      return memo[target_value]
  
  memo[target_value] = None
  return memo[target_value]

print(f"How sum: {how_sum(7, [5,3,4,7], {})}")
print(f"How sum: {how_sum(8, [2], {})}")
print(f"How sum: {how_sum(300, [7,14], {})}")