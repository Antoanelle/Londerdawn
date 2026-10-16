## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    use game_menu(_("About"), scroll="viewport", title_image="images/screen_titles/about_title.png"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text:
    color gui.about_text_color

style about_label_text:
    size gui.label_text_size

