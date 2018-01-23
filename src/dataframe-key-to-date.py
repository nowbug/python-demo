#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Nowbug 
@license: Teld Licence  
@contact: xuluda@163.com 
@site: https://nowbug.github.io 
@software: PyCharm 
@file: dataframe-key-to-date.py 
@time: 2018/1/22 18:34
将一个elxce 里面的key作为日期并可以根据日期来计算数据（求和等）
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
# # ---其中parse_dates 表明选择数据中的哪个column作为date-time信息，
# # ---index_col 告诉pandas以哪个column作为 index
# # --- date_parser 使用一个function(本文用lambda表达式代替)，使一个string转换为一个datetime变量
#
data = pd.read_excel('../data/day.xls', parse_dates=['bizdate'], index_col='bizdate', date_parser=dateparse)
Electricity = []
listy = ['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10',
         '2017-11', '2017-12']
for i in listy:
    Electricity.append(data[i]['totalpower'].sum())
print Electricity
