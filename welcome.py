#! /usr/bin/env python

import cgi
import serial
from subprocess import call
import time
import os

print "Content-Type: text/html" # html content to follow
print                           # blank line, end of headers

#Hardware's team data

capacity  = int(os.listdir('/home/pi/max')[0])
text = os.walk('/home/pi/people')
current_people = 0
for a,b,s in text:

    for n in s:
    	current_people += 1



print """

<html>
<head>
<meta http-equiv="refresh" content="10">
<style>
        h2 {text-align: center;}
        h1 {text-align: center;}
        h3 {text-align: center;}
</style>
</head>
	<body>
	<h1>Welcome to SacHacks!<h1>
	<h2>People in the building:</h2>
	

"""
print '<h1>%d<h1>' % current_people
print '<h1>Only %d allowed<h1>' % capacity
if capacity <= current_people:
        print '<h3>Capacity filled! Wait here!<h3>'
else:
	print '<h3>Feel free to come in!<h3></body>'

print """
	
</html>

"""

