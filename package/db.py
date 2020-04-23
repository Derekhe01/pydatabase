#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/4/21
# @Author    : Roger
# @File      : db.py
# @Software  : PyCharm
# @Desc      :

import cx_Oracle
import pymysql as ps
import pymssql
import logging
import json

logging.basicConfig(level=logging.ERROR,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    filename='error.log',
                    filemode='a'
                    )


class DbHelper:
    def __init__(self, dbtype, host, user, password, database, port):
        '''
        使用办法：
        from __future__ import division
        import sys
        reload(sys)
        sys.path.append('/path/')
        from db import DbHelper
        先创建类对象：对象名= DbHelper('数据库类型：MYSQL/ORACLE/SQLSERVER','IP','用户名','密码','数据库名','端口')
        再调用对象的函数
        例如 mh = DbHelper('MYSQL','192.168.100.100', 'root', '123456', 'test', '3306')
        sql = "select * from user where id=%s"
        params = list(range(1,10))
        for i in params:
            newsql = sql % i
            print(mh.query(newsql)
        '''
        self.dbtype = dbtype
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = 'utf8'
        self.port = int(port)
        self.conn = None
        self.curs = None

    def open(self):
        # 数据库连接
        try:
            # 支持oracle多线程,普通用户连接
            if self.dbtype == 'ORACLE':
                # self.conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(self.user, self.password, self.host, self.port, self.database),threaded=True, events=True,mode=cx_Oracle.SYSDBA)
                self.conn = cx_Oracle.connect(
                    '{0}/{1}@{2}:{3}/{4}'.format(self.user, self.password, self.host, self.port, self.database),
                    threaded=True, events=True)
            elif self.dbtype == 'MYSQL':
                self.conn = ps.connect(host=self.host, user=self.user, password=self.password, db=self.database,
                                        port=self.port, charset=self.charset)
            elif self.dbtype == 'SQLSERVER':
                self.conn = pymssql.connect(host=self.host, user=self.user, password=self.password, db=self.database,
                                             port=self.port, charset=self.charset)
            self.curs = self.conn.cursor()
        except Exception as e:
            logging.error('%s %s connect failed' % (self.database, self.host))
            logging.error(e)

    def close(self):
        # 数据库关闭
        self.curs.close()
        self.conn.close()

    def idu(self, sql):
        '''
        数据增删改，使用idu函数
        :param sql: 执行的sql
        :return: 返回结果
        '''
        self.open()
        try:
            self.curs.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error('%s %s exec failed' % (self.database, self.host))
            logging.error(e)
            self.conn.rollback()
        self.close()

    def query(self, sql):
        '''
        数据查询函数，有返回值
        :param sql: 执行的SQL
        :return: 返回结果
        '''
        self.open()
        try:
            result = self.curs.execute(sql)
            results = self.curs.fetchall()
            self.close()
            return results
        except Exception as e:
            logging.error('%s %s exec failed' % (self.database, self.host))
            logging.error(e)
