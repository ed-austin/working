#! /usr/bin/python3.3
#
# Description:
# script to print out allowable moves of a knight
# which is on a specified squqre.
# Number the squares as below, then 
# calculat each possible value
# for the next move
#

# 5 * 5 Square:
# 0  1  2  3  4
# 5  6  7  8  9
#10 11  x 13 14
#15 16 17 18 19
#20 21 22 23 24 
#
# allowable spots from x (aka 12):
# 1, 3, 5, 9, 15, 19, 21, 23)
# which becomes following values to add to any position x,
# but based on conditions such as falling off the board - 
# ie, disallow if calculated spot < 0 or > 24 - see jumps5 
# for logic to find legal moves: 
# -11, -9, -7, -3, +3, +7, +9, +11 
#
# This works: 1 possible solution:
#  1  18   5  10   3
#  6  11   2  19  14
# 17  22  13   4   9
# 12   7  24  15  20
# 23  16  21   8  25


import copy

def ptrace(tflag, *x):
  """ function to print out trace information"""
  if tflag > 0:
    print (x)


# functions for 5 * 5 square:
def col5(x):
  return (x%5)

def row5(x):
  return int( (x-x%5)/5)

def jumps5(x):
  """ find allowable target spots from any current spot, in 5*5 board"""
  J=[]
  for i in [-11, -9, -7, -3, +3, +7, +9, +11]:
    if x+i > 24 or x+i < 0 or abs(col5(x+i)-col5(x)) > 2 or abs(row5(x+i)-row5(x)) > 2:
      continue
    J.append(x+i)
  J.sort()
  return J

def fprint5(H):
  """print out chessboard in a nice format"""
  for i, val in H.items():
    if i%5==0:
      print ("\n")
    print ("{:3}".format(val), end='')
  print ("\n")

def is_complete5(H):
  """ completion criteria """
  sum=0
  for i, val in H.items():
    sum=sum+val
  if sum == 325:
    print ("Complete !")
    fprint5(H)
    return True
  else:
    return False


# base procedure for 5 * 5 board
def kmoves5(H, spot, step=1):
  """function to recurse over allowable moves"""
  if is_complete5(H) == True:
    return True
  if H[spot]>=1:
    return False
  H[spot]=step
  ptrace(0, "step: ", step)
  M=jumps5(spot)
  ptrace(0, "M here: ", M)
  for spot in M:
    ptrace(0, "spot/step here: ", spot, step+1)
    if kmoves5(copy.deepcopy(H), spot, step+1) == True:
      break
  ptrace(0, "falling off end with step: ", step)
  return


if __name__ == '__main__':

  H={}
  for i in range (25):
    H[i]=0

  spot=int(input("Enter spot: "))
  kmoves5(H, spot, 1)


# EOF
