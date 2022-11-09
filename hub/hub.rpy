# image spriteButton = im.Scale("TEST_CharaSprite.png", 200, 200)
# we know what day it is, can go accordingly

screen hubUI:
    # add test_bg
    add "images/TEST_BG.PNG"
    # add "UI/bg peach.png"
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 80
        hbox:
            yalign 0.3
            xalign 0.5
            grid 5 1:
                spacing 80
                xspacing 150
                imagebutton:
                    idle "yuzukiFaceSprite"
                    action [SetVariable("hubSelectedChar", yuzuki),
                    Hide("hubUI"), Jump("talkYuzuki")]
                imagebutton:
                    idle "shioFaceSprite"
                    action [SetVariable("hubSelectedChar", shio),
                    Hide("hubUI"), Jump("talkShio")]
                imagebutton:
                    idle "satsukiFaceSprite"
                    action [SetVariable("hubSelectedChar", satsuki),
                    Hide("hubUI"), Jump("talkSatsuki")]
                imagebutton:
                    idle "irohaFaceSprite"
                    action [SetVariable("hubSelectedChar", iroha),
                    Hide("hubUI"), Jump("talkIroha")]
                imagebutton:
                    idle "tomoeFaceSprite"
                    action [SetVariable("hubSelectedChar", tomoe),
                    Hide("hubUI"), Jump("talkTomoe")]
        imagebutton:
            idle "button2"
            action [SetVariable("hubSelectedChar", ""),
            Hide("hubUI"), Jump("continueToNext")]


label hub:
    show screen hubUI
    "What should I do now?"
    jump hub


label continueToNext:
    if currDay == "day_3":
        show yuzuki neutral at center with dissolve
        y happy "Oh, by the way!"
        y neutral "You can come in late tomorrow."
        y happy "Must've been hectic, being both a reporter and a woman!"
    scene black
    "And thus, the hub comes to a close."
    $ renpy.jump(nextDay)
