screen talkYuzukiUI:
    add "images/TEST_BG.PNG"
    # left frame for talking
    frame:
        xalign 0.3
        yalign 0.5
        vbox:
            xsize 500
            ysize 500
            text "Talk":
                color "#ffffff"
            if currDay == "day_2":
                textbutton _("Day 2 dialogue!"):
                    action NullAction()
            if currDay == "day_1":
                textbutton _("You are Yuzuki?"):
                    action [Hide("talkYuzukiUI"), Jump("hub" + currDay + "Yuzuki")]
            textbutton _("Back"):
                action [SetVariable("hubSelectedChar", ""),
                Hide("talkYuzukiUI"), Jump("hub")]
    # image goes on the right side
    add "[hubSelectedChar.img]":
        xalign 0.75

label talkYuzuki:
    show screen talkYuzukiUI
    "What should I do now?"
    jump talkYuzuki

#####################
### All day 1 dialogue
#####################

label hubday_1Yuzuki:
    show yuzuki neutral at Position(xalign=0.75)
    pF "You are Yuzuki?"
    y happy "I am! Nice to meet you!"
    hide yuzuki
    jump talkYuzuki



##########################################
## All hub day 2 dialogue
##########################################
label hubday_2Yuzuki:
    show yuzuki neutral at Position(xalign=0.75)
    pF "How are you?"
    y happy "I'm doing fine!"
    hide yuzuki
    jump talkYuzuki
##########################################
