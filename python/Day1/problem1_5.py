# 1. 引入pandas并查看版本
import pandas as pd
from pandas import Series
# pd.show_versions()
# print(pd.__version__)

# 2.头尾拼接两个series
ser1 = Series([1,2,3,4], index = ['a','b','c','d'])
ser2 = Series([5,6,3,8], index = ['e','f','g','h'])

ser = pd.concat([ser1,ser2], axis = 0)
print(ser)

# 3. 找到元素在seriesA中不在seriesB中
print(ser1[~ser1.isin(ser2)])