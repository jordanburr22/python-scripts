#! /usr/bin/env python3

import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else: 
	address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
