#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/4/23
# @Author    : Roger
# @File      : conn.py
# @Software  : PyCharm
# @Desc      :

def conn(file):
    # 取出cmdb库的密码信息,可读用户
    # ip:用户名:密码:数据库:端口
    conn_info = open(file, 'r')
    info = conn_info.read().split()[0].split(':')
    ip = info[0]
    user = info[1]
    pwd = info[2]
    db = info[3]
    port = info[4]
    return ip, user, pwd, db, port
