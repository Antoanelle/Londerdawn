## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    add "main_menu_title_animated":
        xalign 0.0
        zoom 1.5
        
    
    ## The use statement includes another screen inside this one.
    use start_button
    use quit_button
    use about_button
    use setting_button


#Main Screen Buttons
screen start_button():
    imagebutton:
        focus_mask True
        xalign 0.0
        ypos 450
        xoffset 200
        idle im.Scale("images/start_screen/start_idle.png", 500, 350)
        hover im.Scale("images/start_screen/start_hover.png", 500, 350)
        action Start()

screen quit_button():
    imagebutton:
        focus_mask True
        xalign 0.0
        ypos 550
        xoffset 120
        idle im.Scale("images/start_screen/quit_idle.png", 500, 350)
        hover im.Scale("images/start_screen/quit_hover.png", 500, 350)
        action Quit(confirm=not main_menu)


screen about_button():
    imagebutton:
        xalign 0.0 
        ypos 950
        xoffset -20 
        idle im.Scale("images/start_screen/about_idle.png", 180, 120)
        hover im.Scale("images/start_screen/about_hover.png", 180, 120)
        action ShowMenu("about")

screen setting_button():
    imagebutton:
        yalign 1.0 
        xpos 50
        xoffset 40 
        yoffset -10 
        idle im.Scale("images/start_screen/setting_idle.png", 180, 120)
        hover im.Scale("images/start_screen/setting_hover.png", 180, 120)
        action ShowMenu("settings")

image main_menu_title_animated:
    "images/start_screen/game_title.png"
    ypos 200
    ease 0.8 ypos 175
    ease 0.8 ypos 150
    "images/start_screen/game_title_unscrambled.png"
    pause 0.2
    "images/start_screen/game_title.png"
    ease 0.8 ypos 175
    ease 0.8 ypos 200
    repeat