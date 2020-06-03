#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:41:00 2020

@author: sergisanz
"""

from z3 import *

s = Solver()

s.from_file("fichero.smt2")

print(s.check())
print(s.model())