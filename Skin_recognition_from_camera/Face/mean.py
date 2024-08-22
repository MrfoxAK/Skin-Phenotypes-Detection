from asyncore import write
from cgitb import text
from re import X
import statistics


def mean(text):
    sum=0
    with open(text) as f:
        l = []
        for i in f:
            l.append(float(i.strip('\n')))
    # for i in range(0,len(l)-1):
    #     sum=sum+float(l[i])
    # m=sum/len(l)
    m=statistics.mean(l)
    f=open(text,"w") 
    f.write(f"{m}\n")
    print("mean",m)
    f.close()
