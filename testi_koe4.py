def is_prime(number):
    number = 600
    if number < 2:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

print(is_prime(1))
