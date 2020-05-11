# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:46:34 2020

@author: 2019330026 Yun, Junhyuk
"""

#query3.py
import sqlite3

# db 생성
con = sqlite3.connect('./university.db')
cur= con.cursor()

#query
query='''
with candidate_section as (
select *
from (with available_time_slot_id as (select time_slot_id from (select time_slot_id, day, min(start_hr) as min_start_hr, max(end_hr) as max_end_hr from time_slot group by time_slot_id) where min_start_hr>=8 and max_end_hr<=11)
select * from section where time_slot_id in available_time_slot_id and semester='Summer' and year=2010) as tmp_section natural join classroom natural join (select course_id, title from course) as course
where tmp_section.building=classroom.building and tmp_section.room_number=classroom.room_number and tmp_section.course_id=course.course_id), max_capacity as (
select max(capacity) as max_capacity from candidate_section)
select capacity, title from candidate_section where candidate_section.capacity in max_capacity;
'''
# select
try:
    cur.execute(query)
    row=cur.fetchall()
    print('capacity,title')
    for tup in row:
        print(tup[0],',', tup[1], sep='')
except sqlite3.Error as e:
    print("Command skipped: ", e)

# cusor와 connection 종료
con.commit()
cur.close()
con.close()
