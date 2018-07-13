#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys
import sympy


def get_num(string):
    '''
    This will attempt to parse a string as an int and catch an exception if
    it fails
    '''
    try:
        return int(string)
    except Exception:
        print("You didn't enter a number!")
        sys.exit()


def prime_checker(num):
    ''' This will check to see if a given number is prime '''
    if sympy.isprime(num):
        print('It is prime!')
    else:
        print('Nope! Try again.')


def get_nth(n):
    ''' This will print out n primes '''
    p = [sympy.prime(i) for i in range(1, n+1)]
    p_list = []
    for prime in p:
        p_list.append(prime)
    for prime in p_list:
        if not prime == p_list[-1]:
            print(str(prime) + ',', end='')
        else:
            print(p_list[-1])


def main():
    '''
    This is the main function that is our initial entry point into our program
    '''
    # clear the console screen
    os.system('clear')

    # ask for whether they want prime checking or nth prime
    answer = get_num(input('Choice?\n1. prime checking\n2. nth prime\n'))

    if answer == 1:
        # ask for the number they want to check
        prime_checker(get_num(input('What number do you want to check? ')))
    elif answer == 2:
        get_nth(get_num(input('How many primes do you want to see? ')))
    else:
        print("I didn't recognize your response!")
        sys.exit()

    # wait for the user to press enter to quit
    input('\nPress enter to quit...')

    # clear the console screen
    os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
    main()
