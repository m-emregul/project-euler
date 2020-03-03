
import time
baslangıc = time.time()

dizi = [1,2,5,10,20,50,100,200]
n = 8
toplam = 200
count = 0

def func(dizi,i, n, toplam):
    if toplam == 0:
        global count
        count = count + 1
        return

    elif toplam < 0:
        return

    for j in range(i,n):
        func(dizi, j, n, toplam-dizi[j])

func(dizi,0,n,toplam)
print(count)

bitis = time.time()
print("elapsed time : ", bitis - baslangıc)
