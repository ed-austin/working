#! /usr/bin/python3.3
#
# Initialize span of day 1 (i=0) as 1 and put on to stack.
# For i=1 to n, do following
# While price[stack.top()] < price[i] and !stack.isEmpty(), stack.pop()
#  If price[stack.top()] > price[i], span = (i - stack.top())
#  Push current day index i on to stack.
# Let's take an example and see if this works? Let's say prices are given on certain days are 
# as following: 100, 60, 70, 65, 80, 85, 200
# 
# As per algorithm, we will put span[0] = 1 and stack will be [0].
#
# On day 2, stock price is 60. Stock price on day at the top of 
# stack is 100, which is greater than 60. So span[1] = 1- 0 = 1. Stack = [0,1] (sp > dp, so span = 1-top(stack), push 1 to stack )
#
# On day 3, stock price is 70. We will pop from the stack till 
# price[stack.top()] < 70, which obviously pops out 1 as price[1] = 60. 
# So span[2] = 2 – 0 = 2. Push new price on stack, stack = [0,2]
#
# On day 4, stock price is 65. price[stack.top()] > price[3], so span[3] = 3-2=1. Stack = [0,2,3]
#
# On day 5, stock price is 80, now we pop out 3 and 2 from stack as price[2] 
# and price[3] are less than 80. span[4] = 4-0 = 4. stack = [0,4].
#
# On day 6, stock price is 85, now we pop out 4 from stack as price[4] is less than 85. 
# span[5] = 5-0 = 5. stack = [0,5].
# On day 7, stock price is 200, now we pop out 5 and 0 from stack as price[5] 
# and price[0] are less than 200. Now stack is empty, at this point, span[6] = 6. stack = [6].


stack=[]
span=[]

def push (stack_variable, i):
  stack_variable.append(i)
  return stack_variable

def pop (stack_variable):
    return stack_variable.pop()

def top (stack_variable):
  if len(stack_variable) > 0:
    return stack_variable[-1]
  else:
    return 0

def is_empty (stack_variable):
  if len(stack_variable) >= 1:
    return False
  else:
    return True

def tsprice (arr, stack):
  """ prince of stock on top of stack """
  return arr[top(stack)] 

def dprice (arr, i):
  """ daily price """
  return arr[i]


def calc(arr, stack, span):
# initialize first day:
  push (span, 1)
  push (stack, 0)

# now process remaining items:
  for i in range(1, len(arr)):

    if tsprice (arr, stack) > dprice(arr, i):
      push(span, i-top(stack))
      push(stack, i)

    else:
      if dprice (arr, i) >= tsprice(arr, stack):
        while is_empty(stack) is not True and dprice(arr, i) >= tsprice(arr, stack):
          pop(stack)
        push (span, i-top(stack))
        push (stack, i)

# summarize results:
  print ("arr: ", arr)
  print ("stack:", stack)
  print ("span: ", span)
    

if __name__ == '__main__':

  arr=[100, 60, 70, 65, 80, 85, 200, 135, 160, 99, 120, 185, 150, 140, 125, 100, 225, 10]
  calc (arr, stack, span)
    

# EOF
