def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while (i * i) <= n:  # Check up to √n
        if n % i == 0:
            return False
        i += 2  # Skip even numbers

    return True

print(is_prime(7919))