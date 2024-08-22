import matplotlib.pyplot as plt
from scipy import stats

# with open("oily_bright.txt") as f:
#         x= []
#         for i in f:
#             x.append(float(i.strip('\n')))
# f.close()
# with open("oily_img_bright.txt") as f:
#         y= []
#         for i in f:
#             y.append(float(i.strip('\n')))
# f.close()
x=[49.175, 25.65, 35.01, 36.24, 58.31]
y=[53.35,59.65,38.4,41.56,46.17]
print(x,y)
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
