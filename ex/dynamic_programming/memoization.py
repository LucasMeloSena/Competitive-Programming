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

def best_sum(target_value, nums, memo):
  if target_value in memo: return memo[target_value]
  if target_value == 0: return []
  if target_value < 0: return None

  shortest_combination = None

  for num in nums:
    remainder = target_value - num
    remainder_result = best_sum(remainder, nums, memo)
    if remainder_result != None:
      combination = remainder_result + [num]
      if not shortest_combination or len(combination) < len(shortest_combination):
        shortest_combination = combination

  memo[target_value] = shortest_combination
  return memo[target_value]

print(f"Best sum: {best_sum(7, [5,3,4,7], {})}")
print(f"Best sum: {best_sum(300, [7,14], {})}")

def can_construct(target: str, word_bank, memo):
  if target in memo: 
    return memo[target]
  if target == '': 
    return True

  for word in word_bank:
    remainder = target.removeprefix(word)
    if remainder == target: 
      continue
    if can_construct(remainder, word_bank, memo):
      memo[target] = True
      return True
    
  memo[target] = False
  return False

print(f"Can Construct? {can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {})}")
print(f"Can Construct? {can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})}")
print(f"Can Construct? {can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {})}")
print(f"Can Construct? {can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'eeeee', 'eeeeeeeeeeee'], {})}")

def count_construct(target: str, word_bank, memo):
  if target in memo:
    return memo[target]
  if target == '':
    return 1
  
  count = 0
  for word in word_bank:
    remainder = target.removeprefix(word)
    if target == remainder:
      continue
    count += count_construct(remainder, word_bank, memo)

  memo[target] = count
  return count
  
print(f"Count Construct: {count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {})}")
print(f"Count Construct: {count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})}")
print(f"Count Construct: {count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {})}")
print(f"Count Construct: {count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'eeeee', 'eeeeeeeeeeee'], {})}")
print(f"Count Construct: {count_construct('aaaa', ['a', 'aa'], {})}")

def all_construct(target: str, word_bank, memo):
  if target in memo:
    return memo[target]
  if target == '':
    return [[]]
  
  res = []

  for word in word_bank:
    if target.startswith(word):
      remainder = target.removeprefix(word)
      remainder_result = all_construct(remainder, word_bank, memo)
      if remainder_result:
        new = [item + [word] for item in remainder_result]
        res.extend(new)
  
  memo[target] = res
  return memo[target]

print(f"All Construct: {all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {})}")
print(f"All Construct: {all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})}")
print(f"All Construct: {all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {})}")
print(f"All Construct: {all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'eeeee', 'eeeeeeeeeeee'], {})}")
print(f"All Construct: {all_construct('aaaa', ['a', 'aa'], {})}")