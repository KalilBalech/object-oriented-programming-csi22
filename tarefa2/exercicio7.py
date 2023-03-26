import itertools

def primeNumbers():
    yield 2
    prime_num = [2]

    for x in itertools.count(3, 2):
        is_prime = True

        for primeNum in prime_num:
            if x % primeNum == 0:
                is_prime = False
        
        if is_prime:
            prime_num.append(x)
            yield x

# for primeNum in primeNumbers():
#     print(primeNum)
#     if primeNum > 100:
#         break