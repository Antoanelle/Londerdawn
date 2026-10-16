##VARIABLES
default case_1_picked = False
default case_2_picked = False
default case_3_picked = False
default case_4_picked = False

label day_4:

    ##SCENE ONE
    ##CHARACTERS - Elowyn, Ms. Crumblepuff, Paige, Jasper, Elliot
    ##BACKGROUNDS - Sleeping Quarters, Bakery

    ##NARATOR
    scene sleeping quarters with fade
    pause 2.0
    play sound "audio/sfx/smoke_sfx.mp3" loop
    show elowyn analyzing at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    pause 2.0
    show elowyn neutral at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    "When Elowyn woke up, she momentarily thought Paige might have been in her room. The strong smell of smoke wafted in, and it took another five minutes for her to realize it wasn’t coming from her room, but outside." 
    "She stumbles over to the window and spots smoke billowing from a certain building."

    show elowyn shocked at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.5
    elowyn "The bakery!?!? That’s the one good place here!!!"

    ##NARATOR
    scene town with fade
    play sound "audio/bgs/bakery_fire_bg.mp3" loop
    show crumblepuff shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 1.0
    pause 1.0
    show crumblepuff shocked at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.5
    pause 1.0
    show crumblepuff shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 1.0
    pause 1.0
    show crumblepuff shocked at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.5
    "Ms. Crumblepuff stands outside, flitting around her burning establishment as she chucks buckets of water at the building futilely."
    show crumblepuff shocked at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 1.0
    pause 1.0
    show crumblepuff shocked at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.5
    show elowyn shocked at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.0
    elowyn "Ms. Crumblepuff? What’s going on? Are you alright?"
    show crumblepuff sad at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    crumblepuff "My cakes! My ovens! Heaven’s sake, my clocks!!! I only stepped out for minute, and– and–"
    show elowyn thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Is anyone still inside?"
    crumblepuff "Yes! My pastries, the poor dears!!"
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Let’s just handle the fire first…{/i}"

    ##NARATOR
    "After Elowyn and several other townsfolk band together, they are able to tame the flames. However, they were unable to save the bakery from turning into a charred mess." 
    show elowyn neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 2.0
    hide crumblepuff with Dissolve(3.0)
    "After the heat died down enough, Elowyn made her way inside to investigate."
    play sound "audio/bgs/suspenseful_bg.mp3"
    scene bg bakery burnt with fade

    show elowyn thinking at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Not much to see here except for ash…honestly, how miserable do you have to be to burn down the bakery of all places?"

    ##NARATOR
    show elowyn neutral at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "She rummages around for a bit, before she finds something on the ground, miraculously only half burnt. A small, red button shaped like a heart."

    show elowyn thinking at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Hang on. This looks like it belongs to…well, the mayor." 

    ##NARATOR
    scene town with fade
    show crumblepuff sad at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show jasper happy at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset -200
    show paige neutral at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 200
    show elowyn neutral at sprite_size_four:
        xalign 1.5
        yalign 1.0
        yoffset 100
        xoffset 300
        ease 3.0 xalign 1.0
    "The crowd begins to thicken in front of the bakery. Elowyn straightens up to see the townsfolk already pointing fingers."

    show jasper happy at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "This is pretty eventful for a small town like ours. Hey, you didn’t burn down Crumblepuff’s place because she ratted you out, did you?"
    show paige surprised at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    paige "Crumblepuff’s statement was false, as far as I’m concerned. You sure YOU didn’t do it to divert the town’s attention from the kitty fiasco?"
    show jasper confused at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "I respect the cats. I would never do that, meow."
    show paige annoyed at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    paige "There he goes again…you’re not cute enough to get away with that."
    show crumblepuff pout at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.5 
    show jasper confused at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 2.0 xalign 0.0
    crumblepuff "Oh, don’t fight! First my bakery, now your friendship?"
    show jasper pleased at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "Paige & Jasper" "Shut up."
    show elowyn analyzing at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "It’s about time the mayor gets here, isn’t it? This is the biggest thing to happen in town all week. You’d think she’d be eager to take my head off."

    ##NARATOR
    show jasper pleased at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        linear 1.0 alpha 0.0
    show paige annoyed at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        linear 1.0 alpha 0.0
    show crumblepuff sad at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        linear 1.0 alpha 0.0
    show elliot neutral at sprite_size_four:
        xalign -2.5
        yalign 1.0
        yoffset 100
        ease 0.5 xalign 0.0
    "The person who jogs over is shockingly not the mayor, but instead Elliot. A figure who Elowyn had admittedly not seen in a hot minute, probably due to all the homework he incurred." 
    "He runs over with a bucket that is very much empty."

    show elliot shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "Detective! I came as soon as I heard! Oh, what a catastrophe, a catastrophe indeed! Is anyone hurt?"
    show elowyn thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Thankfully not. Where were you? And the mayor?"
    show elliot sad at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "Town hall, of course. Waiting for the mayor before I left, but she hadn’t arrived yet. Frankly, I’m worried about her."
    elowyn "You’re sure she’s not here?"
    show elliot neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "Very much so. Well, if it’s handled I suppose I’ll be back to the hall, then. I still have duties to fulfill, y’know."

    ##NARATOR
    show elliot angry at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
    pause 0.1
    show elliot neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 0.5 xalign -1.5
    "He shoots a pointed look towards Elowyn and trudges off before she can get a word in. The townsfolk remain tense, voices overlapping as fingers are pointed. Elowyn rubs her temples."

    show elowyn analyzing at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Let me just go back to the car."



    ##SCENE TWO
    ##CHARACTERS - Elowyn, Ms. Valentine
    ##BACKGROUNDS - Car

    ##NARATOR
    play sound "audio/bgs/office_car_bg.mp3"
    scene bg car with fade
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "Inside her car, Elowyn racks her brain."

    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Four cases in a row…there had to be something wrong. A connection."

    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    window show
    while not case_1_picked or not case_2_picked or not case_3_picked or not case_4_picked:
        menu:
            
            "{i}I should think back about the previous cases{/i}"
            "Day 1. Clock hands" if not case_1_picked:
                call case_1
                $ case_1_picked = True

            "Day 2. Missing files" if not case_2_picked:
                call case_2
                $ case_2_picked = True

            "Day 3. Cats escaping" if not case_3_picked:
                call case_3
                $ case_3_picked = True

            "Day 4. Burning bakery" if not case_4_picked:
                call case_4
                $ case_4_picked = True

    window auto

    elowyn "I guess I should try calling her, then…"

    ##NARATOR
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "{i}Elowyn rings Valentine, but the woman does not pick up.{/i}" 
    "{i}Instead, Elowyn receives a text: I am currently out of town to handle urgent matters. I will be back tomorrow. Please message me if it is important.{/i}"

    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Hang on…she’s out of town? But Elliot said he didn’t know where she went, and it was her button that I found in the bakery!"
    elowyn "I’ll brief her about what happened. There’s not much more I can do until I can really speak to her anyway. There’s something here, I can feel it."

    ##NARATOR
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "She rubs her eyes, shoulders sagging. Exhaustion tugs at her body from all directions."

    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "I’ll sleep on it. Tomorrow’s the last day. I can’t mess this up!"

    "Fin."

jump day_5


label case_1:
    elowyn "The only easy case. Elliot confessed pretty quickly, and said he did it so he could be late without people knowing."

return

label case_2:
    elowyn "Crumblepuff said she saw Paige at six hunched in her stripey suit, but Jasper said he was with her at the shelter at the same time. Both can’t be true, so either someone is lying, or the person Crumblepuff saw wasn’t Paige."

return

label case_3:
    elowyn "Jasper was the most likely culprit, being the only known person in the shelter at the time that the cats were released. However, he claims to have been asleep when it happened." 
    elowyn "Moreover, the only door the cats could’ve escaped through was the emergency door that Jasper is too big for. I find it hard to believe he would be stupid enough to stay in the building had he been the culprit."

return

label case_4:
    elowyn "Today’s fiasco. The bakery burned down. Elliot arrived with an empty bucket to “help with the fire,” and informed me that the mayor was nowhere to be found." 
    elowyn "What’s even worse is that the only evidence I found for who it may have been is the button…one of the mayor’s."

return
