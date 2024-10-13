# mathlib/series.py

def sum_integers(N:int, m:int=1, start:int=1) -> int:
    """
    Sum integers from start to N.

    Parameters:
    - N: the largest integer in the summation series
    - m: multiple of integers to sum (default: 1)
    - start: the smallest integer in the summation series (default: 1)
    """
    if m <= 0:
        raise ValueError("m must be greater than 0.")
    elif N < 0:
        raise ValueError("N must be greater than 0")
    elif start < 1:
        raise ValueError("start must be greater than 0")

    n = m * (N // m)
    s = m * ((start-1) // m)
    return (n * (n+m))//(2*m) - (s * (s+m))//(2*m)

def get_fibonacci(n:int=None, n_start:int=0, max:int=None) -> list:
    """Generate the fibonnaci sequence.
     
    If n has a value, the sequence is produces up to Fn, where
    Fn = F_n-1 + F_n-2
    
    Otherwise, if max has a value, the sequence is produced until
    Fn < max.
    """
    
    # check inputs
    if n and not isinstance(n, int):
        raise ValueError(f"n must be an integer received: {n} [{type(n)}]")
    if not isinstance(n_start, int):
        raise ValueError(f"n_start must be an integer received: {n_start} [{type(n_start)}]")
    if max and not isinstance(max, int):
        raise ValueError(f"max must be an integer received: {max} [{type(max)}]")
    if n and n_start > n:
        raise ValueError(f"n_start ({n_start}) must be greater than n ({n})")

    seq = [0,1]

    if n:
        for i in range(1,n):
            seq.append(seq[i] + seq[i-1])
    elif max:
        while (seq[-1] + seq[-2]) < max:
            seq.append(seq[-1] + seq[-2])
    else:
        raise ValueError(f"Did not receive a value for n or max.")
    
    return seq[n_start:]