""" Will utilize tensorflow or tensorflow.js, if able, for training and testing """

""" The following is for tensorflow working with python: 
from mediapipe.util.sequence import media_sequence_util as msu

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v1 as tf """

from math import *
import asyncio

""" pow(), sqrt(), mix(), max() and some other functions do not require from math import * """

my_name = "Alston"
my_power_level = "Also, my power level is over " + str(int(pow(10, 3) * 9)) + "!!! " + "Also, also, my favorite number is: " + str(round(2.7))
initial_greeting = "Hey, it's " + my_name + ". Training and testing for Tri-Sense will live here, eventually."
names_and_numbers = ["Carl", str(3), "Stan", str(7), "Ken"]

""" Tupple time with () like - tupple_time = ("index 0 here", "index 1 here") """
""" Tupples are immutable """
""" Can access tupples with indexing like - tupple_time[1]"""
coordinate = (5, 3)
coordinates = [(2, 3), (8, 10), (20, 15)]

print(initial_greeting.replace("Alston", "Drew") + "\n" + my_power_level)

response = input("Who are you: ")
print("Hello " + response + "!")

async def show_nums_and_coordinates(confirmation):
    print(confirmation.capitalize() + ":\n" + names_and_numbers[1] + "\n" + str(coordinate) + "\n" + str(coordinates[2]) + "\n" + "Function ran(text from 'All good here' through this sentence).")
    await asyncio.sleep(3)
    print("Thank you for trying this program.")

async def working_with_list_flow():
    favorite_numbers = [3, 5, 7, 15]
    favorite_characters = ["Goku", "Midoriya", "Andy Dufresne", "Edmond Dantes"]
    favorite_characters.extend(favorite_numbers)
    fav_nums_copy = favorite_numbers.copy()
    favorite_numbers.extend(favorite_characters)
    print(fav_nums_copy)
    print(favorite_characters)

    """Conditional loop"""
    for number in favorite_numbers:
        await asyncio.sleep(1)
        print(number)
    else:
        print("Loop complete!")

asyncio.run(working_with_list_flow())
asyncio.run(show_nums_and_coordinates("all Good Here"))