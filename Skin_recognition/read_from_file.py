with open('oily.txt') as f:
    # content = f.readlines()
    l = []
    for i in f:
        l.append(int(i.strip('\n')))
l.sort()
print(l)
size = len(l)
# print(size)
# index = int(((size+1)/2)-1)
# print(l[index])
level = int(sum(l)/size)

print(level)

print("\n")

with open('dry.txt') as f:
    # content = f.readlines()
    l1 = []
    for j in f:
        l1.append(int(j.strip('\n')))
l1.sort()
print(l1)
size1 = len(l1)
# print(size)
# index1 = int(((size1+1)/2)-1)
# print(index)

level1 = int(sum(l1)/size1)

print(level1)
