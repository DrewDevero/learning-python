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
my_power_level = "Also, my power level is over " + str(pow(10, 3) * 9) + "!!!"
initial_greeting = "Hey, it's " + my_name + ". Training and testing for Tri-Sense will live here, eventually."
names_and_numbers = ["Carl", str(3), "Stan", str(7), "Ken"]
coordinate = (5, 3)
coordinates = [(2, 3), (8, 10), (20, 15)]

print(initial_greeting.replace("Alston", "Drew") + "\n" + my_power_level)

response = input("Who are you: ")
print("Hello " + response + "!")

async def show_nums_and_coordinates(confirmation):
    print(confirmation.capitalize() + ":\n" + names_and_numbers[1] + "\n" + str(coordinate) + "\n" + str(coordinates[2]) + "\n" + "Function ran(text from 'All good here' through this sentence).")
    await asyncio.sleep(3)
    print("Thank you for trying this program.")

asyncio.run(show_nums_and_coordinates("All Good Here"))