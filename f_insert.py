#!/usr/bin/python3.3
# given a db, a sql source (file or sql), and a file, 
# load the contents of the file one row at a time through
# insert... values (   ) 
import os
#import sys
#import sqlite3

import sql_functions as s


#
# --- program ---
#


if __name__ == '__main__':
  db     = sys.argv[1]
  source = sys.argv[2]
  if (sys.argv[3]):
    _file  = sys.argv[3]
  s.f_insert ( db, source, _file )


# EOF
