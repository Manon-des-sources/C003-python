import random

print "start\r\n"

secret = random.randint(1, 100)
guess  = 0
tries  = 0

print "Ahoy! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number form 1 to 99£¬ I'll give you 6 tries."

while guess != secret and tries < 6:
    guess = input("what's yer guess?")
    if guess < secret:
        print "Too low, ye scurvey dog!"
    elif guess > secret:
        print "Too high, landlubber!"
    tries = tries + 1

if guess == secret:
    print "Avast! ye got it! Found my secret, ye did!"
else:
    print "No more guess! Better luck next time, matey"
    print "The secret number was", secret