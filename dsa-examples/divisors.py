from collections import Counter

def prime_factorization(n):
    d = 2
    factors = []

    while n > 1:
        # Prime factorization:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    counter = Counter(factors)
    return counter

def divisors(n):
    factors = prime_factorization(n)
    divisors_list = [1]

    for factor, exponent in factors.items():
        aux = []
        for num in divisors_list:
            for i in range(1, exponent + 1):
                new_divisor = num * (factor ** i)
                aux.append(new_divisor)

        divisors_list.extend(aux)

    divisors_list.sort()
    return divisors_list

def number_of_divisors(n):
    factors = prime_factorization(n)
    total = 1

    for exponent in factors.values():
        total *= (exponent + 1)

    return total

def gcd(n1, n2):
    factors1 = prime_factorization(n1)
    factors2 = prime_factorization(n2)

    common_factors = factors1.keys() & factors2.keys()

    total = 1
    for factor in common_factors:
        total *= factor

    return total

def lcm(n1, n2):
    _gcd = gcd(n1, n2)
    return abs(n1 * n2) / _gcd

# print(f"GCD: {gcd(150, 120)}")  # or math.gcd(150, 120)
# print(f"LCM: {lcm(150, 120)}")  # or math.lcm(150, 120)
# print(f"Number of divisors of {144000}: {number_of_divisors(144000)}")
print(divisors(60))