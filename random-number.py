#! /usr/bin/env python3

import random, sys

try:
	if len(sys.argv) == 3:
		min = int(sys.argv[1])
		max = int(sys.argv[2])	
	else:
		min = int(input('Enter range minimum: '))
		max = int(input('Enter range maximum: ' ))

	print(random.randint(min, max))
except ValueError:
	print('Invalid min/max values')
