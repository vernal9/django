import numpy as np # 引入NumPy
import matplotlib.pyplot as plt # 引入matplotlib的函數

x = np.arange(20) # x軸的值
y1 = 3 * x + 1  # y軸的值
y2 = -3 * x + 20  # y軸的值

plt.title("add legend") # 圖的標題
plt.xlabel("x axis") # x軸的名稱
plt.ylabel("y axis") # y軸的名稱
plt.plot(x,y1, color = "red", label = "y1") # 繪製x,y1的圖
plt.plot(x,y2, ls = "--", label = "y2") # 繪製x,y2的圖
plt.legend(loc = 0, prop={'size': "x-large"})
plt.show() # 顯現圖形