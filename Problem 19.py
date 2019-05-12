import datetime
import time
beginning = time.time()

total = 0
for i in range(1901,2001):
    for j in range(1,13):
        d = datetime.date(i,j,1)
        if d.weekday() == 6:
            total += 1
print(total)




elapsed = time.time()-beginning            
print("elapsed time  :",elapsed)

#171
#elapsed time  : 0.0005002021789550781
