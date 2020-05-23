#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
from mysql.connector import Error
import pandas as pd

def connect():
    Host='localhost'
    Database='medals'
    User='root'
    Password=''
    try:
        global conn
        conn=mysql.connector.connect(host=Host,database=Database,user=User,password=Password)
        if conn.is_connected():
            print('Connected to MySQL database')
            
    except Error as e:
        print(e)

if __name__ == '__main__':
    connect()


# In[2]:


pd.read_sql("select nationality, count(*) as 'count of athletes' from athletes group by nationality;", con=conn)


# In[3]:


pd.read_sql("select nationality, sum(athletes.gold) as 'count of gold medals', sum(athletes.silver) as 'count of silver medals' from athletes group by nationality;", con=conn)


# In[4]:


pd.read_sql("select sport, sex, sum(athletes.gold) as 'count of gold medals', sum(athletes.silver) as 'count of silver medals' from athletes group by sport, sex", con=conn)


# In[5]:


conn.close()


# In[ ]:




