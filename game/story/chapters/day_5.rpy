##VARIABLES
default give_answer = False
default think_more = False

label day_5:

##SCENE ONE
##CHARACTERS - Elowyn, Victoria, Elliot
##BACKGROUNDS - City Hall
    stop music
    scene bg day 5 with Dissolve(2.0)

    play sound "audio/bgs/office_car_bg.mp3"
    scene bg city hall
    pause 2.0
    show elowyn neutral at sprite_size_four:
        xalign 2.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    show victoria neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    show elliot neutral at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100

    "Elowyn walks into town hall a bit wary, Victoria already seated at her desk, tired but composed. Elliot stands beside her, checking his watch."

    victoria "Liddell. I received your message about the fire."
    elowyn "Yes ma’am. The bakery. Nobody was hurt, but the place is donezo." 
    victoria "Dreadful, truly. And to think I was gone for one day."
    show elowyn thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "On that note, I’d like to ask the both of you a few questions, if that’s alright. Starting with you, Ms. Valentine."
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "Be quick."
    elowyn "Where were you yesterday?"
    victoria "The county seat. I received a letter requesting my immediate attendance regarding the town’s budget. Urgent as it was, I took the first train."
    elowyn "And the meeting?"
    victoria "There wasn’t one. Nobody in the county office had any idea what I was talking about. I wasted an entire day, and I only returned a couple of hours ago."
    elowyn "I see…who sent you the letter then?"
    victoria "I don’t know. It was in my mail. Elliot sorts my mail."

    show elliot sad at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "Elliot straightens at the mention of him, clearing his throat."

    show elliot shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "I, well…I sort it, yes, that is true. But I certainly don’t read it, Mayor, anyone could have slipped such a thing in. An unruly prank, maybe?"
    victoria "Hm. Convenient that it came right before the fire."
    show elowyn neutral at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Okay, Ms. Valentine, I also found something in the bakery. Do you recognize this?"

    show elliot neutral at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "Elowyn holds up the remnants of the heart-shaped button."

    show victoria surprised at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "That’s from my coat, although it came off weeks ago. How did you get your hands on that?"
    show elowyn thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Weeks ago? You lost it?"
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "I handed it off to be repaired. Elliot, where did that coat of mine end up?"
    show elliot shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "Er, in the, um. The closet, I believe. I was meaning to send it off soon, but with all the work I had been getting, I simply haven’t had the time."
    show victoria angry at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "It’s a button, Elliot. If you didn’t want to take it down to the tailor, you could’ve sewn it back yourself. How long does it take to sew a button?"
    show elliot sad at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "I’m sorry, ma’am. Right away, ma’am."

    show elliot angry at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    pause 0.2
    show elliot neutral at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "He bows his head, jaw clenched."

    show elowyn analyzing at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Elliot. Yesterday, you told me you were at town hall waiting for the mayor to show up. Weren’t you the one who reminded her about her schedule that morning? I assume that would be your duty."
    elliot "I said I didn’t know where she went. I only knew she wasn’t here."
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "What? I left a note on your desk, Elliot. It mentioned where I’d be."
    show elliot shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "...Oh dear, I must have missed it."
    show elowyn thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Wait, what? Something is amiss. Maybe I can push my luck?"
    elowyn "And what about the bucket?"
    elliot "Pardon?"
    elowyn "The one you brought to aid the fire. It was empty."
    show elliot angry at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "I was going to fill it! There wasn’t an opportunity, I was just trying to get there first!"
    elowyn "Interesting. I recall a well only fifteen feet away, that’s how the rest of us filled our buckets."
    show elliot sad at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "Are you suggesting something, Detective?"
    elowyn "Not yet, just asking. I’ve heard enough for now. I need to think."

    play sound "audio/bgs/suspenseful_bg.mp3"
    show elowyn shocked at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show victoria angry at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    window show
    menu:
        victoria "Think!? The town is falling apart and I’m taking the heat for it, Liddell! I need answers NOW!"
        "Give an answer":
            $ give_answer = True
        "I need to think!!!":
            $ think_more = True

    if give_answer:
        menu:
            "Elliot":
                jump culprit_elliot
            "Jasper":
                jump bad_ending
            "Ms. Crumblepuff":
                jump bad_ending
            "Paige":
                jump bad_ending
            "Victoria":
                jump bad_ending

    if think_more:
        show elowyn neutral at sprite_size_four:
            xalign 1.0
            yalign 1.0
            yoffset 100

        elowyn "Please ma’am. I need to think. Just give me five minutes and I promise I can give you the culprit. Not just this case, but all of them."
        show victoria surprised at sprite_size_four:
            xalign 0.0
            yalign 1.0
            yoffset 100
        victoria "!"
        show victoria neutral at sprite_size_four:
            xalign 0.0
            yalign 1.0
            yoffset 100

        victoria "…Very well. Five minutes, no more."
        elowyn "Alright. From the top."
        elowyn "The first day. Elliot was the culprit, but…he confessed so quickly, and for such a silly reason. I let it go because it felt too easy, but what if it was supposed to feel easy?"
        elowyn "On the second day, Jasper and Crumblepuff both claimed Paige was at a different place at the same time."
        elowyn "The difference was that Jasper was allegedly with her, while Crumblepuff claims to have seen her–she saw someone hunched over in a stripey suit. Could someone else have been wearing that suit?"
        elowyn "On the third day, Jasper was the only one in the shelter when the cats were all let out. However, there was no way to leave through the main doors without triggering an alarm at that time, and the emergency door was too small for Jasper."
        show elowyn thinking at sprite_size_four:
            xalign 1.0
            yalign 1.0
            yoffset 100
        elowyn "If it isn’t him, who else is small enough?"
        elowyn "Finally, the fourth day. Crumblepuff’s bakery burst into flames and burnt down. The only evidence was the mayor’s heart button."
        elowyn "However, she wasn’t even in town when the crime happened, and she lost that button weeks ago. According to her, she received a fake letter which lured her away from town on the exact day of the fire."
        elowyn "If not her, who else would be able to plant that button, and who sent the letter?"
        elowyn "The townspeople don’t trust her. They're furious that she hasn’t done anything…was this the intention all along? Who would want this?"

        show elowyn shocked at sprite_size_four:
            xalign 1.0
            yalign 1.0
            yoffset 100
        "Elowyn pauses, her eyes widening."

        elowyn "Elliot."
        elowyn "It was never about the clocks. It’s always been about the chair: her chair. And I let him go because he seemed stupid and pathetic. Shame on you, Elowyn."
        show elowyn smile at sprite_size_four:
            xalign 1.0
            yalign 1.0
            yoffset 100
        show elliot sad at sprite_size_four:
            xalign 0.5
            yalign 1.0
            yoffset 100
        elowyn "Ma’am, the culprit is…"

        menu:
            "Elliot":
                jump good_ending


