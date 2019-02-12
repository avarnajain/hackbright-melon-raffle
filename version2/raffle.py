"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
import sys
from customers import *
from random import choice


def choose_winner(customer_list):
    winner = choice(customer_list)

    print("Tell {name} at {email} that they've won!".format(
        name=winner.name,
        email=winner.email
        ))

def run_raffle(filepath):
    customer_list = get_customers_from_file(filepath)
    choose_winner(customer_list)

run_raffle(sys.argv[1])
