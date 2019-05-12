from primenumbers import isprime
import time
starting = time.time()

def fleft(n):
    while len(n) >= 1:
        if isprime(int(n)):
            return fleft(n[1:])
        else: return False
    return True
def fright(n):
    while len(n) >= 1:
        if isprime(int(n)):
            return fright(n[:-1])
        else: return False
    return True

total = 0
counter = 0
number = 13
while counter != 11:
    if isprime(number):
        if bool(fleft(str(number))):
            if bool(fright(str(number))):
                total += number
                counter += 1

    number += 1

print(total)



elapsed = time.time() - starting
print(elapsed)
