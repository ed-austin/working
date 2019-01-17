#!/usr/bin/python3.3
import os
import sys
import re
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


def f_get_rdms (source):
  sqlite = re.compile ("[\w/]*\.db")
  m = sqlite.match(source)
  if m:
    return "sqlite"


def f_conn (db):
  rdms = f_get_rdms(db)
  if (rdms == str("sqlite")):
    return sqlite3.connect(db, isolation_level = None)


def f_fetchall( conn, sql ):
  cur = conn.cursor()
  cur.execute(sql)
  for row in cur.fetchall():
    print (row)


def f_run_sql (db, source):
  f_fetchall (f_conn(db), f_get_sql(source))
  #for row in  f_fetchall (f_conn(db), f_get_sql(source)):
  #  return (row)


def f_insert (db, source, source_file): 
   conn = f_conn(db)
   sql  = f_get_sql(source) + " {} {} {}"
   f    = open (source_file, "r")
   i=0
   data = f.readlines()
   c = conn.cursor()
   for row in data:
     #cmd = sql + ' values ( ' + row + ')'
     cmd = sql.format("values ( ", row.strip(), ")")
     print ("cmd: ", cmd)
     c.execute(cmd)    
   conn.commit()


# EOF
