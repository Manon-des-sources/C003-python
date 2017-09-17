# coding=utf-8
#!python3

# =======================================================================
"""
来源：
问题：
接口：
说明：
"""
# =======================================================================
# modules section
import random

# 用一个11面的骰子、代替两个6面的骰子，投出2-12 之间的数值
totals = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0]

for i in range(1000):
    dice_tatal = random.randint(2, 12)
    totals[dice_tatal] += 1

print('one die 11:')
print('index\t', 'times')
for i in range(2, 13):
    print(i, '\t', totals[i])

# 用两个6面的骰子、将它们投出的骰子相加，结果在2-12 
totals_2 = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0]
for i in range(1000):
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    dice_tatal = die_1 + die_2
    totals_2[dice_tatal] += 1
    
print('two die 6:')
print('index\t', 'times')
for i in range(2, 13):
    print(i, '\t', totals_2[i])
