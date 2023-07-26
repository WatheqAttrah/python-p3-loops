#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print(f"Happy New Year!")


happy_new_year()


def square_integers(int_list):
    # code goes here!
    square_list = [number * number for number in int_list]
    return square_list
    pass


def fizzbuzz():
    # code goes here!
    number = 1
    while number <= 100:
        if (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif (number % 3 == 0 and number % 5 != 0):
            print("Fizz")
        elif (number % 5 == 0 and number % 3 != 0):
            print("Buzz")
        else:
            print(number)
        number += 1


fizzbuzz()
