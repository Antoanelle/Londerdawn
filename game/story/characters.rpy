## Characters present within the script are intialized here

default elliot_name = "???"
default jasper_name = "????"

define elowyn = Character(_("Elowyn"), color="#ffffff")
define elliot = Character("[elliot_name]", dynamic=True, color="#ffffff")
define victoria = Character(_("Ms. Valentine"), color="#ffffff")
define jasper = Character(_("[jasper_name]"), dynamic = True, color="#ffffff")
define crumblepuff = Character(_("Ms. Crumblepuff"), color="#ffffff")
define paige = Character(_("Paige"), color="#ffffff")
define boss = Character(_("Boss"), color="#ffffff")


image elowyn neutral = "images/sprites/elowyn_neutral.png"
image elowyn smile = "images/sprites/elowyn_smile.png"
image elowyn shocked = "images/sprites/elowyn_shocked.png"
image elowyn thinking = "images/sprites/elowyn_thinking.png"
image elowyn analyzing = "images/sprites/elowyn_analyzing.png"

image elliot neutral = "images/sprites/elliot_neutral.png"
image elliot angry = "images/sprites/elliot_angry.png"
image elliot happy = "images/sprites/elliot_happy.png"
image elliot sad = "images/sprites/elliot_sad.png"
image elliot shocked = "images/sprites/elliot_shocked.png"

image jasper confused = "images/sprites/jasper_confused.png"
image jasper happy = "images/sprites/jasper_happy.png"
image jasper pleased = "images/sprites/jasper_pleased.png"
image jasper smile = "images/sprites/jasper_smile.png"

image paige annoyed = "images/sprites/paige_annoyed.png"
image paige neutral = "images/sprites/paige_neutral.png"
image paige surprised = "images/sprites/paige_surprised.png"
image paige thinking = "images/sprites/paige_thinking.png"

image victoria angry = "images/sprites/victoria_angry.png"
image victoria neutral = "images/sprites/victoria_neutral.png"
image victoria surprised = "images/sprites/victoria_surprised.png"
image victoria thinking = "images/sprites/victoria_thinking.png"

#Missing crumblepuff

transform sprite_size:
    zoom 0.60

transform sprite_size_four:
    zoom 0.5

