#!/usr/bin/python3.3
import os
import sys
sys.path.append ('/home/schuged61/working/python')

# import sql functions:
import f_run_sql as s

def rleft():
  print ("executing rleft")

def rright():
  print ("execution rright")

def list():
  printt ("execution list")

def maini():
  print ("executing main")

def recur_dfirst(id,i=0):
  b="  "*i
  print ("{}:{}{:>5}".format('node ', b, id))
  #print ("node: ", id)
  if (id >= 0): 
    left=s.f_run_sql (s.f_conn('/home/schuged61/working/python/avl/test.db'),  "select left from nodes where id = {}".format(id))
    if (left):
      #print ("left : ", left[0])
      print ("{}:{}{:>5}".format('left ', b, left[0]))
      recur_dfirst(left[0],i+1) 

    right=s.f_run_sql (s.f_conn('/home/schuged61/working/python/avl/test.db'),  "select right from nodes where id = {}".format(id))
    if (right):
      #print ("right: ", right[0])
      print ("{}:{}{:>5}".format('right', b, right[0]))
      recur_dfirst(right[0],i+1) 


def recur_bfirst(id,i=0):
  b="  "*i
  print ("{}:{}{:>5}".format('node ', b, id))
  if (id >= 0):
    out=s.f_run_sql (s.f_conn('/home/schuged61/working/python/avl/test.db'),"select left, right from nodes where id = {}".format(id))
    if (out):
      print ("{}:{}{:>5}".format('left ', b, out[0]))
      print ("{}:{}{:>5}".format('right', b, out[1]))
      if (out[0]):
        recur_bfirst(out[0],i+1)
      if (out[1]):
        recur_bfirst(out[1],i+1)
 


if __name__ == '__main__':
  recur_dfirst(0)
  print (os.environ['PWD'])


# EOF
