# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:14:41 2020

@author: Yun, Junhyuk 2019330026
"""

#query2.py
import sqlite3

# db 생성
con = sqlite3.connect('./university.db')
cur= con.cursor()

#query
query='''
with ID_table as (select t1.year as year, t1.semester as semester, cnt, ID from (select semester, year,count(ID) as cnt, ID from teaches group by year,semester,ID) as t1 inner join (select semester, year, max(cnt) as max_cnt from (select semester, year,count(ID) as cnt from teaches group by year,semester,ID) group by semester, year) as t2 on t1.cnt=t2.max_cnt and t1.semester=t2.semester and t1.year=t2.year)
select year, semester, cnt, name from ID_table natural join instructor where ID_table.ID = instructor.ID;
'''

# select
try:
    cur.execute(query)
    row=cur.fetchall()
    print('year,semester,course_count,name')
    for tup in row:
        print(tup[0], ',', tup[1], ',', tup[2],',', tup[3], sep='')
except sqlite3.Error as e:
    print("Command skipped: ", e)

# cusor와 connection 종료
con.commit()
cur.close()
con.close()
