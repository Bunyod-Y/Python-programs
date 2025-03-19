# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:40:24 2025

@author: bunyod
"""

year=int(input("Enter a year: "))

if (year%400==0) and (year%100==0):
    print("{0} is a leap year".format(year))
    
elif (year%4==0) and (year%100!=0):
    print("{0} is leap year".format(year))
else:
    print("{0} is not leap year".format(year))    
    
if (year%400==0) and (year%100==0):
    print(f"{year} is a leap year")
        
elif (year%4==0) and (year%100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")  