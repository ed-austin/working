# There are n stairs, a person standing at the bottom 
# wants to reach the top. The person can climb either 
# 1 stair or 2 stairs at a time. Count the number of 
# ways, the person can reach the top.

# https://www.geeksforgeeks.org/count-ways-reach-nth-stair/

STAIRS=7

def climb (stairs, _str=''):
  """ Recursive call to climb
  """
  if stairs < 0:
    return
  if stairs == 0:
    print (_str)
    return
  for i in [1, 2]:
    climb (stairs-i, _str = _str + ':' + str(i))


climb (STAIRS)
