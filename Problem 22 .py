import string
import time
beginning = time.time()

alphabet = string.ascii_uppercase

def func_word(n):
    t = 0
    for i in n:
        t += (alphabet.index(i)+1)        #Index starts with 0,not 1
    return t

total = 0
with open("Dosyalar.txt","r") as file:
    content = (file.read()).split(",")
    content.sort()
    for i in content:
        result = (func_word(i[1:-1])) * (content.index(i) + 1)
        total += result

print(total)

elapsed = time.time()-beginning
print("elapsed time  :",elapsed)
