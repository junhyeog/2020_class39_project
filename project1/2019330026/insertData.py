# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:43:03 2020

@author: 2019330026 Yun, Junhyuk
"""

import sqlite3

# db 생성
con = sqlite3.connect('./university.db')
cur= con.cursor()

# 만들어진 table 확인
cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
row = cur.fetchall()
print("Created Table: ", end='')
for table in row:
    print(table[0], end=', ')
print("\n")

# 각 table에 해당하는 csv 파일 읽기
for table in row:
    table=table[0]
    # 데이터 읽기
    fd = open("./data/"+table+".csv", 'r')
    data = [tuple(s.split(',')) for s in fd.read().split('\n')[1:-1]] # title 제거, tuple 형식으로 파싱
    fd.close()
    # 데이터베이스에 쓰기
    for tup in data:
        try:
            cur.execute("INSERT INTO "+table+ " VALUES "+ str(tup))
        except sqlite3.Error as e:
            print("Command skipped: ", e)

# table에 저장된 값 확인
for table in row:
    table=table[0]
    print()
    try:
        cur.execute("SELECT * FROM "+table)
        row=cur.fetchall()
        print("Table:", table, len(row))
        print(row)
    except sqlite3.Error as e:
        print("Command skipped: ", e)

# cusor와 connection 종료
con.commit()
cur.close()
con.close()
