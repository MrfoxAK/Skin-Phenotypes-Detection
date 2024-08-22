from asyncore import write
from cgitb import text


def median(text1):
    sum=0
    with open(text1) as f:
        l = []
        for i in f:
            l.append(i.strip('\n'))
    l.sort()
    size = len(l)
    index = int(((size+1)/2)-1)
    f=open(text1,"a")
    a = f.write(f"{l[index]}\n")
    f.close()

def mean(text):
    sum=0
    with open(text) as f:
        l = []
        for i in f:
            l.append(i.strip('\n'))
    for i in range(0,len(l)-1):
        sum=sum+int(l[i])
    m=sum/len(l)
    f=open(text,"a") 
    a = f.write(f"{m}\n")
    f.close()

mean("dry.txt")