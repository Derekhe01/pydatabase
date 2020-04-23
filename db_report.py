#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/4/23
# @Author    : Roger
# @File      : db_report.py
# @Software  : PyCharm
# @Desc      :

import logging
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from package import db, html, conn


logging.basicConfig(level=logging.ERROR,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    filename='error.log',
                    filemode='a'
                    )


def main():
    result = []
    conn_sql = 'select host,user,password,db,port from mysql_server'
    query_sql = input("输入查询sql:\n")
    query_sql = query_sql.strip().strip(';')
    source_file = os.path.abspath('./etc/login.ini')
    ip, user, pwd, database, port = conn.conn(source_file)
    sdb = db.DbHelper('MYSQL', ip, user, pwd, database, port)
    conn_results = sdb.query(conn_sql)
    if not conn_results:
        sys.exit(0)
    else:
        for c in conn_results:
            thost, tuser, tpassword, tdatabase, tport = c
            try:
                tdb = db.DbHelper('MYSQL', thost, tuser, tpassword, tdatabase, tport)
                values = tdb.query(query_sql)
                for v in values:
                    result.append([thost, tdatabase, v])
            except Exception as e:
                values = e
                result.append([thost, tdatabase, values])
                logging.error(e)
    html.to_html('db_query', 'result', result)


if __name__ == '__main__':
    main()
