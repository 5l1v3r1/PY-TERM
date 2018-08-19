#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

'''
imports
'''

import sys
import os
import time
import random
import socket
from time import sleep


'''
defs & classes
'''

def updt(total, progress):
    barLength, status = 150, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "~" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
	
class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    LOGGING = '\33[34m'
	
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.LOGGING]
random.shuffle(color_random)
	
pyterm = color.HEADER + '''
							██████╗ ██╗   ██╗  ████████╗███████╗██████╗ ███╗   ███╗
							██╔══██╗╚██╗ ██╔╝  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
							██████╔╝ ╚████╔╝█████╗██║   █████╗  ██████╔╝██╔████╔██║
							██╔═══╝   ╚██╔╝ ╚════╝██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║
							██║        ██║        ██║   ███████╗██║  ██║██║ ╚═╝ ██║
							╚═╝        ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                     ''' + color.END

hostname = (socket.gethostname())
info = color.OKBLUE + """

						}----------{ PY-TERM; (C) The Dark Army, 2016-2018. }----------{
					}-----{ PY-TERM on: %s. Python: "ENV PYTHON 2" stated by: SCRIPT }-----{
						}--------{ TO START TYPE: 'help', OR TYPE YOURE COMMAND }--------{
			
			""" + color.END
def boot():
	print('' + color.RED)
	runs = 100
	for run_num in range(runs):
		time.sleep(.1)
		updt(runs, run_num + 1)	
	print('' + color.END)
	
def bootT():
	print('' + color.RED)
	runs = 50
	for run_num in range(runs):
		time.sleep(.1)
		updt(runs, run_num + 1)	
	print('' + color.END)
	
def bootF():
	print('' + color.RED)
	runs = 25
	for run_num in range(runs):
		time.sleep(.1)
		updt(runs, run_num + 1)	
	print('' + color.END)

def bootFF():
	print('' + color.RED)
	runs = 5
	for run_num in range(runs):
		time.sleep(.1)
		updt(runs, run_num + 1)	
	print('' + color.END)


'''
command line vars
'''

help = '''
	HELP			=>			For more information on a specific command, type 'help' command-name.
	CLEAR			=>			Clears the screen.
	LS			=>			Lists server's directors.
	EXIT			=>			Quits PY-TERM program.
	SYSTEMINFO 		=>			Loads system info.
		'''
	
def exit():
	os.system('exit')

def clear():
	os.system('clear')

def ls():
	os.system('ls-a')

def systeminfo():
	os.system('systeminfo')
	
PATH = os.system('dirs')

x = 1
	
'''
command line interface
'''

commlinetext = color.RED + (hostname) + ':' + color.END 
commlinedir = color.OKGREEN + '/' + color.END
clear()
print(pyterm)
boot()
print("Loading TERMINAL")
bootT()
print("Starting Server")
bootFF()
print("Starting Damien's")
bootT()
print("Runing RC & CONF files")
bootF()
input("SERVER TERMINAL LOADED, PRESS [ENTER] TO CONTUNE...")
clear()
print(pyterm)
print(info % hostname)
while x == 1 :
	commandline = input('%s%s > ' % (commlinetext, commlinedir))
	if commandline == 'help':
		print(help)
	elif commandline == 'clear':
		clear()
	elif commandline == 'ls':
		ls()
	elif commandline == 'systeminfo':
		systeminfo()
	elif commandline == 'cd':
		cd()
	elif commandline == 'exit':
		break 
		exit()
	else:
		print("\n'%s' is not recognized as an internal or external command, operable program or file.\n" % (commandline))
