#! /usr/bin/env python3

import os, re
pythonRegex = re.compile(r'.*\.py$')
dir = os.listdir('/Users/jordanburroughs/code/python-scripts')
pythonFiles = list(filter(pythonRegex.match, dir))

for file in sorted(pythonFiles):
	print(file)
