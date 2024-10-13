def get_prime_factors(N: int) -> list:
    """Return a list of all prime factors in N."""
    factors = []
    
    # Check for number of 2s that divide N
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    # look in the range from 3 to sqrt(N) and skip evens
    for i in range(3, int(N**0.5) + 1, 2):
        # While i divides N, add i and divide N
        while N % i == 0:
            factors.append(i)
            N //= i

    # If N is a prime number greater than 2, then add it to the list
    if N > 2:
        factors.append(N)

    return factors