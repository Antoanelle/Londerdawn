# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jane", color="ff0000")
define m = Character("Me", color="00ff00")
define t = Character("Test", color="0000ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Jane happy

    # These display lines of dialogue.

    m "Hello World!"
    e "Hello World!"
    t "Hello World!"

    # This ends the game.

    return
