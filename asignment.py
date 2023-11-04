# 1) Difference between a list and a tuple ?
# li= [1,2,3,4,5,6,7,8,9,10]
# print(li)
# output of the li [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# li[5] = 50
# print(li)
# print(type(li))   # <class 'list'>
# output of the muteable li [1, 2, 3, 4, 5, 50, 7, 8, 9, 10]
# tuple
# tup=(1,2,3,4,5,6,7,8)
# print(tup)
# print(type(tup))     #<class 'tuple'>
# output of tup (1, 2, 3, 4, 5, 6, 7, 8)
# tup[2]= 10
# print(tup)
# output after add element of tuple 
# TypeError: 'tuple' object does not support item assignment

#--------------------------------------------------
#2) How would you filter the expiry from the
# following pandas Series and get a new series of dtype Date Time ?

# import pandas as pd

# data = pd.Series([
#     'BANKNIFTY03MAR2230900PE.NFO',
#     'BANKNIFTY10MAR2230900PE.NFO',
#     'NIFTY17JUN2316900CE.NFO',
#     'TATACHEM25FEB21500CE.NFO',
#     'ACC25MAR221800CE.NFO'
# ])
# find = r'(\d{2}[A-Z]{3}\d{2})'
# expiry_dates = data.str.extract(find, expand=False)
# df = pd.to_datetime(expiry_dates)
# print(df)
# output of the code ------------>
# 0   2022-03-03
# 1   2022-03-10
# 2   2023-06-17
# 3   2021-02-25
# 4   2022-03-25
