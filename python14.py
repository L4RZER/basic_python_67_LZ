"""
#
# Part: Python Install Package
# 
"""

import camelcase
camel = camelcase.Camelcase()
txt = "Hey Bro!"
print(camel.hump(txt))