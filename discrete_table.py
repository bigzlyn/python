# 离散表
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x3_1 = np.array(["2014", "2015", "2016", "2017", "2018"])
y3_1 = np.array([11659.3, 19643.3, 14429.3, 3129.3, 13219.3])

plt.scatter(x3_1, y3_1)
plt.xlabel("年份", fontsize=15)
plt.ylabel("人数(万人次)", fontsize=15)
plt.title("出境游客", fontsize=20)
plt.show()