label culprit_elliot:
    show elliot shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elliot "!"
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    victoria "And what makes you say that?"
    elowyn "The first day. Elliot was the culprit, but…he confessed so quickly, and for such a silly reason. I let it go because it felt too easy, but what if it was supposed to feel easy? I suspect it was a distraction."
    elowyn "On the second day, Jasper and Crumblepuff both claimed Paige was at a different place at the same time."
    elowyn "The difference was that Jasper was allegedly with her, while Crumblepuff claims to have seen her–she saw someone hunched over in a stripey suit."
    elowyn "If someone else–someone smaller maybe–wore it, it would make sense why they looked “hunched,” and why there appeared to be two Paiges."
    elowyn "On the third day, Jasper was the only one in the shelter when the cats were all let out. However, there was no way to leave through the main doors without triggering an alarm at that time, and the emergency door was too small for Jasper."
    show elowyn thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "If it isn’t him, who else is small enough?"
    elowyn "Finally, the fourth day. Crumblepuff’s bakery burst into flames and burnt down. The only evidence was the mayor’s heart button."
    elowyn "However, she wasn’t even in town when the crime happened, and she lost that button weeks ago. According to her, she received a fake letter which lured her away from town on the exact day of the fire."
    elowyn "If not her, there’s only one other person who would be able to plant that button, and send the letter."
    elowyn "After all these incidents, the townspeople don’t trust you, Ma’am. They're furious that you haven’t done anything. Who would benefit from this other than your right hand man himself?"
    elowyn "He was eyeing your seat all along. After the townsfolk had enough of your “incompetence,” he would become their 'savior.'"
    show elowyn smile at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elliot sad at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Elliot, you’re the culprit!"

jump good_ending

