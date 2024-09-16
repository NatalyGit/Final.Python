# Задание 1. one hot Вячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies? 
# import random 
# lst = ['robot'] * 10 
# lst += ['human'] * 10 
# random.shuffle(lst) 
# data = pd.DataFrame({'whoAmI':lst}) 
# data.head()


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot['human'] = (data['whoAmI'] == 'human').astype(int)

# Метод astype() в pandas используется для преобразования столбцов в другой тип данных. В даннoм случае мы преобразоваем логические значения
# (True/False) в целочисленные значения (1/0).

one_hot.to_csv('csv.csv')
print(one_hot.head(20))
