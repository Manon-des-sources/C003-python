# coding=utf-8
#!python3

"""
问题：第12章习题
"""

import easygui

temp = ''
names = []
input_names = input("Enter 5 names:\r\n")  # input输入的所有是一个字符串
print("your entered: ", type(input_names), input_names)

for name in input_names:
    if ('a' <= name <= 'z') or ('A' <= name <= 'Z'):
        temp += name
    else:
        if temp != '':
            names.append(temp)
            temp = ''

if temp != '':
    names.append(temp)
names.sort()
print("Sorted names: ", type(names), names)

index = input("You can replace one, which one? (1-5)  ")
index = int(index) - 1

temp = input("New name: ")
names[index] = temp

print(names)