label day_3:

    ##SCENE ONE
    ##CHARACTERS - Elowyn, Jasper
    ##BACKGROUNDS - Town, Forest

    ##NARATOR
    play sound "audio/bgs/main_menu_town_bg.mp3"
    scene town with fade
    pause 2.0
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "Yesterday’s case was a bust. Elowyn would have tried harder had she been a more ambitious or honorable woman." 
    "Fortunately, she was nothing but a hungry one–which is what brought her to her trek in search of the bakery this morning."

    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "I’m thinking a muffin today. Chocolate or blueberry, though?"
    "???" "Meow!"
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Shoot! Jasper? Is that you?"
    "???" "Meow meow!"
    "???" "Meowwwww!"
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    pause 0.5
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "{i}No, the sounds are coming from different directions. Does Jasper have siblings he hasn’t told me about?{/i}"

    ##NARATOR
    "A cat darts out of the bushes, and scurries past Elowyn’s feet."

    show elowyn shocked at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Oh. An actual cat. I suppose I prefer this to the catboy."

    ##NARATOR
    "Elowyn would come to regret this statement."

    show elowyn smile at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "There’s another one over there. And two fighting by that lamppost. One by the bakery, three under that tree, five just darted out of that alleyway…hold on. Were there this many cats here before?"

    ##NARATOR
    "As a matter of fact, there were not."

    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "…I suppose I should handle this before the mayor finds out. I have an idea of who might know something about this anyway."

    ##NARATOR
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 2.5
    "With this in mind, Elowyn turns the opposite way and makes her way over to Jasper’s place on the outskirts of town. A quaint place, with its door currently scratched up."
    show elowyn neutral at sprite_size:
        xalign 2.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 1.0
    show jasper confused at sprite_size:
        alpha 0.0
        xalign 0.0
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    "A sharp knock is all it takes for the door to swing open, revealing an unusually frazzled Jasper. His tall frame is hunched. He’s missing his signature smile, and instead sports rumpled clothes and messy hair."

    show elowyn smile at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Wow. Looking good."
    jasper "Trying out comedy, Detective? Don’t quit your day job. If you’re here about the cats, let me start by saying it’s not anything I can help with."
    elowyn "I was actually just going to ask if you knew why there were so many at all, but now I’m thinking I should just pin it on you and call it a day."
    show jasper happy at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "You’re joking, right? I retract my previous statement. You’re hilarious, truly."
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Be serious, please."
    show elowyn neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show jasper confused at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "Well, I'd assume the whole town thinks it’s my fault at this point, so forgive me if I’m not too enthusiastic about this interrogation."
    show elowyn thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "So they’re the shelter cats, then? Why not help catch them and put them back, at least?"
    show jasper pleased at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    jasper "Thanks, genius. That’s what I was doing all night. There’s just too many, and the workers want to figure out who did it in the first place. Sounds like a case for YOU."
    show elowyn shocked at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Ack, the C-word! Not again!!!{/i}"
    show elowyn analyzing at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    elowyn "Right. Well, I guess I’d better get on that, then."



    ##SCENE TWO
    ##CHARACTERS - Elowyn, Paige
    ##BACKGROUNDS - Town, Library

    ##NARATOR
    play sound "audio/bgs/main_menu_town_bg.mp3"
    scene town with fade
    pause 2.0
    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "Elowyn departs with her back hunched, certainly not eager to get sent on yet another errand."

    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Who can I ask? Wait, doesn’t Paige volunteer at the shelter with Jasper? Although she’s certainly not the welcoming type…I’ll have to take my chances."
    play sound "audio/bgs/libary_bg.mp3"
    scene bg library with fade

    show paige surprised at sprite_size:
        alpha 0.0
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    show elowyn neutral at sprite_size:
        xalign -1.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.0
    paige "Back again, Detective? More stolen files? I promise it wasn’t me this time, as it wasn’t the last."
    show paige surprised at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Urk…{/i} Haha, nothing of the sort! Actually, I wanted to ask about the cat situation."
    show paige thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "Oh, yes. I know nothing about that. Good talk."
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Wait, wait, wait!! I’ll drop your name from yesterday’s situation, alright? And I’ll throw in a muffin from Crumblepuff’s! Just please, tell me anything you know!"
    paige "Hmmm… gosh, now that I think about it, I do remember the staff talking about how unusual it all was."
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Yes!!! In what way? In what way???"
    show paige neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "Patience. After they close, they lock all the doors except for one. Too small for people to get into, and cats can’t typically use handles."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Sorry for asking, but what’s the point of a door like that anyway?"
    paige "Apparently the late owner was small enough to go through, and so he made it for himself." 
    paige "Now, it’s used as an emergency door of sorts, although really only the shortest volunteers can crawl through, if really necessary. It leads to the main rooms."
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "{i}Only the shortest? But Jasper’s huge!{/i} Noted. And who was there last night?"
    show paige thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "As far as I know? Jasper. Not a good look, I’m sure."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "But then it would have to be him, no? Who else would be able to open the doors and let all the cats out?"
    show paige surprised at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "Dunno. But a donut might make me remember something else."
    show elowyn analyzing at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "…Go on."
    show paige neutral at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "How generous of you. Well after the shelter closes, opening the doors will make the alarm go off. It’s no big deal, it can be turned off if you know the password."
    show elowyn thinking at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "So…?"
    paige "Well, the alarm never went off last night. So the main doors were never opened."
    show elowyn shocked at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Which means the only door that the cats could have left from is the tiny emergency door {i}…which Jasper couldn’t get through!{/i}"
    show paige thinking at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "Who knows. You should, actually. Better get on that." 

    ##NARATOR
    show paige annoyed at sprite_size:
        xalign 1.0
        yalign 1.0
        yoffset 100
    "She blows smoke in her face."
    show elowyn smile at sprite_size:
        xalign 0.0
        yalign 1.0
        yoffset 100
    elowyn "Yes, ma’am…"



    ##SCENE THREE
    ##CHARACTERS - Elowyn, Paige, Jasper
    ##BACKGROUNDS - Town, Forest
    play sound "audio/bgs/main_menu_town_bg.mp3"
    scene town with fade
    pause 2.0

    show elowyn analyzing at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "I thought I made a breakthrough, but haven’t I only complicated this for myself?"
    elowyn "If I were a worse person I would have said Jasper and called it a day…too bad I’m not."
    elowyn "If the only way Jasper could’ve let the cats out undetected was through the small emergency door, then he would’ve had to leave through one of the main doors and trigger the alarm." 
    show elowyn thinking at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "He clearly made it home just fine…I should find out when he left."
    pause 1.0

    ##NARATOR
    scene forest with fade
    pause 2.0
    show elowyn neutral at sprite_size_four:
        xalign -0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign 0.5
    "With a promising new lead, Elowyn made her way back to Jasper’s house, only to find Paige already there, currently in a spat with the hooligan himself."

    show elowyn thinking at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
        ease 3.0 xalign -0.4
    show paige neutral at sprite_size_four:
        alpha 0.0
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    show jasper happy at sprite_size_four:
        alpha 0.0
        xalign 0.5
        yalign 1.0
        yoffset 100
        linear 2.0 alpha 1.0
    elowyn "{i}Maybe I’ll just listen for a bit…{/i}"
    show elowyn neutral at sprite_size_four:
        xalign -0.4
        yalign 1.0
        yoffset 100
    show jasper confused at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "Really? Now you think it’s me too?"
    show paige annoyed at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "All I asked was if there was someone else in the shelter when you left. Getting so defensive only makes you look guiltier."
    show jasper smile at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "That’s rich, coming from you. Why don’t you just put those files back where they belong?"
    show paige surprised at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "Are you really going there? You know damn well I didn’t do anything."
    show jasper pleased at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "And to think I defended you when the detective asked me about it. I should’ve told her I saw you skipping back home with an armful of papers. She seems gullible enough to believe me, maybe you would’ve been behind bars already."
    show elowyn analyzing at sprite_size_four:
        xalign -0.4
        yalign 1.0
        yoffset 100
    elowyn "{i}What the hell!?{/i}"
    show paige annoyed at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    paige "Just answer my question, Jasper."
    show jasper confused at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "Fine–I didn’t. I mean, I was asleep, but I was there until four in the morning. I only found out about the cats when the folks covering the morning shift found me and asked me where they went."
    paige "No wonder you can’t keep a job; you suck at volunteering too."
    jasper "Hypocrite. Your attitude makes people not wanna go to the library anymore. I bet you alone contribute to 90%% of this town’s illiteracy."
    paige "You can’t even spell 'illiteracy.'"
    show jasper pleased at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    jasper "No thanks to you."
    show elowyn thinking at sprite_size_four:
        xalign -0.4
        yalign 1.0
        yoffset 100
    elowyn "{i}So Jasper left the shelter this morning. That explains why no alarms were set off. Say he let the cats out via the emergency door…why wouldn’t he try and leave?"
    elowyn "{i}Anyone with half a brain cell would think to accuse him first. Something isn’t adding up.{/i}"

    ##NARATOR
    show elowyn shocked at sprite_size_four:
        xalign -0.4
        yalign 1.0
        yoffset 100
        ease 1.0 xalign 0.0
    "Lost in thought, Elowyn failed to notice the cat currently sneaking up behind her until it lunged at her shoelaces. She yelped, alerting both Paige and Jasper at once."
    
    show paige thinking at sprite_size_four:
        xalign 1.0
        yalign 1.0
        yoffset 100
    show jasper confused at sprite_size_four:
        xalign 0.5
        yalign 1.0
        yoffset 100
    paige "Eavesdropping now?"

    ##NARATOR
    show elowyn shocked at sprite_size_four:
        xalign 0.0
        yalign 1.0
        yoffset 100
        ease 3.0 xalign -1.5
    show paige thinking at sprite_size_four:
        alpha 1.0
        xalign 1.0
        yalign 1.0
        yoffset 100
        linear 3.0 alpha 0.0
    show jasper confused at sprite_size_four:
        alpha 1.0
        xalign 0.5
        yalign 1.0
        yoffset 100
        linear 3.0 alpha 0.0
    "Elowyn takes off running. She doesn’t stop until she gets to her car, where she slumps down inside."

    scene bg car with fade
    play sound "audio/bgs/office_car_bg.mp3"
    show elowyn thinking at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "I just don’t have enough evidence to prove it was Jasper…nor do I have a motive for him. I think this one is a bust, just like the last. At least the mayor didn’t hear about this yet."

    ##NARATOR
    show elowyn neutral at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    "Elowyn’s phone rings."

    show elowyn analyzing at sprite_size:
        xalign 0.5
        yalign 1.0
        yoffset 100
    elowyn "Crap."

    "Fin."

jump day_4