# The script of the game goes in this file.


# should be a global init
init:
    $playerName = "Balan"

define s = Character("Stick", image="stick")
define y = Character("Yuzuki", image="yuz")
define sh = Character("Shio", image="shio")
define i = Character("Iroha", image="iroha")
define t = Character("Tomoe", image="tomoe")
define sa = Character("Satsuki", image="satsuki")

image test_bg = "TEST_BG.PNG"

image stick happy = "TEST_HappyChara.png"
image stick sad = "TEST_SadChara.png"
image stick angry = "TEST_AngryChara.png"

image yuz happy = "Yuzuki/Happy_SketchY.PNG"

image shio angry = "Shio/Angry_SketchSh.PNG"

image iroha neutral = "Iroha/Neutral_SketchI.PNG"

image tomoe neutral = "Tomoe/Neutral_SketchT.PNG"

image satsuki neutral = "Satsuki/Neutral_SketchSa.PNG"

image stick animated:
    "TEST_HappyChara.png"
    "TEST_SadChara.png"
    "TEST_AngryChara.png"
    repeat


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
    show yuz happy:
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

    # s sad "I am sad now."
    # s happy "I am happy now."
    # s angry "I am angry now."
    # s sad "I am sad again."

    s happy "player's name is [playerName]."

    jump start_day_1


    # This ends the game.

    return
