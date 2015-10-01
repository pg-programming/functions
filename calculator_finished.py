#!/usr/bin/env python

import os
import sys


## Write functions for each operation

def add(first, second):
  return first + second

def add_three(first, second, third):
  return operate_three(first, second, third, add)

def subtract(first, second):
  return first - second

def subtract_three(first, second, third):
  return operate_three(first, second, third, subtract)

def multiply(first, second):
  return first * second

def multiply_three(first, second, third):
  return operate_three(first, second, third, multiply)

def divide(first, second):
  try:
    return first / second
  except ZeroDivisionError:
    print 'Dividing by zero has the potential to destroy the universe.'
    print 'Quitting before any irreversible damage is incurred.'
    sys.exit()

def divide_three(first, second):
  return operate_three(first, second, third, divide)

def operate_three(first, second, third, func):
  return func(func(first, second), third)

def exponent(num, power):
  return num**power

def get_num(string):
  try:
    return int(string)
  except Exception:
    print 'I was unable to parse your input. Please enter a number next time'
    sys.exit()

def print_result(num):
  print 'The answer is: %s' % (num)

def main():

  # clear the console screen
  os.system('clear')

  ## have the user choose an operator
  print 'Choose your operator:'
  print '1. +\n2. -\n3. *\n4. /\n5. ^'
  operator = raw_input()


  ## ask for two or three operands
  num_operands = get_num(raw_input('Two or three operands: '))


  ## get the first and second operands
  operand_1 = get_num(raw_input('Please enter the first operand: '))
  operand_2 = get_num(raw_input('Please enter the second operand: '))

  ## get the third operand if they wanted three
  operand_3 = None
  if num_operands == 3:
    operand_3 = get_num(raw_input('Please enter the third operand: '))


  ## call the appropriate function based on their operator and number of operands

  if operator == '1':
    if operand_3:
      print_result(add_three(operand_1, operand_2, operand_3))
    else:
      print_result(add(operand_1, operand_2))

  if operator == '2':
    if operand_3:
      print_result(subtract_three(operand_1, operand_2, operand_3))
    else:
      print_result(subtract(operand_1, operand_2))

  if operator == '3':
    if operand_3:
      print_result(multiply_three(operand_1, operand_2, operand_3))
    else:
      print_result(multiply(operand_1, operand_2))

  if operator == '4':
    if operand_3:
      print_result(divide_three(operand_1, operand_2, operand_3))
    else:
      print_result(divide(operand_1, operand_2))

  if operator == '5':
    if operand_3:
      print "Sorry. I don't know what you mean with three operands and an exponent"
    else:
      print_result(exponent(operand_1, operand_2))

  # wait for the user to press enter to quit
  raw_input('\nPress enter to quit...')

  # clear the console screen
  os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
  main()
