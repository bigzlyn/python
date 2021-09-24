# 线性回归
import numpy as np

# 载入线性回归模型
from sklearn.linear_model import LinearRegression

# 载入波士顿房价数据
from sklearn.datasets import load_boston

# 读入数据
boston = load_boston()

# 拆分数据集,拆分
# data = np.array(boston['data'])
# x = data[0::, 19]
# x = np.array(boston['data'])
x = boston['data']
print(x)

y = boston['target']
names = boston['feature_names']

# 拆分训练计集和测试集
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# 训练线性回归模型, fit=拟合, 修改参数
# model = LinearRegression(normalize=True, copy_X=True, n_jobs=1, positive=True).fit(x_train, y_train, sample_weight=0.5)
model = LinearRegression().fit(x_train, y_train)

# 模型评价
y_pred = model.predict(x_test)

import matplotlib.pyplot as plt

plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=0.5, linestyle='-')
plt.plot(range(y_pred.shape[0]), y_pred, color="red", linewidth=0.5, linestyle='-')
plt.legend(['test', 'pred'])

plt.show()
