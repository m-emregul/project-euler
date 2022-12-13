import time
beginning = time.time()

def g(n):
    s = 0
    for i in str(n):
        s += int(i) ** 2
    return s

def func(n):
    global nums
    global count
    if n in ones:
        ones.update(nums)
        nums.clear()
        return False
    elif n in eightynines:
        eightynines.update(nums)
        nums.clear()
        return True
    else:
        nums.add(n)
        m = g(n)
        return func(m)

nums = set()
ones = set()
eightynines = set()
ones.add(1)
eightynines.add(89)

for i in range(2,1000000):
    func(i)

print(len(eightynines))   #this gives the result
print(len(ones))  

end = time.time()
print("elapsed time   :", end-beginning)
