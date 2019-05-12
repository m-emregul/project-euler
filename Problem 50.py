import primenumbers
import time
beginning = time.time()

primes = [x for x in range(3947) if primenumbers.isprime(x)]

aa = 0
bb = 0
def func_recur(liste):
    global aa,bb
    while len(liste) > 1:
        sum = 0
        counter = 0
        a,b = 0,0
        for i in liste:
            sum += i
            counter += 1
            if primenumbers.isprime(sum):
                a = sum
                b = counter
        if b > bb:
            aa,bb = a,b
        else: pass
        a,b,sum,counter = 0,0,0,0
        return func_recur(liste[1:])
    return None

func_recur(primes)
print(aa,bb)
print(func_recur(primes))


elapsed = time.time()-beginning
print("elapsed time  :",elapsed)
