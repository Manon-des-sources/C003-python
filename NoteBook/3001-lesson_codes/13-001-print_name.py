# coding=utf-8
#!python3

# =======================================================================
"""
来源：第13章习题1
问题：打印名字(7*7 点阵)
接口：printMyName(name)
"""

# =======================================================================
# globals 

_C_ = [
"  CCCC ",
" C    C",
"C      ",
"C      ",
" C    C",
"  CCCC "
]

_H_ = [
"H     H",
"H     H",
"HHHHHHH",
"H     H",
"H     H",
"H     H"
]

_E_ = [
"EEEEEEE",
"E      ",
"EEEEE  ",
"E      ",
"E      ",
"EEEEEEE"
]

_N_ = [
"N     N",
"NN    N",
"N N   N",
"N  N  N",
"N   N N",
"N    NN"
]

MyName = [_C_, _H_, _E_, _N_, _C_, _H_, _E_, _N_] 

# "  CCCC ", "H     H", "EEEEEEE", "N     N",
# " C    C", "H     H", "E      ", "NN    N",
# "C      ", "HHHHHHH", "EEEEE  ", "N N   N",
# "C      ", "H     H", "E      ", "N  N  N",
# " C    C", "H     H", "E      ", "N   N N",
# "  CCCC ", "H     H", "EEEEEEE", "N    NN"

def printMyName():
    for x in range(_C_.__len__()):
        for y in range(MyName.__len__()):
            print(MyName[y][x], end='  ')
        print()

printMyName()