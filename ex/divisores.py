from collections import Counter

def fatoracao(n):
  num = n
  d = 2
  fatores = []
  
  while n > 1:
    # Fatoração prima:
    while n % d == 0:
      fatores.append(d)
      n //= d
    d += 1
    
  counter = Counter(fatores)
  return counter

def divisores(n):
  fatores = fatoracao(n)
  dividers = [1]
    
  for fator, expoente in fatores.items():
        aux = [] 
        for num in dividers:
            for i in range(1, expoente + 1):
                novo_divisor = num * (fator ** i)
                aux.append(novo_divisor)
                
        dividers.extend(aux)
        
  dividers.sort()
  return dividers

def qtde_divisores(n):
    fatores = fatoracao(n)
    total = 1
    for expoente in fatores.values():
      total *= (expoente + 1)
    return total
    
def mdc(n1, n2):
  fatores1 = fatoracao(n1)
  fatores2 = fatoracao(n2)
  fatores_comuns = fatores1.keys() & fatores2.keys()
  total = 1
  for i in fatores_comuns:
    total *= i
  return total

def mmc(n1, n2):
  _mdc = mdc(n1, n2)
  return abs(n1 * n2) / _mdc
    
# print(f"MDC: {mdc(150, 120)}") # or math.gcd(150,120)
# print(f"MMC: {mmc(150, 120)}") # or math.lcm(150,120)
# print(f"Quantidade de divisores do número {144000}: {qtde_divisores(144000)}")
print(divisores(60))