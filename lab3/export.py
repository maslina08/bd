#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cx_Oracle
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import pandas_oracle.tools as pt

connection = cx_Oracle.connect('SYS/s@localhost', mode=cx_Oracle.SYSDBA)


# In[5]:


query1 = "select * from athletes"
df1 = pt.query_to_df(query1, connection)
query2 = "select * from events"
df2 = pt.query_to_df(query2, connection)
query3 = "select * from countries"
df3 = pt.query_to_df(query3, connection)


# In[6]:


df1.to_csv('athletes.csv')
df2.to_csv('events.csv')
df3.to_csv('countries.csv')


# In[ ]:




