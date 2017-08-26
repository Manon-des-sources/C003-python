#  coding=utf-8 
#! python3 
#  使用按钮、以获取用户输入

# =======================================================================
import easygui

# use buttonbox
flavor = easygui.buttonbox(msg = "What is your favorite ice cream flavor?",
                           title = "ice cream",
                           choices = ("Vanilla", "Chocolate", "Strawberry"))  # 元组
easygui.msgbox("You picked " + flavor)

# use choicebox
flavor = easygui.choicebox(msg = "What is your favorite ice cream flavor?",
                           title = "ice cream",
                           choices = ["Vanilla", "Chocolate", "Strawberry"])  # 列表
easygui.msgbox("You picked " + flavor)

# use enterbox to get a 'str'
flavor = easygui.enterbox(msg = "What is your favorite ice cream flavor?", 
                          title = "ice cream",
                          default ="orange")
easygui.msgbox("You picked " + flavor)
