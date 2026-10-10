# VARIABLES
default computer_clicked = False
default file_clicked = False

label start:
    scene work_in_progress
    "Hi! Our game is a work-in-progess, so check back another time :)"
return


label real_one:
    ##BEGINNING
    ##CHARACTERS - Elowyn, Boss
    ##BACKGROUNDS - Small office

    scene small_desk with Dissolve(1.5)

    show elowyn

    #Input paper sound effects, door knocking and entering
    ###NARATOR
    "Elowyn sits at her new desk, sorting through paperwork and files. Her boss steps out of his office with a file in his hand."

    boss "Look alive, Elaine! I have a case for you."
    elowyn "{i}He still doesn’t know my name?{/i}"
    elowyn "Another missing cat, Sir?"

    #Input something hitting the desk and paper sound effects
    ###NARATOR
    "He drops the folder onto her desk. Inside is a photograph of a small, unfamiliar town."

    boss "It’s your lucky day. Residents of Londerdawn have been complaining about this bizarre incident. The mayor has been pressuring us to solve this case. Even though it’s classified as low priority, we pushed it earlier in the work order."

    ###NARATOR
    "Boss seems to recall a bad memory. He looks like he just bit into a lemon."

    boss "That old bat is going to rush you for sure. Just try to get it done fast. Pin it on the mailman or something."
    elowyn "Um… Yeah sure, I’ll get right on that sir."
    boss "{i}Sarcasm drips from his words.{/i}"
    boss "Great, I knew I could count on your help. Good luck with that!"

    elowyn "Right…"
    window show
    while not computer_clicked or not file_clicked:
        menu:
            "{i}What should I do next?{/i}"
            
            "Search on computer" if not computer_clicked:
                call computer
                $ computer_clicked = True
            "Investigate file" if not file_clicked:
                call files
                $ file_clicked = True
    window auto

    #Input computer typing sounds
    #Extra: Have the user input into the computer the town, if the user types right the game continues

    #When the user clicks on both items, the game moves on
    elowyn "{i}What am I getting myself into…{/i}"

    jump day_1


###CHOICES
label computer:
    scene computer_screen
    ##NARATOR
    "He leaves abruptly. She turns to her computer and looks up Londerdawn"

    elowyn "{i}Ugh, what a mouthful…Hold on. I’m not getting any results! Is this a prank or something?{/i}"
return


label files:
    ###NARATOR
    "Elowyn opens the file and finds nothing but an address scrawled across the back of a receipt."

return
