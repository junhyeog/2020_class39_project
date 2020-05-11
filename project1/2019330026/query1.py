# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:44:59 2020

@author:  2019330026 Yun, Junhyuk
"""

#query1.py
import sqlite3

# db 생성
con = sqlite3.connect('./university.db')
cur= con.cursor()

# select
try:
    cur.execute("SELECT dept_name, avg(salary) FROM instructor GROUP BY dept_name ORDER BY dept_name IS NULL")
    row=cur.fetchall()
    print('dept_name,salary')
    for tup in row:
        print(tup[0], ',', tup[1], sep='')
except sqlite3.Error as e:
    print("Command skipped: ", e)

# cusor와 connection 종료
con.commit()
cur.close()
con.close()
