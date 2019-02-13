#! /usr/bin/python3.3
#
# Description:
# script to print out allowable moves of a bishop
# which is on a specified squqre.
# Number the squares as below, then 
# calculat each diagonal in terms
# of the different values for each square
#
# 0  1  2  3  4  5  6  7
# 8  9 10 11 12 13 14 15
#16 17 18 19 20 21 22 23
#24 25 26 27 28 29 30 31
#32 33 34 35 36 37 38 39
#40 41 42 43 44 45 46 47
#48 49 50 51 52 53 xx 55
#56 57 58 59 60 61 62 63


def col(x):
  return (x%8)


def row(x):
  return x-x%8


def diag(x,i,M):
  if x+i > 63 or x+i < 0:
    return M
  if abs(col(x+i)-col(x))> 1 or abs(row(x+i) == row(x)) > 1:
    return M
  M.append(x+i)
  return diag(x+i, i, M)


def bmoves(x):
  M=[]
  for i in [-9, -7, 7, 9]:
    M=diag(x, i, M)
  return M


if __name__ == '__main__':


  spot=input("Enter spot: ")
  print (bmoves(int(spot)))


# EOF
