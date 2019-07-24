#coding=utf-8
import pandas as pd
import numpy as np

n_data = [18, 30, 25, 40]
n_index = ["Tom", "Bob", "Mary", "James"]
user_age = pd.Series(data=n_data, index=n_index, name="user_info")
print user_age
# 获取年龄大于30的元素
print user_age[user_age>30]
# 获取第4个和第二个元素
user_age[[3, 1]]