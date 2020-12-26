# -*- coding: utf-8 -*-
import os
import subprocess

command = 'curl wttr.in'

two = subprocess.check_output(command).decode('utf-8')
str = two[90:127]
print( str)