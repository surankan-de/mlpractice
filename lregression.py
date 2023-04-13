import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#general y=x**2
x = [1,2,3,4,5]
y = [1,4,9,16,25]

m =0
b=0

#declaring cost and exp
def exp(m,x,b):
    return m*x*x+b

def c(a,b):
    sum =0
    for i in range(0,len(a),1):
        sum+=(a[i]-b[i])**2

    return sum/len(a)
res =[]
for i in range(0,len(x),1):
    res.append(exp(m,x[i],b))

costs = []
cost = c(res,y)
costs.append(cost)


for i in range(201):
    dm=0
    db =0
    for j in range(len(x)):
        dm+=0.01*((res[j]-y[j])*x[j])/len(x)
        db+=0.01*((res[j]-y[j]))/len(x)
    m-=dm
    b-=db

    for j in range(len(res)):
        res[j] = exp(m,x[j],b)

    cost = c(res,y)
    costs.append(cost)
    
plt.scatter([i for i in range(202)],costs)
plt.show()
print(res)






