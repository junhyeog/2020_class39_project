# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:38:02 2020

@author: 2019330026 Yun, Junhyuk
"""

import sqlite3

# db 생성
con = sqlite3.connect('./university.db')
cur= con.cursor()

# sql 파일 입력 받고 command 파싱
fd = open('DDL.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')

# 각각의 Command 실행
for command in sqlCommands:
    try:
        cur.execute(command)
    except sqlite3.Error as e:
        print("Command skipped: ", e)
        
# 만들어진 table 확인
cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
row = cur.fetchall()
print("Created Table: ", len(row))
for table in row:
    print(table[0], end=', ')

# cusor와 connection 종료
con.commit()
cur.close()
con.close()
