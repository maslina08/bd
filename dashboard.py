#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
from mysql.connector import Error
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.dashboard_objs as dashboard

py.sign_in('maslina8', '0MZhNYQK7iFfngyzE015')

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId =url.split('~')
    return raw_fileId[1].replace('/', ':')


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


df1 = pd.read_sql("select nationality, count(*) as 'count of athletes' from athletes group by nationality;", con=conn)
df1 = df1.sort_values(['count of athletes'], ascending=False)
data = [go.Bar(x=df1['nationality'],y=df1['count of athletes'])]

layout = go.Layout(
    title='nationality/count of athletes',
    xaxis=dict(
        title='nationality'),
    yaxis=dict(
        title='count of athletes')
)
fig = go.Figure(data=data, layout=layout)
 
nationality_count_of_athletes = py.plot(fig, filename='my-first-graph')


# In[3]:


df2 = pd.read_sql("select nationality, sum(athletes.gold) as 'count of gold medals', sum(athletes.silver) as 'count of silver medals' from athletes where athletes.silver != 0 and athletes.gold != 0 group by nationality;", con=conn)
df2 = df2.sort_values(['count of silver medals','count of gold medals'], ascending=False)
trace1 = go.Bar(x=df2['nationality'],y=df2['count of gold medals'],name='Gold',marker=dict(color='#FFD700'))
trace2 = go.Bar(x=df2['nationality'],y=df2['count of silver medals'],name='Silver',marker=dict(color='#9EA0A1'))

data = [trace1,trace2]

layout = go.Layout(title='Medals',barmode='stack')

layout = go.Layout(
    title='Nationality/Gold and Silver medals',
    xaxis=dict(
        title='Nationality'),
    yaxis=dict(
        title='Count of medals')
)

fig = go.Figure(data=data, layout=layout)
 
nationality_count_of_silver_gold = py.plot(fig, filename='my-second-graph')


# In[4]:


df3 = pd.read_sql("select sport, sex, sum(athletes.gold) as 'count of gold medals' from athletes where sex = 'male' group by sport", con=conn)
df3 = df3.sort_values(['count of gold medals'], ascending=False)
df4 = pd.read_sql("select sport, sex, sum(athletes.gold) as 'count of gold medals' from athletes where sex = 'female' group by sport", con=conn)   
df4 = df4.sort_values(['count of gold medals'], ascending=False)   
trace1 = go.Bar(x=df3['sport'],y=df3['count of gold medals'],name='male',marker=dict(color='blue'))
trace2 = go.Bar(x=df4['sport'],y=df4['count of gold medals'],name='female',marker=dict(color='pink'))    
    

data=[trace1, trace2]

layout = go.Layout(
    title='Gold medals - male vs female',
    xaxis=dict(
        title='sport'),
    yaxis=dict(
        title='count of gold medals')
)
fig = go.Figure(data=data, layout=layout)

gold_medals_male_vs_female = py.plot(fig, filename='my-third-graph')


# In[5]:


my_dboard = dashboard.Dashboard()
 
nationality_count_of_athletes_id = fileId_from_url(nationality_count_of_athletes)
nationality_count_of_silver_gold_id = fileId_from_url(nationality_count_of_silver_gold)
gold_medals_male_vs_female_id = fileId_from_url(gold_medals_male_vs_female)
 
box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': nationality_count_of_athletes_id,
    'title': 'Nationality/Count of athletes'
}
 
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': nationality_count_of_silver_gold_id,
    'title': 'Nationality/Gold and Silver medals'
}
 
box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': gold_medals_male_vs_female_id,
    'title': 'Gold medals - male vs female'
}
 
my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)
 
 
 
py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')


# In[6]:


conn.close()

