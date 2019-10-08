# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 20:43:00 2019

@author: Le Huy Hoang
"""

import sys
import os

# Enable/Disable Debug Mode
debugFlag = os.getenv('DEBUG')
print('debugFlag: ' + str(debugFlag))
if 'ON' == debugFlag:
    print('Executing application in Debug Mode!')
    def LOG(message):
        print('[Debug] ' + message)
    
else:
    print('Executing application in Optimized Mode!')
    print('Note: Set environment variable DEBUG to \'ON\' before executing to enable Debug Mode.')
    def LOG(message):
        pass
