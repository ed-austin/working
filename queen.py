#
# Queen problem
# lets try 8 x 8 sq
#
#              X
#    0  1  2  3  4  5  6  7
#    8  9 10 11 12 13 14 15
#   16 17 18 19 20 21 22 23
#   24 25 26 27 28 29 30 31
#   32 33 34 35 36 37 38 39
#   40 41 42 43 44 45 46 47
#   48 49 50 51 52 53 54 55
#   56 57 58 59 60 61 62 63

# Problem: place queens so that no queen can take another queen
# as you place a queen, determine all the spots under its control,
# where a queen is gets 1, 2,
# squares under its control are set to -1
# your are done when all spots are no longer 0

# Version 2:
#replace the "divmod" calls with rank, file and diag functions to improve readability

import copy

def rank(pos):
  """ returns the rank of the position, ie, the 'across-ways' value """
  return divmod(pos,8)[0]

def file(pos):
  """ returns the file of the position, ie, the 'up-down-ways' value """
  return divmod(pos,8)[1]

def diag1(pos):
  """ returns the diagonal value of the position
      this diag is upper-left -- lower right
  """
  return divmod(pos,9)[1]


def diag2(pos):
  """ returns the diagonal value of the position
      this diag is upper-right -- lower left
  """
  return divmod(pos,7)[1]


def uBoard (B, pos):
  if pos > 63:
    return None
  if B[pos] != 0:
    return None
  else:
    b = copy.deepcopy(B)
    b[pos]=max(b)+1
    for i in range(len(b)):
      if (rank(i) == rank(pos)) and b[i] == 0: # rank
        b[i] = -1
      if (file(i) == file(pos)) and b[i] == 0: # file
        b[i] = -1
      # diagonals:
      if (i < pos):
        if diag1(abs(i-pos)) == 0 and file(i) <= file(pos):
          b[i] = -1
        if diag2(abs(i-pos)) == 0 and file(i) > file(pos):
          b[i] = -1
      if (i > pos):
        if diag1(abs(i-pos)) == 0 and file(i) > file(pos): 
          b[i] = -1
        if diag2(abs(i-pos)) == 0 and file(i) < file(pos):
          b[i] = -1
  return b


def pprint (M):
  for i in range(len(M)):
    if i%8 == 0:
      print ("")
    if M[i] == -1:
        print ("{:3}".format('  .'),end='')
    else: 
        print ("{:3}".format(M[i]),end='')
  print ("\n")
 

def solve (B, pos):
  """ solve the question recursively """ 
  if not B:
    return
  if max(B) == 8:
    print ("\n\nSolution:")
    pprint (B)
  for i in range(len(B)):
    solve(uBoard(B, pos+i), pos+i)


if __name__ == '__main__':
  B=[0]*64
  for i in range(len(B)):
    solve(B, pos=i)
  
