print("Welcome to Tresure Island")
print("Your Mission is to find the Tresure")
direction = input('Which direction you want to go? Type "left" or "right".').lower()
if direction == "left":
    s_w = input('You have two choices, wheater do you want "swim" to cross or do you want to "wait. "? ').lower()
    if s_w == "wait":
        colour = input('You have to choose between three colors, "red" or "blue" or "yellow."? ').lower()
        if colour == "yellow":
            print("You have win the game sire")
        elif colour == "red":
            print("Your game is over, you can start again! thank you")
        elif colour == "blue":
            print("Your game is over, you can start again! thank you")
        else:
            print("You chos a door that doesn't exist, you can start again! thank you")
    else:
        print("You have boarded a bus to heaven")
else:
    print("You have boarded a bus to heaven")
