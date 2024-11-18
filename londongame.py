print(r'''
   |       _L                                                          |
        / \     (  )                                                        ( )  |   |
        | |     |  |                                                  ___L_/   \/ \ / \
        | |   ()|  |()                                   | |         /      \ |||  \| |
     ___| |_()|   _  |_____                              |V|  ____--/     __dv|    ____"\
  /""          __( )   ____"==________..__           ____||| /       _____              ||
 /  __  []  ||     | ||   || / __________ \  _  |  _/  ____ "  [] []|     |    /\/\/\/\  _
 | /___    _''_      ''   ''| ]] ]]}} }} } |/ \/ \|  [[[|  |                  |  c c c |  \
   |      / \/ \                   ________        __             ______   _           |
          |            _______   _     _                _______   ||| ||     __
        ___________                                                         _________
''')
print("Welcome to London.")
print("Your mission is to reach Buckingham Palace.")

choice1 = input("You're at King's Cross, which Underground line will you choose?" "Type victoria or piccadilly \n"). lower()

if choice1 == "victoria":
    choice2 = input("You have reached Victoria, there is a post which says 'Buckingham Palace Road'. "
                    "Will you follow that road and try your luck on foot or will you start to look for a bus stop?" 
                    "Type 'foot' or 'busstop'\n"). lower()
    if choice2 == "busstop":
       choice3 = input("You find a bus stop which is nearby. Which bus will you take? Type '57', '68' or 'C10'\n "). lower()
       if choice3 == "C10":
           print("Congratulations, you reached your destination")
       elif choice3 == "57":
           print("Seems like you got lost mate. Try it again.")
       elif choice3 == "68":
           print("You met Boris Johnson on this bus, the two of you start to talk and you end up in a random East London pub. "
                 "Not a wise move.")
       else:
           print("You choose a bus that doesn't exist. You lost.")
    else: print("Really?")

else: print("Oh no! You got lost.")


