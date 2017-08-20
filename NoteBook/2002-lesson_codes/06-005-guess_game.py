#  coding=utf-8 
#! python3 
#  猜数游戏

# =======================================================================
import random
import easygui

secret = 0
tries  = 0
guess  = 0
last_guess = guess

_again = "again"
_quit  = "quit"
start_again = _again

easygui.msgbox(title = "guess a number", 
               msg = """AHOY!  I'm the Dread Pirate Roberts, and I have a secret!
                        It's a number from 1 to 99. 
                        I'll give you 6 tries.""",
               ok_button="start")
while (start_again == _again):
    secret = random.randint(1, 99)
    guess  = secret + 1
    tries  = 0
    while (guess != secret) and (tries < 6):
        last_guess = guess
        guess = easygui.enterbox(title = "Enter you guess number",
                                msg = "enter from 1 - 99, 0 could quit game.",
                                default = str(last_guess))
        guess = int(guess)
        tries = tries + 1
        if not guess: 
            break
        if guess < secret:
            easygui.msgbox(title = "Show Time",
                           msg = str(guess) + " is too low, ye scurvy dog!\r\n" + 
                                              "you have " + str(6 - tries) + " times left",
                           ok_button = "try again")
        elif guess > secret:
            easygui.msgbox(title = "Show Time",
                           msg = str(guess) + " is too high, landlubber!\r\n" + 
                                              "you have " + str(6 - tries) + " times left",
                           ok_button = "try again")

    if guess == secret:
        start_again = easygui.buttonbox(title = "Game end",
                                        msg = '[' + str(guess) +']  ' + "Avast!  ye got it! Found my secret, ye did!",
                                        choices = (_again, _quit)
                                        )
    else:
        start_again = easygui.buttonbox(title = "Game end",
                                        msg = "No more guesses! Better luck next time, matey!",
                                        choices = (_again, _quit)
                                        )
