# The main script of the story. Will call on events from different files
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default;
    scene bg room

    # This shows a character sprite. A placeholder is used.
    show elowyn happy

    elowyn "Hello World!"

    # Chapters
    call start_chapter_1
    elowyn "Bye Chapter 1!"

    call start_chapter_2
    elowyn "Bye Chapter 2!"

    call start_chapter_3
    elowyn "Bye Chapter 3!"

    call start_chapter_4
    elowyn "Bye Chapter 4!"

    call start_chapter_5
    elowyn "Bye Chapter 5!"

    call start_chapter_6
    elowyn "Bye Chapter 6!"

    # This ends the game.
    return
