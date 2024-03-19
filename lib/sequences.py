#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
       print([])
       return
    
    if length == 1:
       print([0])
       return
    
    if length == 2:
       print([0,1])
       return
    
    fib_seq = [0,1]

    while len(fib_seq) < length:
      next_num = fib_seq[-1] + fib_seq[-2]
      fib_seq.append(next_num)
      
    print(fib_seq)

print_fibonacci(10)
#!fibonacci sequence is a sequence where the next number is found by adding up the two numbers before it: