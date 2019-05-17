#!D:\Python\python.exe 
# -*- coding:utf-8 -*-
# created by General

from odps import ODPS

odps = ODPS('LTAIp48JMGmSL6Bb', 'ClDJmBDAOeeOPuuA2XXURDQ45Xp1zx', 'chuangjin_risk',
            endpoint='http://service.odps.aliyun.com/api')

for table in odps.list_tables():
    print(table)