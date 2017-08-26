# coding=utf-8
#!python3

"""
问题：热狗店，提供如下组合：热狗dog、小面包bun、番茄酱ketchup、芥末酱mustard、洋葱onion
     给出所有可能的组合
"""

import easygui

# dog     = easygui.msgbox(title = "hot dog", msg = "Would you like a dog ?")
# bum     = easygui.msgbox(title = "hot dog", msg = "Would you like a bum ?")
# ketchup = easygui.msgbox(title = "hot dog", msg = "Would you like a ketchup ?")
# mustard = easygui.msgbox(title = "hot dog", msg = "Would you like a mustard ?")
# onion   = easygui.msgbox(title = "hot dog", msg = "Would you like a onion ?")

dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40
print("\tDog \tBun \tKetchup Mustard Onions tot_cal")
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print("#", count, "\t", end="")
                    print(dog, "\t", bun, "\t", ketchup, "\t", end="")
                    print(mustard, "\t", onion, end="")
                    print(dog*dog_cal + bun*bun_cal + mustard*mus_cal + ketchup*ket_cal + onion*onion_cal)
                    count += 1