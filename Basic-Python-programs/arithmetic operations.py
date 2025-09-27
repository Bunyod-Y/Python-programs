# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 13:52:28 2025

@author: bunyod
"""
number1=float(input("Enter first number: "))
number2=float(input("Enter second numbers: "))

#addition
addition=round(number1+number2)
print("Addition is ", addition)

#subtriction
subtriction=round(number1-number2)
print("Subtriction is ", subtriction)

#multiplication
multiplication=round(number1*number2)
print("Multiplication is ", multiplication)

#Division
if number2==0:
    print("Division by 0")
else:
    division=(number1/number2)
    print("Division is ", division)
