#  coding=utf-8 
#! python3 

"""
文件用途：
1、跟随书本示例做实验
2、课后习题
"""

# =======================================================================
import easygui
import time
import pygame


tries = input("Do you want to play(y/n)?")
while tries == "y":
    print("Which multiplication table would you like?")
    table_index = int(input())
    print("Here's your table:")
    multiplication = 1
    while multiplication <= 10:
        print(table_index, " * ", multiplication, " = ", table_index * multiplication)
        multiplication += 1
    tries = input("Do you want to play again(y/n)?")
