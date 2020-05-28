#!/usr/bin/env python
# coding: utf-8

# In[125]:


import cx_Oracle
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import pandas_oracle.tools as pt
import datetime
import numpy 
connection = cx_Oracle.connect('SYS/s@localhost', mode=cx_Oracle.SYSDBA)
cursor = connection.cursor()
def InConverter(value):
    return int(value)

def InputTypeHandler(cursor, value, num_elements):
    if isinstance(value, numpy.int64):
        return cursor.var(int, arraysize=num_elements, inconverter=InConverter)

cursor.inputtypehandler = InputTypeHandler

df = pd.read_csv('C:/Users/Roma/Desktop/medals/athletes.csv')
fmt = '%m/%d/%Y'
query="""
INSERT INTO ATHLETES (id, name, nationality, sex, dob, height, weight, sport ,gold,silver)
VALUES (:id, :name, :nationality, :sex, :dob, :height, :weight, :sport, :gold, :silver)"""
for i in range(len(df['id'])):
    try:
        try:
            cursor.execute(query, id = df['id'][i], name=df['name'][i], nationality=df['nationality'][i], sex=df['sex'][i], dob=datetime.datetime.strptime(df['dob'][i], fmt), height=df['height'][i], weight=df['weight'][i], sport=df['sport'][i] ,gold=df['gold'][i], silver=df['silver'][i])
        except:
            date = df['dob'][i].split('/')
            dd = date[0]+'/'+date[1]+'/'+'19'+date[2]
            cursor.execute(query, id = df['id'][i]+10000, name=df['name'][i], nationality=df['nationality'][i], sex=df['sex'][i], dob=datetime.datetime.strptime(dd, fmt), height=df['height'][i], weight=df['weight'][i], sport=df['sport'][i] ,gold=df['gold'][i], silver=df['silver'][i])
    except:
        pass

