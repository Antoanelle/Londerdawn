# VARIABLES
default computer_clicked = False
default file_clicked = False

label start:
    
    ##BEGINNING
    ##CHARACTERS - Elowyn, Boss
    ##BACKGROUNDS - Small office
    play music "audio/bgs/office_car_bg.mp3"

    scene small_desk with Dissolve(1.5)
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100

    ###NARATOR
    play sound "audio/sfx/door_knock_sfx.mp3"
    queue sound "audio/sfx/door_opening_sfx.mp3"
    queue sound "audio/sfx/paper_shuffled_sfx.mp3"
    "Elowyn sits at her new desk, sorting through paperwork and files. Her boss steps out of his office with a file in his hand."

    stop sound fadeout 5.0
    boss "Look alive, Elaine! I have a case for you."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}He still doesn’t know my name?{/i}"
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Another missing cat, Sir?"

    play sound "audio/sfx/paper_falling_sfx.mp3"
    ###NARATOR
    "He drops the folder onto her desk. Inside is a photograph of a small, unfamiliar town."

    boss "It’s your lucky day. Residents of Londerdawn have been complaining about this bizarre incident. The mayor has been pressuring us to solve this case. Even though it’s classified as low priority, we pushed it earlier in the work order."

    ###NARATOR
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "Boss seems to recall a bad memory. He looks like he just bit into a lemon."

    boss "That old bat is going to rush you for sure. Just try to get it done fast. Pin it on the mailman or something."
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Um… Yeah sure, I’ll get right on that sir."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    boss "{i}Sarcasm drips from his words.{/i}"
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    boss "Great, I knew I could count on your help. Good luck with that!"

    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
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

    show elowyn analyzing at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}What am I getting myself into…{/i}"
    hide elowyn analyzing
    jump day_1


###CHOICES
label computer:
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    ##NARATOR
    play sound "audio/sfx/computer_clicking_sfx.mp3" loop
    "He leaves abruptly. She turns to her computer and looks up Londerdawn"

    stop sound fadeout 5.0
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Ugh, what a mouthful…Hold on. I’m not getting any results! Is this a prank or something?{/i}"

return


label files:
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    ###NARATOR
    play sound "audio/sfx/paper_falling_sfx.mp3"
    "Elowyn opens the file and finds nothing but an address scrawled across the back of a receipt."
return
