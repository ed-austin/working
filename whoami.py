#! /usr/bin/python3.3

def whoami(  ):
  """returns name of currently executing function"""
    import sys
    return sys._getframe(1).f_code.co_name

