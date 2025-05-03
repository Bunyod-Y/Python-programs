# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:02:17 2025

@author: bunyod
"""

a=int(input("Enter value for A: "))
b=int(input("Enter value for B: "))

print(f"Before Swapping A={a}, B={b}")

a, b = b, a

print(f"After Swapping A={a}, B={b}")