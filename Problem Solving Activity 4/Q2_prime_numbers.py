def generate_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if number < 2:
            continue
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


print(generate_primes(1, 30))
print(generate_primes(2, 2))
print(generate_primes(14, 16))
print(generate_primes(9, 9))  # Extra edge case
