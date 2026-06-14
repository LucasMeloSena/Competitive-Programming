def eh_primo(n):
  if n <= 2:
    return True

  i = 3
  while i * i < n: # Indo até √n
    if n % i == 0:
      return False
    i += 2 # Pulando números pares
    
  return True
  
print(eh_primo(7919))