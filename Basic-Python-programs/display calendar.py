# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:50:38 2025

@author: bunyod
"""

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)
