#!/usr/local/bin python3

# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())
# only works on Unix/Linux/Mac:

pid = os.fork()
if pid==0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getpid()))
else:
	print('I (%s) just created a child process (%s)' % (os.getpid(), pid))
