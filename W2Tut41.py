# Copyright Paul-Johan Seim

def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)

foo(3)

def too (x):
   def bar (z):
      return z + x
   return bar(3)

too(2)
