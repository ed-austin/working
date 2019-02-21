#! /usr/bin/python3.3
# script to read log 
# Simulate reading error log
# if you see n consecutive IDs,
# they may be a sign of hackers
# so capture them
# 
# Adjust source file format as needed,
# example file here is in format:
#
# name throw_away_text
#

import sys
file = sys.argv[1]

d={}
stack=[]

def push(stack, nm):
  stack.append(nm)
  return stack

def clear (stack):
  stack.clear()
  return stack

def top (stack):
  return stack[0]

def cnt (stack):
  return len(stack)

def fprint (d):
  for k, v in d.items():
    print ("{:10} {:5}".format(k, v))



if __name__ == '__main__':

  stack = push (stack, '-1') # prime stack
  with open (file) as f:
    for line in f:
      name = line.split(" ")[0]
      if name not in top(stack): #clear stack and push new name
        stack=push(clear(stack), name)
      else:
        if cnt( push(stack,name) ) >= 3:
          d[name]= cnt(stack)

  fprint (d)

# EOF
