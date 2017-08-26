#  coding=utf-8 
#! python3 
#  动手试一试，习题2：获取地址

# =======================================================================
import easygui

address  = ""
address += easygui.enterbox(title = "Enter your address", msg = "name"       ) + "\r\n"
address += easygui.enterbox(title = "Enter your address", msg = "room number") + "  "
address += easygui.enterbox(title = "Enter your address", msg = "street"     ) + "  "
address += easygui.enterbox(title = "Enter your address", msg = "city"       ) + "\r\n"
address += easygui.enterbox(title = "Enter your address", msg = "state"      ) + "\r\n"
address += easygui.enterbox(title = "Enter your address", msg = "postalcode" )

easygui.msgbox(msg = address)
