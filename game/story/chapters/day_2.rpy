##VARIABLES
default bakery_picked = False
default car_picked = False
default menu_dialogue = ""

label day_2:

    ##SCENE ONE
    ##CHARACTERS - Elowyn, Elliot
    ##BACKGROUNDS - Sleeping quarters

    ##NARATOR 
    scene sleeping quarters
    play music "audio/bgs/morning_bg.mp3"
    play sound "audio/sfx/door_knock_sfx.mp3" loop
    pause 2.0
    show elowyn analyzing at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    pause 3.0
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    play sound "audio/sfx/door_knock_sfx.mp3"
    "There is a loud banging on the door of Elowyns sleeping quarters. She jumps awake and scrambles to collect herself before answering. Elliot's figure appears as the door creaks open"

    show elliot neutral at sprite_size:
        xalign -1.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.0
    elowyn "{i}Rubbing her eyes {/i} Elliot, is that you? What are you doing here? What time is it?"
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "Good morning. Time is of the essence! I hate to be the bearer of bad news but… we kind of have a situation at the library and Mayor Valentine needs your assistance right this minute."
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "What kind of situation? My boss is expecting my return today."
    elliot "Yes, I understand that, but something catastrophic has happened. All of the townsfolk’s confidential files have gone missing."
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Missing? What do you m-"
    elliot "Quickly, we really must go now!"

    ##NARATOR 
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign -1.5
    "Elowyn changes into a new pair of clothes, slips on her shoes, swipes paperwork that is lying on the desk into her bag, and closes the door behind her"
    hide elliot



    ##SCENE TWO
    ##CHARACTERS - Elowyn, Victoria, Elliot
    ##BACKGROUNDS - City Hall
    play music "audio/bgs/office_car_bg.mp3"
    scene bg city hall with fade
    pause 2.0
    show victoria thinking at sprite_size_four:
        alpha 0.0
        xalign 0.0
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    show elowyn neutral at sprite_size_four:
        alpha 0.0
        xalign 0.5
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    show elliot sad at sprite_size_four:
        alpha 0.0    
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    pause 3.0
    show victoria neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "Liddell, where were you! At this rate the files are halfway out the city already!"
    
    show elowyn smile at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Let’s not panic. We can resolve this!"
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "How can we resolve this before anyone finds out?! People will surely figure out what has happened any second now. THIS IS ALL PAIGE’S FAULT. I’ve always known that woman was up to no good."
    show elowyn thinking at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    show elliot happy at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Paige? What makes you say that?"
    show elliot neutral at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    victoria "Well she’s the one in charge of organizing and upkeeping the fileroom over at the library. She is the only librarian in this town afterall, and since I don’t believe Elliot is capable enough to handle all that paperwork, I entrusted her instead."

    ##NARATOR 
    show elliot sad at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    "Elliot makes a face, but doesn’t protest otherwise."

    show elliot neutral at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Very well then… I will go speak with Paige and possibly a few other people to get a better understanding of what is going on."
    show victoria neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "I knew I could count on you!"

    ##NARATOR 
    show elliot sad at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show victoria angry at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "She gives Elliot a thinly veiled look of disgust that he shrivels under. After the stunt he pulled, it’s no wonder she isn’t happy with him."



    ##SCENE THREE
    ##CHARACTERS - Elowyn, Paige, Ms. Crumblepuff, Jasper
    ##BACKGROUNDS - Library, Town, Bakery, Forest
    play music "audio/bgs/library_bg.mp3"

    ##NARATOR
    scene bg library with fade
    pause 2.0
    show paige neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elowyn neutral at sprite_size:
        xalign -1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0
    "Elowyn pays Paige a visit over at the library. When she walks through the door she find Paige dusting the shelves"

    paige "Talk to the receptionist up front, please."
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Oh, no, it’s me!  Y’know, the detective."
    show paige annoyed at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "You didn’t hear me the first time? Receptionist. Up front."

    ##NARATOR
    "The receptionist at the front desk offers a cheerful wave."

    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Geez. I actually have business with you, specifically."
    show paige neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "I get off at six."
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Oh, well…I guess we can meet then?"
    paige "Oh, no I’m not free after either."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Um. Right. Well, when would you be–"

    ##NARATOR
    play sound "audio/sfx/smoke_sfx.mp3" loop
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "Paige takes a large whiff from her pipe and blows it right into Elowyn’s face. Elowyn sputters and flails about."

    show paige annoyed at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "You’d think a detective would be better at taking a hint. Buzz off, Ellie."

    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign -1.5
    pause 2.0
    ##NARATOR
    play music "audio/bgs/main_menu_town_bg.mp3"
    scene town with fade
    show elowyn neutral at sprite_size:
        xalign 1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.5
    pause 2.0
    "And buzz off she did. Elowyn wandered around the town a bit, trying to find a way to continue the investigation when her primary suspect was just so unwilling to talk."

    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "{i}Should I try again after her shift? No, I don’t think she’ll speak to me at all. I guess I could head to the bakery for a treat…or maybe I can just sit in my car.{/i}"

    window show
    while not bakery_picked or not car_picked: 
        if not bakery_picked and not car_picked:
            $ menu_dialogue = "{i}What should I do?{/i}"
        else:
            $ menu_dialogue = "{i}What should I do now?{/i}"
        menu:
            "[menu_dialogue]"
            "Pig out at the bakery" if not bakery_picked:
                call bakery_scene
                $ bakery_picked = True

            "Bum around in the car" if not car_picked:
                call car_scene
                $ car_picked = True
    window auto
    
    scene town with fade 
    pause 2.0
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    pause 0.5
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "I’ve run into a dead end… {i}Crumblepuff claims she saw Paige head towards town hall at six, but Jasper says he was with her.{/i}"
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        pause 0.5
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "{i}Is one of them lying? Or is Paige really not the culprit…? No, she’s the only one it could’ve been, according to the mayor. Gah! My head!!!{/i}"
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        pause 0.5
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "I thought Paige was the one, but I can’t accuse her like this at all…There’s nothing I can do anymore."
    hide elowyn

    ##NARATOR
    "Unfortunately, Elowyn’s fear came true. There was not enough evidence to prove Paige’s innocence or accuse her of being guilty. The files remained missing, and the mayor was livid."
    "Elowyn understood why Elliot was eager to avoid her, at least. She would go home at least. She solved the case her boss gave her, and that was enough."
    "This would be the last of this terrible town…right? Right???"

    "Fin."
    pause 2.0

    jump day_3   


