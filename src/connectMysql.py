#!D:\Python\python.exe 
# -*- coding:utf-8 -*-
# created by General

import pymysql

db = pymysql.connect(host="47.96.125.53", port=3307, user="risk_kxg", password="Risk_kxg@20190213", database="riskdb_kxg",charset='utf8')

cursor = db.cursor()

cursor.execute("select * from sms_id;")

data = cursor.fetchall()

# for x in data:
#     print(x[0])

j = 0
for id in data:
    print(j,id[0])
    j+=1
db.close()