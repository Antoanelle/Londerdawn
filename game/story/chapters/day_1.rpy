label day_1:

    ##SCENE ONE
    ##CHARACTERS - Elowyn, Elliot
    ##BACKGROUNDS - Car, Forest

    ##NARATOR
    play music "audio/bgs/office_car_bg.mp3" 
    scene bg car with Dissolve(2.0)
    "Elowyn has never had good luck, and today is no exception."
    "She finds herself on a foggy morning, stranded in the middle of nowhere with no signal and no sign of civilization."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100

    play sound "audio/sfx/broken_car_sfx.mp3"
    elowyn "{i}Today of all days my rustbucket gives up on me… I know you’re a decade old, but you couldn’t hold out just one more day!?{/i}"

    stop sound fadeout 1.0
    ###NARATOR
    pause 1.0
    play music "audio/bgs/forest_bg.mp3"
    scene bg forest with fade
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 5 xalign 0.5
    "Arm fully extended, Elowyn wanders through the forest hoping to grab any ounce of signal she can get."

    "???" "Time waits for nobody…"
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Huh… Am I going insane right now, or did I just hear someone?"
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "???" "Gosh, am I going to be late? Again? Today of all days!"
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "{i}Tell me about it. Wait, I should go after them, shouldn’t I? You know, do my job, and all…{/i}"

    ###NARATOR
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "She begins to follow this ominous voice in hope of getting some help, and finally comes across…"
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 1 xalign 0.0
    show elliot angry at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 0.5 xalign 1.0
    "???" "Woah! What on earth are you doing creeping around over there!? Stay back! Are you a friend of that hooligan? Mumbles. Does he even have any friends???"
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Who…? Um, I think we got off on the wrong foot…I’m Detective Liddell. You can call me Elowyn, I was hoping you could point me in the direction of “Londerdawn”."

    ###NARATOR
    show elliot shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    "He blinks in surprise, and his disdain seems to evaporate immediately at the news."

    show elliot happy at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "???" "Oh, so {i}you’re{/i} the detective! Why didn’t you just say so from the start!"

    ###NARATOR
    "The man checks the watch on his hand thrice in quick succession, the band a bold, ruby red."
    "{b}(Red Watch added to journal!){/b}"

    "???" "Well then, I’d be happy to lead the way Elise. Let's make haste!"
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Can anyone get my name right…{/i}"

    show elliot happy at sprite_size:
        ease 0.5 xalign 1.5
    pause 0.5
    hide elliot
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    ###NARATOR
    "Before she can correct him, he bolts off with startling speed. She hurries after him, wondering how his stubby legs could move with such urgency."
    show elowyn shocked at sprite_size:
        ease 1.0 xalign 1.5
    pause 1.0
    hide elowyn shocked
    pause 2.0



    ##SCENE TWO
    ##CHARACTERS - Elowyn, Jasper
    ##BACKGROUND - Forest

    ###NARATOR
    scene bg forest with Dissolve(2.0)
    "It seems like out of nowhere, the town’s entrance materializes right before their eyes amidst the fog."

    play sound "audio/sfx/leaves_moving_sfx.mp3" loop
    show elliot happy at sprite_size:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 0.5 xalign 1.5
    pause 0.5
    hide elliot happy
    pause 0.5
    show elowyn neutral at sprite_size:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0
    "Near the outskirts that Elowyn spots a flash of movement in the trees. She spares a momentarily glance, and is met with a shiny, wide grin."
    stop sound fadeout 5.0

    show jasper smile at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    "????" "Meow."
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Woah!!! Who’s up there!?"
    show jasper happy at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    $ jasper_name = "Jasper"
    jasper "Jasper. Who’s down there?"
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "This must be the {i}“hooligan.”{/i}"
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Gosh, you scared me. I’m, uh, Elowyn."
    
    show jasper pleased at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elowyn analyzing at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    ###USER PICKS HOW THEY RESPOND TO JASPER 
    window show
    menu:
        jasper "Haha, what a stupid name! Nice to meet you, anyway."

        "Don’t you have anything better to do?":
            call questioning_option

        "Why don’t you get down here and meet my fists too!!!":
            call aggressive_option
    window auto

    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "…This is nice and all, but I really do need to get going."
    show jasper smile at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    jasper "See ya."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Whatever, man."
    show jasper smile at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 0.0
    show elowyn neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 3.5 xalign 2.0
    pause 3.0
    hide jasper smile 
    hide elowyn neutral
    pause 1.0



    ##SCENE THREE
    ##CHARACTERS - Elowyn, Elliot, Victoria, Ms. Crumblepuff, Paige
    ##BACKGROUNDS - Bakery
    play music "audio/bgs/main_menu_town_bg.mp3"
    scene town with Dissolve(2.0)
    ###NARATOR
    show elliot happy at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 1.5
    pause 1.0
    hide elliot happy
    "The town is quaint but lively, and the townsfolk seem to be in a tizzy. Elowyn has little time to examine before the man rushes off to a nearby building."
    
    show elowyn shocked at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.0
        pause 0.5
        ease 3.0 xalign 2.0
    elowyn "{i}A bakery? The smell is making my tummy rumble. Hang in there, bud!{/i}"
    show elliot happy at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elowyn neutral at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0

    "???" "Just around the corner!"

    play music "audio/bgs/bakery_bg.mp3"
    scene bakery with fade
    ###NARATOR
    show elowyn neutral at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        xoffset -200
        ease 3.0 xalign 0.0
    show elliot neutral at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        xoffset 200
        ease 3.0 xalign 0.0
    "The man stops at a small pavilion. Two people are seated, and a woman in a baker’s hat is pouring tea for them."

    show elliot happy at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
    "???" "Ms. Valentine! I found the detective ambling about in the woods!"

    show elowyn thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn "Well I wouldn’t put it like {i}that…{/i}"
    show victoria neutral at sprite_size_four:
        xalign 1.5
        yalign 1.0
        yoffset 100
        xoffset -200
        ease 3.0 xalign 1.0
    show elowyn neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show elliot happy at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
    victoria "So you must be Elowyn! I am Victoria Valentine, the one who requested your services."
    show elowyn smile at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn "Haha, guilty as charged! It’s a pleasure to–"
    show victoria angry at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset -200
    victoria "Guilty, you say! I thought your job was to catch criminals, not be one!"
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn "Um. It was a figure of speech, ma’am."
    victoria "And you’re VERY late, you know? Did Elliot lead you astray?"
    show crumblepuff smile at sprite_size_four:
        xalign 1.5
        yalign 1.0
        yoffset 100
        xoffset 250
        ease 2.0 xalign 1.0
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show elliot sad at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
    show victoria angry at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset -200
    crumblepuff "Oh, you’re such a hoot, Vicky! You told them to be here by six, and six it is!"
    $ elliot_name = "Elliot"
    show elliot shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
    elliot "Yes, what Ms. Crumblepuff said!"
    show elliot sad at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
    show crumblepuff pout at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 250
    victoria "Don’t take me for a fool, Elliot! You know Crumblepuff’s clocks have read 6:00 pm since dinosaurs walked the planet! {b}(Crumblepuff’s Clocks added to journal!){/b}"
    show elliot shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
    show crumblepuff happy at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 250
    elliot "Oh, it looks like I left my watch at home. Excuse me while I go get it!"
    show elliot neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 200
        ease 0.5 xalign -1.0
    pause 1.0
    show elowyn thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn "{i}It was on his hand the whole time, though.{/i}"

    ###NARATOR
    "Elliot scurries off"
    hide elliot 

    show victoria neutral at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0 xoffset 300
    show paige neutral at sprite_size_four:
        xalign 1.5
        yalign 1.0
        yoffset 100
        xoffset 200
        ease 3.0 xalign 1.0
    show elowyn neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show crumblepuff happy at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 250
        ease 3.0 xalign 0.5
    ###NARATOR
    "The other woman at the table huffs, smoke swirling around the table."

    show paige annoyed at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 200
    show crumblepuff pout at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 250
    crumblepuff "Don’t laugh, Paige! We can’t complain about my clocks when they’re the only ones that even work!"
    show paige thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 200
    paige "Oh, I’m not complaining. I’m happy to watch the hour hand grow mold."
    show elowyn thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show crumblepuff happy at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 250
    elowyn "Sorry to cut in, but what’s wrong with the clocks?"

    ###NARATOR
    play sound "audio/sfx/smoke_sfx.mp3" loop
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show paige annoyed at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 200
    "Paige responds by blowing smoke straight into her face."

    stop sound
    show elowyn neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show victoria neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 300
    victoria "Contrary to what Crumblepuff implied, it’s {i}her{/i} clocks that don’t work. As for the rest of us, it’s not a matter of damage. The issue is theft."
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn "Someone stole your clocks? All of them?"
    show crumblepuff smile at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 250
    crumblepuff "Wow, you really are a detective! Close, but not quite."

    show paige thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 200
    show elowyn thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    ###USER PICKS HOW THEY REACT TO THE STOLEN HANDS
    window show
    menu:
        paige "They stole the hands. All of them. Well, almost all of them. I guess they didn’t see a point in taking Crumblepuff’s.{b}(Stolen Clock Hands added to journal!){/b}"

        "Wow, looks like someone had a lot of time on their hands. Heh.":
            call joking_option
        "Who has the time for that???":
            call confused_option
    window auto
    play music "audio/bgs/bakery_bg.mp3"
    show elowyn neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    show victoria neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 300
    show crumblepuff happy at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 250
    elowyn "Ahem." 
    pause 1.0

    

    ##SCENE FOUR
    ##CHARACTERS - Elowyn, Victoria
    ##BACKGROUNDS - Town

    ###NARATOR
    "Victoria stands up and walks away, and motions for Elowyn to follow her."
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 300
        ease 3.0 xalign -1.0
    show elowyn neutral at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
        ease 3.0 xalign -1.0
    pause 2.0

    scene town with fade
    play music "audio/bgs/main_menu_town_bg.mp3"
    show victoria neutral at sprite_size:
        xalign 1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    show elowyn neutral at sprite_size:
        xalign 1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0
    victoria "Liddell, I want to stress how important it is for you to solve this case, and fast."
    elowyn "Right. I mean, the whole town is affected, however ridiculous the situation is."
    victoria "Correct. The townsfolk are growing restless. I fear if the culprit is not caught, their anger will turn to me."
    show victoria thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "You think they’ll blame you?"
    victoria "I think they’ll blame my incompetence as their mayor, yes."
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "That won’t be a problem, ma’am. I assure you, I’ll find the culprit!"
    show victoria neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    victoria "Good. You have today."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Um. Just today?"
    victoria "Move with urgency, Elowyn. I suggest you start with the clock tower. Who knows what may happen if you delay."
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Okay, start with the clocktower. Got it! I'm assuming this clock tower isn’t accessible to the public."
    victoria "That would be right. Elliot and I have a set of keys, but it has been quite a while since we’ve had to use them. Go fetch Elliot, he can lend you his. I’ve got things to do."
    pause 1.0

    

    ##SCENE FIVE
    ##CHARACTERS - Elowyn, Elliot
    ##BACKGROUNDS - Town

    ###NARATOR
    "Victoria shoos Elowyn away with the wave of a hand, and she takes off to find Elliot."
    show victoria neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 3.0 alpha 0.0
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign -1.0
    pause 3.0
    hide victoria
    hide elowyn

    scene town with fade
    show elliot neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    show elowyn neutral at sprite_size:
        xalign 1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    elowyn "Hey, I was wondering if you knew who has a key to open the door to the clocktower."
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "The… The clocktower? Erm.. Why would you need to go all the way up there?"
    elowyn "Well, I'm here to investigate aren’t I? Plus, Victoria told me to start my investigation there."
    elliot "Right. Um, Well Victoria has a key, I know that for sure."
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "And you don’t?"
    elliot "I- You see- Um- They were… stolen. Someone stole it!"
    elowyn "Someone stole your key?"
    elliot "Yes, isn’t that rather unfortunate. {i}Glances at his watch{/i} Oh would you look at the time, im running late!"

    ###NARATOR
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 0.5 xalign -1.5
    "Elliot prances off and Elowyn logs this information in her journal."
    "{b}(Elliot’s statement added to journal!){/b}"
    hide elliot


    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Victoria is under the assumption that Elliot still has his set of keys to the clocktower…if someone stole the keys from him, why hasn’t he told Victoria about it? Something isn’t adding up here.{/i}"

    ###NARATOR
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign -1.5
    "Elowyn impulsively decides to chase after Elliot to get some answers."
    show elowyn shocked at sprite_size:
        xalign 1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    show elliot neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "ELLIOT! WAIT UP!!!"

    ###NARATOR
    "Upon hearing Elowyn's voice in the distance, Elliot hesitates for a moment and reluctantly slows down, allowing her to catch up."
    show elliot sad at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "I really hav-"
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Breathing heavily{/i} Don’t you think you should tell Victoria that someone stole your set of keys? Whoever has them must be the one behind all of this."
    elliot "Well I-"
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Now I have to figure out who stole your key in addition to the clockhands. Let me level with you–there’s no way I can solve this case by the end of the day. Let’s go tell Victoria right now. Maybe she’ll have some insights."
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "Let’s? As in… we? I don’t think that is a good idea."

    ###NARATOR
    show elliot sad at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "He fidgets with his watch."

    elowyn "{i}Seriously? I’m scared of her too, y’know.{/i}"
    elowyn "Um, I guess I can go alone then."
    show elliot neutral at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "No, I mean I don’t think it’s necessary for you to tell the mayor. It would only agitate her more, you see, and she’s already VERY cross."
    elowyn "{i}…It’s clear as day this guy is hiding something from me. But why?{/i}"
    play music "audio/bgs/suspenseful_bg.mp3"
    elowyn "Can I ask you something, Elliot? It’s obvious that asking Valentine about the keys will help me move forward with the investigation."
    elowyn "I’m sure the satisfaction of catching the culprit would outweigh the momentarily stress. Why are you stopping me?"
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "Ms. Liddell, you’ve only been in the town an hour at best…you don’t understand why we’re all so eager to avoid her anger."
    elowyn "You haven’t answered my question."
    elliot "…Are you suspecting me, Detective?"
    elowyn "It’s not personal. Until we find the culprit, everyone is a suspect. {i}Wow, I sound tough.{/i} So? Why are you withholding information?"
    show elliot sad at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "I’m not…you are twisting my words, surely…"
    elowyn "I’m taking a gamble here…Elliot. You’re the only other person who has direct access to the clock tower. If you’re telling the truth about your keys going missing, I can find them for you." 
    elowyn "But if not, allow me to ask a yes or no question. This is your last chance to fess up. {i}Sherlock has nothing on me!{/i} Did you steal the clock hands?"

    
    ###NARATOR
    play sound "audio/sfx/key_shaking_sfx.mp3"
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    "Elliot stares wide-eyed for a moment, his bottom lip trembling. He finally exhales, and pulls out a ring of keys from his pocket."

    play music "audio/bgs/main_menu_town_bg.mp3"
    show elliot sad at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "I didn’t hurt anyone."
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Wait, seriously?{/i} You still committed a crime! {size=20}And, uh, why’d you do it?{/size}"
    elliot "It’s…a bit embarrassing."
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "I bet. Lay it on me."
    elliot "As I’m sure you’ve noticed, I am chronically late. If the town couldn’t see the time, then I could move as I pleased."
    elowyn "You’re serious? You know what year it is, right? We have digital clocks now."
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elliot "…"
    show elliot sad at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}That’s it? Was it that easy?{/i}"
    
    show elliot shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
        linear 3.0 alpha 0.0
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 3.0 alpha 0.0

    ###NARATOR
    "As it turned out, it was. Elowyn reported her findings to the Mayor immediately and she was shockingly lax with Elliot, choosing not to report him but instead assigning him an egregious amount of work." 
    "Elowyn was very glad she was not him!"
    hide elliot
    hide elowyn
    pause 2.0
    jump day_2


###CHOICES     
label questioning_option:
    show jasper happy at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    jasper "I’m unemployed."
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Oh…I’m sorry."
    show jasper pleased at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    jasper "Don’t be, I’m right where I wanna be."

return


label aggressive_option:
    show jasper confused at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    jasper "No thanks. I’m not eager to be a victim of police brutality, Detective."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "I’m a private investigator, actually. Wait, how’d you know I'm a detective?"
    show jasper pleased at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    jasper "Secret."

return

label joking_option:
    stop music
    show elowyn smile at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    "Everyone looks at each other, then back at her."

    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn"…I was joking."
    show victoria thinking at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset 300
    victoria "I’m glad you’re finding this funny."

return


label confused_option:
    show paige annoyed at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 200
    paige "Isn’t it {i}your{/i} job to figure that out?"
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        xoffset -200
    elowyn "It was a rhetorical question!"
    show crumblepuff smile at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 250
    crumblepuff "Ah, rhetoric–wordplay, if you will. The pinnacle of art and the cornerstone of creation, the seed that sprouts innovation! Can I share some of my own rhetoric with you all?"
    show crumblepuff pout at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        xoffset 250
    show paige thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
        xoffset 200
    paige "Let me see… Is the sky green?"

return

