################################################################################
## In-game screens
################################################################################

## Say, Input, Choice, and Quick Menu Screens

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        background(
            Image("images/dialogue/textbox_light_blue.png", xalign=0.5, ypos=0) if who == "Elowyn"
            else Image("images/dialogue/textbox_light_yellow.png", xalign=0.5, ypos=0) if who in("Elliot", "???") 
            else Image("images/dialogue/textbox_light_red.png", xalign=0.5, ypos=0) if who == "Ms. Valentine"
            else Image("images/dialogue/textbox_light_green.png", xalign=0.5, ypos=0) if who in("Jasper", "????")
            else Image("images/dialogue/textbox_light_orange.png", xalign=0.5, ypos=0) if who == "Ms. Crumblepuff"
            else Image("images/dialogue/textbox_light_purple.png", xalign=0.5, ypos=0) if who == "Paige"
            else Image("images/dialogue/textbox_light_blue.png", xalign=0.5, ypos=0)
            ) 
            
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                background (
                    Frame("images/dialogue/namebox_blue.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) if who == "Elowyn"
                    else Frame("images/dialogue/namebox_yellow.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) if who in("Elliot", "???") 
                    else Frame("images/dialogue/namebox_red.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) if who == "Ms. Valentine"
                    else Frame("images/dialogue/namebox_green.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) if who in("Jasper", "????")
                    else Frame("images/dialogue/namebox_orange.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) if who == "Ms. Crumblepuff"
                    else Frame("images/dialogue/namebox_purple.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) if who == "Paige"
                    else Frame("images/dialogue/namebox_blue.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                )  
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #background Frame("images/dialogue/namebox_blue.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name")
    color "#ffffff"
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice
screen choice(items):
    style_prefix "choice"
   
    vbox:
        at choice_fade_in
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xpos 1300
    ypos 580
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background "images/choice_light_idle.png"
    hover_background "images/choice_light_hover.png"
    insensitive_background "images/choice_light_disabled.png"

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    xmaximum gui.choice_button_width
    xpos 150
    yalign 0.5

transform choice_fade_in:
    alpha 0.0
    linear 0.1 alpha 1.0


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

default quick_menu = True

screen quick_menu():
    default auto_clicked = False

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        fixed:
            #style_prefix "quick"
            #style "quick_menu"
            xfill True
            yfill True

            vbox:
                xpos 380
                ypos 825
                spacing 10

                imagebutton:
                    idle "images/gui/btn_light_history_idle.png"
                    hover "images/gui/btn_light_history_hover.png"
                    action ShowMenu('history')

                imagebutton:
                    idle "images/gui/btn_light_save_idle.png"
                    hover "images/gui/btn_light_save_hover.png"
                    action ShowMenu('save')

                imagebutton:
                    idle "images/gui/btn_light_options_idle.png"
                    hover "images/gui/btn_light_options_hover.png"
                    action ShowMenu('preferences')

            vbox:
                xpos 1470
                ypos 825
                spacing 10

                imagebutton:
                    idle "images/gui/btn_light_skip_idle.png"
                    hover "images/gui/btn_light_skip_hover.png"
                    action Skip() alternate Skip(fast=True, confirm=True)

                imagebutton:
                    idle "images/gui/btn_light_continue_idle.png"
                    hover "images/gui/btn_light_continue_hover.png"
                    selected_idle "images/gui/btn_light_continue_hover.png"
                    selected_hover "images/gui/btn_light_continue_hover.png"
                    action Preference("auto-forward", "toggle")

                imagebutton:
                    idle "images/gui/btn_light_load_idle.png"
                    hover "images/gui/btn_light_load_hover.png"
                    action ShowMenu("load")


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")



##BACKGROUNDS
image bg office = Transform("images/backgrounds/small_office.png", blur=5)
image bg car = "images/backgrounds/car_resized.png"
image bg city hall = "images/backgrounds/city_hall_resized.png"
image bg library = "images/backgrounds/library_resized.png"


##ITEMS
image newspaper = "images/bad_ending_newspaper.png"
    