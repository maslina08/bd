#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cx_Oracle
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import pandas_oracle.tools as pt

connection = cx_Oracle.connect('roma/rama@localhost')


# In[2]:


query1 = "select nationality, count(*) as count_of_athletes from athl_inf group by nationality"
query2 = "select nationality, sum(athl_inf.gold) as count_of_gold_medals, sum(athl_inf.silver) as count_of_silver_medals from athl_inf where athl_inf.silver != 0 and athl_inf.gold != 0 group by nationality"
query3 = "select sport, sum(athl_inf.gold) as count_of_gold_medals from athl_inf where athl_inf.sex = 'male' group by SPORT"
query4 = "select sport, sum(athl_inf.gold) as count_of_gold_medals from athl_inf where athl_inf.sex = 'female' group by SPORT"
df1 = pt.query_to_df(query1, connection)
df2 = pt.query_to_df(query2, connection)
df3 = pt.query_to_df(query3, connection)
df4 = pt.query_to_df(query4, connection)


# In[3]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.dashboard_objs as dashboard

py.sign_in('maslina8', '0MZhNYQK7iFfngyzE015')

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId =url.split('~')
    return raw_fileId[1].replace('/', ':')


# In[4]:


df1 = df1.sort_values(['COUNT_OF_ATHLETES'], ascending=False)
data = [go.Bar(x=df1['NATIONALITY'],y=df1['COUNT_OF_ATHLETES'])]

layout = go.Layout(
    title='nationality/count of athletes',
    xaxis=dict(
        title='nationality'),
    yaxis=dict(
        title='count of athletes')
)
fig = go.Figure(data=data, layout=layout)
 
nationality_count_of_athletes = py.plot(fig, filename='my-first-graph-view')


df2 = df2.sort_values(['COUNT_OF_SILVER_MEDALS','COUNT_OF_GOLD_MEDALS'], ascending=False)
trace1 = go.Bar(x=df2['NATIONALITY'],y=df2['COUNT_OF_GOLD_MEDALS'],name='Gold',marker=dict(color='#FFD700'))
trace2 = go.Bar(x=df2['NATIONALITY'],y=df2['COUNT_OF_SILVER_MEDALS'],name='Silver',marker=dict(color='#9EA0A1'))

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
 
nationality_count_of_silver_gold = py.plot(fig, filename='my-second-graph-view')


df3 = df3.sort_values(['COUNT_OF_GOLD_MEDALS'], ascending=False)
df4 = df4.sort_values(['COUNT_OF_GOLD_MEDALS'], ascending=False)   
trace1 = go.Bar(x=df3['SPORT'],y=df3['COUNT_OF_GOLD_MEDALS'],name='male',marker=dict(color='blue'))
trace2 = go.Bar(x=df4['SPORT'],y=df4['COUNT_OF_GOLD_MEDALS'],name='female',marker=dict(color='pink'))    
    

data=[trace1, trace2]

layout = go.Layout(
    title='Gold medals - male vs female',
    xaxis=dict(
        title='sport'),
    yaxis=dict(
        title='count of gold medals')
)
fig = go.Figure(data=data, layout=layout)

gold_medals_male_vs_female = py.plot(fig, filename='my-third-graph-view')



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
 
 
 
py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python -view')


connection.close()


# In[ ]:




