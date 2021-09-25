# pip install tensorflow
import tensorflow as tf

# 版本为tf 2.x，但网上很多资料tf 1.x
# 跟tf 1.x 版本进行兼容
tf.compat.v1.disable_eager_execution()

import numpy as np

# 不是用TensorFlow源码安装，忽略警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 认识会话 session
# tf.Session()        #tf 1.x 写法
sess = tf.compat.v1.Session()
result = sess.run(tf.constant(1))           # 要执行tensorflow代码就要丢在sess.run()
print(result)

# 认识常量 constant
a = tf.constant(1)
print(a)

# 或者
b = 1
c = tf.constant(b)
print(c)

w = tf.Variable(np.random.rand())
print(w)

# 占位符
p = tf.compat.v1.placeholder()


######################################

# 获取张量的阶（从下面例子看到tf的计算过程）
g = tf.Graph()
# 定义一个计算图
# 上一层的输出是下一层的输入
with g.as_default():
    ## 定义张量t1,t2,t3
    t1 = tf.constant(np.pi)
    t2 = tf.constant([1, 2, 3, 4])
    t3 = tf.constant([[1, 2], [3, 4]])

    ## 获取张量的阶
    r1 = tf.rank(t1)
    r2 = tf.rank(t2)
    r3 = tf.rank(t3)

    ## 获取他们的shapes
    s1 = t1.get_shape()
    s2 = t2.get_shape()
    s3 = t3.get_shape()
    print("shapes:", s1, s2, s3)

# 启动前面定义的图来进行下一步操作
with tf.compat.v1.Session(graph=g) as sess:
    print("Ranks:", r1.eval(), r2.eval(), r3.eval())