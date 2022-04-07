"""
This program randomy generate a set of numbers and then calculate the average of the numbers
"""
import random


def average(args):
    """
    This function returns the average of a list of numbers
    """
    return sum(args)/len(args)


def random_number_generator(count):
    """
    This function returns a random number between 0 and 100
    """
    rng_list = []
    given_no_count = int(count)
    counter = 0
    while counter < given_no_count:
        rng = random.randint(1, 100)
        rng_list.append(rng)
        counter += 1
    return rng_list


def main():
    """
    This function is the main function of the program
    """
    rng_list = random_number_generator(input(
        "How many random numbers do you want to generate? "))
    for number in rng_list:
        print(number)
    print("The average of the numbers is:", average(rng_list))


main()
