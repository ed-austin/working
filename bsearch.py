def bsearch(list, val, start, stop):
   """ binary search
       naive - fails if value isn't found
       Doesn't handle some edge cases, such as what if value isn't in list
   """
   print ("start, stop: ", start, stop)
   med = ((stop + start)//2)
   print ("med: ", med)
   if val == list[med]:
     print (val, " is found at pos: ", med)
     return
   elif val < list[med]:
     bsearch (list, val, start, med)
   else:
     bsearch(list, val, med, stop)


def is_asc(a, b):
  """ 
  convenience function
  to be applied to start and end id of a sorted, ascending array
  as opposed to a rotated, sorted array
  """
  if a < b:
    return True
  else:
    return False


def is_between (a, b, c):
  """ convenience function
  """
  if c >= a and c <= b:
    return True
  else:
    return False


def bsearch3(list, val, start, stop):
  """ binary search for sorted, then pivoted, array
  """
  if val == list[start]:
    print (val, "is found at position ", start)
    return
  if val == list[stop]:
    print (val, "is found at position ", stop)
    return
  med = (start + stop)//2
  if    is_asc(list[med], list[stop]) and is_between (list[med], list[stop], val):
    bsearch3(list, val, med, stop)
  elif is_asc(list[start], list[med]) and is_between (list[start], list[med], val):
    bsearch3(list, val, start, med)
  elif  not is_asc(list[med], list[stop]) and (val >= list[med] or val <= list[stop]):
    bsearch3(list, val, med, stop)
  elif not is_asc(list[start], list[med]) and (val >= list[start] or val <= list[med]):
    bsearch3(list, val, start, med)
  else:
    print ("ERROR: value ", val, "not found")
    exit()


def main (list, f):
  """ test that each item in list will be found """
  for i in range(len(list)): 
    val = list[i]
    if list[0] == val:
      print (val, " is found at position 0")
    elif list[-1] == val:
      print (val, " is found at position ", len(list)-1)
    else:
      f(list, val, 0, len(list)-1)

if __name__ == '__main__':
  list=[-7, -5, -3, -1, 1, 3, 4, 6, 8, 10, 12, 14, 16, 17, 20, 25, 26, 27, 32, 34, 36, 37, 38, 40, 55, 56]
  list2=[34, 36, 37, 38, 40, 55, 56, -7, -5, -3, -1, 1, 3, 4, 6, 8, 10, 12, 14, 16, 17, 20, 25, 26, 27, 32]
#                                                       ^
  list3=[36, 37, 38, 40, 41, 42, 1, 2,3]
  #main(list3, bsearch2)
  main(list3, bsearch3)
  #val = int(input("Enter value to find: "))
  #bsearch3(list2, val, 0, len(list)-1) 
