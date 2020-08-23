#
# Chess knight problem
# lets try 8 x 8 sq
#
#              X
#    0  1  2   3    4  5  6  7
#    8  9 10  11   12 13 14 15
#   16 17 18  19   20 21 22 23
# Y 24 25 26  _27_ 28 29 30 31
#   32 33 34  35   36 37 38 39
#   40 41 42  43   44 45 46 47
#   48 49 50  51   52 53 54 55
#   56 57 58  59   60 61 62 63


def pprint (M):
  for i in range(len(M)):
    if i%8 == 0:
      print ("")
    print ("{:3}".format(M[i]),end='')


def get_moves (pos, M):
  """ return possible moves """
  y,x = divmod(pos, 8)
  moves=[-17, -15, -10, -6, +6, +10, +15, +17]
  list=[]
  # 1: if pos + move is > 63 or < 0, don't allow
  for i in moves:
  # 2: check for moves across a board boundary (not allowed)
    if (pos + i >= 0) and (pos+i <= 63):
      ynew,xnew=divmod(pos+i, 8)
      if abs(xnew-x) <= 2:
  # 3: check that the proposed position has not yet been occupied
        if M[pos+i] == 0:
          list.append (pos+i)
  list.sort()
  list.reverse()
  return (list)


def ulist(M, pos,v):
  """ append a value to M and return """
  import copy
  list= copy.deepcopy(M)
  list[pos]=v
  return list
  

def solve (M, cpos, move):
  """ solve the question recursively """ 
  if move == 64:
    print ("\n\nmove: ", move)
    print ("sum: ", sum(M))
    pprint (M)
    #exit()
  for next in  get_moves(cpos, M):
    solve(ulist(M, next, move+1), next, move+1)


if __name__ == '__main__':
  M=[0]*64
  M[2]=1
  solve(M, cpos=2, move=1)