label bakery_scene:
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "{i}I’m too hungry to think right now. Maybe I can ask the baker some questions while I’m at it.{/i}"

    play music "audio/bgs/bakery_bg.mp3"
    scene bg bakery second with fade
    ##NARATOR
    show elowyn neutral at sprite_size:
        xalign 1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    show crumblepuff happy at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "Elowyn makes her way over and ducks inside, seating herself at a quaint table. The clocks reads 6:00 pm as usual, which is somewhat comforting."

    show crumblepuff smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    crumblepuff "Hello Sugar!"
    show elowyn smile at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}I’m liking this nickname{/i}. Nice to see you again. Mind if I grab a slice of cake and a drink? Dealer’s choice."
    crumblepuff "Yes, ma’am! I’ll give you the best I’ve got!"
    elowyn "{i}She’s so nice…a breath of fresh air in a town like this.{/i}"
    elowyn "And um, also a couple of questions, if you’d allow it?"
    crumblepuff "I don’t see why not. Just doing your job, aren’t you?"
    elowyn "Yep! I appreciate your help. Well, I just wanted to ask about Paige, mainly what she was doing yesterday. Any information would be helpful."
    show crumblepuff smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    crumblepuff "Let me think…Oh, I think I did! She was heading towards the town hall I think, at around six."
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    pause 0.5
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Wait, seriously? Okay…but um, no offense, could you tell me the actual time? Not what your clocks say."
    show crumblepuff pout at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    crumblepuff "Rude!!! For your information, I wasn’t even at the bakery! The clock said six on the clock, on my phone, and the tower too."
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    pause 0.5
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Wait…Didn’t Paige say she got off work at six? If she wasn’t lying about that, then the timings match up!{/i}"
    elowyn "Are you sure?"
    show crumblepuff happy at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    crumblepuff "Well, it certainly looked like her. Had her cute stripey suit on, although she was hunched over a little funny."
    show elowyn neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Noted…"

return


label car_scene:
    elowyn "{i}I just need to get away from all of this for a bit. Some time with my baby should fix this.{/i}"

    ##NARATOR
    play music "audio/bgs/forest_bg.mp3"
    scene bg forest with fade
    pause 2.0
    play sound "audio/sfx/leaves_moving_sfx.mp3"
    show elowyn neutral at sprite_size:
        alpha 0.0
        xalign 0.5
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    "Elowyn treks back around to the woods, hoping for an uneventful journey back to the car. Unfortunately, Elowyn’s life had never been so forgiving and she was immediately startled by a voice from the trees."
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    show jasper happy at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0
    jasper "Hey. Heading home?"
    elowyn "I wish. Just taking a break. I’m guessing I don’t have to ask you about what you’re doing."
    show jasper confused at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "I resent that. I’m actually an active member of the community, believe it or not. I’m sure you wouldn’t know anything about that."
    show elowyn analyzing at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}This freaking guy{/i}…Oh yeah? In what way?"
    show jasper confused at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    pause 0.5
    show jasper happy at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "Interrogating me? I’ll allow it. I’m a volunteer at the animal shelter, ma’am. Work with the kitties, meow"
    show elowyn analyzing at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    pause 0.5
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}I really wish he’d stop doing that.{/i} Sure. Actually, while you’re here, did you see Paige yesterday? Notice anything different about her, was she acting weird?"
    show jasper confused at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "Wait, you think she’s the culprit? You’re a newbie, aren’t you? Take my advice, she’s not."
    elowyn "Sorry? And why wouldn’t she be?"
    show jasper happy at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "She’s a little embarrassed to admit this, but she’s a cat person. That’s why she’s always hanging out with me, haha."
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "She is?"
    show jasper confused at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "But, no, seriously–she volunteers with me. She was with me the other day, too."
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Are you sure? What time?"
    show jasper happy at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "Yep. Six, usually. Don’t tell her I told you, though. She gets crabby."
    show elowyn neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Gotcha…I’ll keep this in mind."

return