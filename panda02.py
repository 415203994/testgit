#coding=utf-8
import pandas as pd
import numpy as np
index = pd.Index(data=["Tom", "Bob", "Mary", "James"], name="name") # name为索引名字

data = {
    "age": [18, 30, 25, 40],
    "city": ["BeiJing", "ShangHai", "GuangZhou", "ShenZhen"]
}

user_info = pd.DataFrame(data=data, index=index)
#print user_info

# 切片
d = user_info.iloc[:,:-1]
# 筛选
f = user_info[user_info.city=="BeiJing"]

