# Very simple program to generate a random number using the command line arguments
# example: python3 ProjectPack1_RNG_py/rng-3.py 10 100

import random
import sys

rng_min = int(sys.argv[1])
rng_max = int(sys.argv[2])
print("Here is a random number for you between " + str(rng_min) + " and " + str(rng_max) + ": ", random.randint(rng_min, rng_max))
