# 客户数据分析
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 文件导入
file_path = "./resource/客户数据-all.xlsx"
df = pd.read_excel(file_path)
print(df)

df2 = df.head(10)
print(df2)
df.info()

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})


print(df)
print(df.head(1))
print(df.tail(3))



