# import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets,linear_model


houseprice = [245,312,279,308,199,219,404,324,319,255]
size = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]
print(size)


size2 = np.array(size).reshape(-1,1)
print(size2)

regr = linear_model.LinearRegression()
regr.fit(size2,houseprice)

print("Coefficoent" , regr.coef_)
print("Intercept" , regr.intercept_)

def graph(formula,x_range ): 
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)


graph('regr.coef_*x + regr.intercept_', range(1000,2700))
plt.scatter(size,houseprice,color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
plt.show()
