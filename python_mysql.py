#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 安装MySQLdb，请访问 http://sourceforge.net/projects/mysql-python
# Linux平台可以访问：https://pypi.python.org/pypi/MySQL-python) 分为预编译的二进制文件和源代码安装包

# # 数据库连接
# # 打开数据库连接
# db = MySQLdb.connect("172.16.1.130", "root", "123456", "test")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
# print "Database version : %s " % data
# # 关闭数据库连接
# db.close()


# # 创建数据库表
# db = MySQLdb.connect("172.16.1.130", "root", "123456", "test")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)
# # 关闭数据库连接
# db.close()


# # 数据库插入操作
# # 打开数据库连接
# db = MySQLdb.connect("172.16.1.130", "root", "123456", "test")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# # 以上sql语句也可以写成
# # sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
# #        LAST_NAME, AGE, SEX, INCOME) \
# #        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
# #        ('Mac', 'Mohan', 20, 'M', 2000)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()
# # 关闭数据库连接
# db.close()


# 以下代码使用变量向SQL语句中传递参数:
# ..................................
# user_id = "test123"
# password = "password"
#
# con.execute('insert into Login values("%s", "%s")' % \
#              (user_id, password))
# ..................................


# 数据库查询操作
# 打开数据库连接
db = MySQLdb.connect("172.16.1.130", "root", "123456", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()


# # 数据库更新操作
# # 打开数据库连接
# db = MySQLdb.connect("172.16.1.130", "root", "123456", "test")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
#
# # 关闭数据库连接
# db.close()


# # 删除操作
# # 打开数据库连接
# db = MySQLdb.connect("172.16.1.130", "root", "123456", "test")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
#
# # 关闭连接
# db.close()


# 执行事务
# SQL删除记录语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 向数据库提交
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()


# DB API中定义了的常见错误及异常
# Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
# Error	警告以外所有其他错误类。必须是 StandardError 的子类。
# InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
# DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
# DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
# OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
# IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
# InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
# ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
# NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。








