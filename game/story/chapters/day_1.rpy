label day_1:

    ##SCENE ONE
    ##CHARACTERS - Elowyn, Elliot
    ##BACKGROUNDS - Car, Forest

    ##NARATOR
    "Elowyn has never had good luck, and today is no exception."
    "She finds herself on a foggy morning, stranded in the middle of nowhere with no signal and no sign of civilization."

    elowyn "{i}Today of all days my rustbucket gives up on me…I know you’re a decade old, but you couldn’t hold out just one more day!?{/i}"

    ###NARATOR
    "Arm fully extended, Elowyn wanders through the forest hoping to grab any ounce of signal she can get."

    "???" "Time waits for nobody…"
    elowyn "Huh… Am I going insane right now, or did I just hear someone?"
    "???" "Gosh, am I going to be late? Again? Today of all days!"
    elowyn "{i}Tell me about it. Wait, I should go after them, shouldn’t I? You know, do my job, and all…{/i}"

    ###NARATOR
    "She begins to follow this ominous voice in hope of getting some help, and finally comes across…"

    show elliot
    "???" "Woah! What on earth are you doing creeping around over there!? Stay back! Are you a friend of that hooligan? Mumbles. Does he even have any friends???"
    elowyn "Who…? Um, I think we got off on the wrong foot…I’m Detective Liddell. You can call me Elowyn, I was hoping you could point me in the direction of “Londerdawn”."

    ###NARATOR
    "He blinks in surprise, and his disdain seems to evaporate immediately at the news."

    "???" "Oh, so {i}you’re{/i} the detective! Why didn’t you just say so from the start!"

    ###NARATOR
    "The man checks the watch on his hand thrice in quick succession, the band a bold, ruby red."
    "{b}(Red Watch added to journal!){/b}"

    "???" "Well then, I’d be happy to lead the way Elise. Let's make haste!"
    elowyn "{i}Can anyone get my name right…{/i}"

    ###NARATOR
    "Before she can correct him, he bolts off with startling speed. She hurries after him, wondering how his stubby legs could move with such urgency."



    ##SCENE TWO
    ##CHARACTERS - Elowyn, Elliot, Jasper
    ##BACKGROUND - Forest

    ###NARATOR
    "It seems like out of nowhere, the town’s entrance materializes right before their eyes amidst the fog."
    "Near the outskirts that Elowyn spots a flash of movement in the trees. She spares a momentarily glance, and is met with a shiny, wide grin."

    show jasper
    "????" "Meow."
    elowyn "Woah!!! Who’s up there!?"
    $ jasper_name = "Jasper"
    jasper "Jasper. Who’s down there?"
    elowyn "This must be the {i}“hooligan.”{/i}"
    elowyn "Gosh, you scared me. I’m, uh, Elowyn."
    
    ###USER PICKS HOW THEY RESPOND TO JASPER 
    window show
    menu:
        jasper "Haha, what a stupid name! Nice to meet you, anyway."

        "Don’t you have anything better to do?":
            call questioning_option

        "Why don’t you get down here and meet my fists too!!!":
            call aggressive_option
    window auto

    elowyn "…This is nice and all, but I really do need to get going."
    jasper "See ya."
    elowyn "Whatever, man."
    hide jasper



    ##SCENE THREE
    ##CHARACTERS - Elowyn, Elliot, Victoria, Ms. Crumblepuff, Paige
    ##BACKGROUNDS - Bakery

    ###NARATOR
    "The town is quaint but lively, and the townsfolk seem to be in a tizzy. Elowyn has little time to examine before the man rushes off to a nearby building."

    elowyn "{i}A bakery? The smell is making my tummy rumble. Hang in there, bud!{/i}"
    "???" "Just around the corner!"

    ###NARATOR
    "The man stops at a small pavilion. Two people are seated, and a woman in a baker’s hat is pouring tea for them."

    "???" "Ms. Valentine! I found the detective ambling about in the woods!"

    show victoria
    elowyn "Well I wouldn’t put it like {i}that…{/i}"
    victoria "So you must be Elowyn! I am Victoria Valentine, the one who requested your services. "
    elowyn "Haha, guilty as charged! It’s a pleasure to–"
    victoria "Guilty, you say! I thought your job was to catch criminals, not be one!"
    elowyn "Um. It was a figure of speech, ma’am."
    victoria "And you’re VERY late, you know? Did Elliot lead you astray?"
    show crumblepuff
    crumblepuff "Oh, you’re such a hoot, Vicky! You told them to be here by six, and six it is!"
    $ elliot_name = "Elliot"
    elliot "Yes, what Ms. Crumblepuff said!"
    victoria "Don’t take me for a fool, Elliot! You know Crumblepuff’s clocks have read 6:00 pm since dinosaurs walked the planet! {b}(Crumblepuff’s Clocks added to journal!){/b}"
    hide elliot
    elliot "Oh, it looks like I left my watch at home. Excuse me while I go get it!"
    elowyn "{i}It was on his hand the whole time, though.{/i}"

    ###NARATOR
    "Elliot scurries off"

    show paige
    ###NARATOR
    "The other woman at the table huffs, smoke swirling around the table."

    crumblepuff "Don’t laugh, Paige! We can’t complain about my clocks when they’re the only ones that even work!"
    paige "Oh, I’m not complaining. I’m happy to watch the hour hand grow mold."
    elowyn "Sorry to cut in, but what’s wrong with the clocks?"

    ###NARATOR
    "Paige responds by blowing smoke straight into her face."

    victoria "Contrary to what Crumblepuff implied, it’s {i}her{/i} clocks that don’t work. As for the rest of us, it’s not a matter of damage. The issue is theft."
    elowyn "Someone stole your clocks? All of them?"
    crumblepuff "Wow, you really are a detective! Close, but not quite."

    ###USER PICKS HOW THEY REACT TO THE STOLEN HANDS
    window show
    menu:
        paige "They stole the hands. All of them. Well, almost all of them. I guess they didn’t see a point in taking Crumblepuff’s.{b}(Stolen Clock Hands added to journal!){/b}"

        "Wow, looks like someone had a lot of time on their hands. Heh.":
            call joking_option
        "Who has the time for that???":
            call confused_option
    window auto
    elowyn "Ahem." 
    



    ##SCENE FOUR
    ##CHARACTERS - Elowyn, Victoria
    ##BACKGROUNDS - Town
    hide paige
    hide crumblepuff

    ###NARATOR
    "Victoria stands up and walks away, and motions for Elowyn to follow her."

    victoria "Liddell, I want to stress how important it is for you to solve this case, and fast."
    elowyn "Right. I mean, the whole town is affected, however ridiculous the situation is."
    victoria "Correct. The townsfolk are growing restless. I fear if the culprit is not caught, their anger will turn to me."
    elowyn "You think they’ll blame you?"
    victoria "I think they’ll blame my incompetence as their mayor, yes."
    elowyn "That won’t be a problem, ma’am. I assure you, I’ll find the culprit!"
    victoria "Good. You have today."
    elowyn "Um. Just today?"
    victoria "Move with urgency, Elowyn. I suggest you start with the clock tower. Who knows what may happen if you delay."
    elowyn "Okay, start with the clocktower. Got it! I'm assuming this clock tower isn’t accessible to the public."
    victoria "That would be right. Elliot and I have a set of keys, but it has been quite a while since we’ve had to use them. Go fetch Elliot, he can lend you his. I’ve got things to do."

    

    ##SCENE FIVE
    ##CHARACTERS - Elowyn, Elliot
    ##BACKGROUNDS - Town

    ###NARATOR
    "Victoria shoos Elowyn away with the wave of a hand, and she takes off to find Elliot."
    hide victoria
    show elliot

    elowyn "Hey, I was wondering if you knew who has a key to open the door to the clocktower."
    elliot "The… The clocktower? Erm.. Why would you need to go all the way up there?"
    elowyn "Well, I'm here to investigate aren’t I? Plus, Victoria told me to start my investigation there."
    elliot "Right. Um, Well Victoria has a key, I know that for sure."
    elowyn "And you don’t?"
    elliot "I- You see- Um- They were… stolen. Someone stole it!"
    elowyn "Someone stole your key?"
    elliot "Yes, isn’t that rather unfortunate. {i}Glances at his watch{/i} Oh would you look at the time, im running late!"
    hide elliot

    ###NARATOR
    "Elliot prances off and Elowyn logs this information in her journal."
    "{b}(Elliot’s statement added to journal!){/b}"

    elowyn "{i}Victoria is under the assumption that Elliot still has his set of keys to the clocktower…if someone stole the keys from him, why hasn’t he told Victoria about it? Something isn’t adding up here.{/i}"

    ###NARATOR
    "Elowyn impulsively decides to chase after Elliot to get some answers."

    elowyn "ELLIOT! WAIT UP!!!"

    ###NARATOR
    "Upon hearing Elowyn's voice in the distance, Elliot hesitates for a moment and reluctantly slows down, allowing her to catch up."

    show elliot
    elliot "I really hav-"
    elowyn "{i}Breathing heavily{/i} Don’t you think you should tell Victoria that someone stole your set of keys? Whoever has them must be the one behind all of this."
    elliot "Well I-"
    elowyn "Now I have to figure out who stole your key in addition to the clockhands. Let me level with you–there’s no way I can solve this case by the end of the day. Let’s go tell Victoria right now. Maybe she’ll have some insights."
    elliot "Let’s? As in… we? I don’t think that is a good idea."

    ###NARATOR
    "He fidgets with his watch."

    elowyn "{i}Seriously? I’m scared of her too, y’know.{/i}"
    elowyn "Um, I guess I can go alone then."
    elliot "No, I mean I don’t think it’s necessary for you to tell the mayor. It would only agitate her more, you see, and she’s already VERY cross."
    elowyn "{i}…It’s clear as day this guy is hiding something from me. But why?{/i}"
    elowyn "Can I ask you something, Elliot? It’s obvious that asking Valentine about the keys will help me move forward with the investigation."
    elowyn "I’m sure the satisfaction of catching the culprit would outweigh the momentarily stress. Why are you stopping me?"
    elliot "Ms. Liddell, you’ve only been in the town an hour at best…you don’t understand why we’re all so eager to avoid her anger."
    elowyn "You haven’t answered my question."
    elliot "…Are you suspecting me, Detective?"
    elowyn "It’s not personal. Until we find the culprit, everyone is a suspect. {i}Wow, I sound tough.{/i} So? Why are you withholding information?"
    elliot "I’m not…you are twisting my words, surely…"
    elowyn "I’m taking a gamble here…Elliot. You’re the only other person who has direct access to the clock tower. If you’re telling the truth about your keys going missing, I can find them for you." 
    elowyn "But if not, allow me to ask a yes or no question. This is your last chance to fess up. {i}Sherlock has nothing on me!{/i} Did you steal the clock hands?"

    ###NARATOR
    "Elliot stares wide-eyed for a moment, his bottom lip trembling. He finally exhales, and pulls out a ring of keys from his pocket."

    elliot "I didn’t hurt anyone."
    elowyn "{i}Wait, seriously?{/i} You still committed a crime! {size=20}And, uh, why’d you do it?{/size}"
    elliot "It’s…a bit embarrassing."
    elowyn "I bet. Lay it on me."
    elliot "As I’m sure you’ve noticed, I am chronically late. If the town couldn’t see the time, then I could move as I pleased."
    elowyn "You’re serious? You know what year it is, right? We have digital clocks now."
    elliot "…"
    elowyn "{i}That’s it? Was it that easy?{/i}"
    
    hide elliot

    ###NARATOR
    "As it turned out, it was. Elowyn reported her findings to the Mayor immediately and she was shockingly lax with Elliot, choosing not to report him but instead assigning him an egregious amount of work. Elowyn was very glad she was not him!"

    jump day_2


###CHOICES     
label questioning_option:
    jasper "I’m unemployed."
    elowyn "Oh…I’m sorry."
    jasper "Don’t be, I’m right where I wanna be."

return


label aggressive_option:
    jasper "No thanks. I’m not eager to be a victim of police brutality, Detective."
    elowyn "I’m a private investigator, actually. Wait, how’d you know I'm a detective?"
    jasper "Secret."

return

label joking_option:
    "Everyone looks at each other, then back at her."

    elowyn"…I was joking."
    victoria "I’m glad you’re finding this funny."

return


label confused_option:
    paige "Isn’t it {i}your{/i} job to figure that out?"
    elowyn "It was a rhetorical question!"
    crumblepuff "Ah, rhetoric–wordplay, if you will. The pinnacle of art and the cornerstone of creation, the seed that sprouts innovation! Can I share some of my own rhetoric with you all?"
    paige "Let me see… Is the sky green?"

return


