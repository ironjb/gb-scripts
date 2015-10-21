#!/usr/bin/python
import os
import eyeD3
# help(eyeD3)
for filename in os.listdir('./'):
	if '.mp3' in filename:
		print filename
		# audiofile = eyeD3.utils.load('./140822_Hour4.mp3')
		# print audiofile.tag.title