# The script of the game goes in this file.

transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    linear 2.0 xalign -1.0
    repeat

label show_everyone:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene test_bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show stick happy at center with blinds
    show yuzuki happy:
        xpos 0

    show tomoe neutral:
        xpos 0.2
    show shio angry at center
    show satsuki neutral:
        xpos 0.53

    show iroha neutral:
            xpos 0.7



    # These display lines of dialogue.

    y "I am Yuzuki."

    sh "I am Shio."

    i "I am iroha."


    # This ends the game.

    return
