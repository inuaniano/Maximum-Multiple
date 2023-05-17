def max_divisible(divisor, bound):
    # Start from the bound and decrement by 1
    for num in range(bound, 0, -1):
        # Check if the number is divisible by the divisor
        if num % divisor == 0:
            return num

    # If no number is found, return None or an appropriate value
    return None
