#!/usr/bin/python3.3
import os
import sys
import sqlite3


# 
#   --- subs ---
#


def f_get_sql(sql):
  try:
    f=open (sql, "r");
    str = f.read();
  except:
    str = sql
  return str; 


def f_conn (db):
  return sqlite3.connect(db, isolation_level = None)


def f_fetchall( conn, sql ):
  cur = conn.cursor()
  cur.execute(sql)
  return cur.fetchall()


def f_run_sql (conn, sql):
  for row in f_fetchall (conn, sql):
    return (row)
  


#
# --- program ---
#


if __name__ == '__main__':
  db     = sys.argv[1]
  source = sys.argv[2]
  f_run_sql ( f_conn(db), f_get_sql(source) )
#  for row in f_fetchall ( f_conn(db), f_get_sql(source) ):
#    print (row)



# EOF
