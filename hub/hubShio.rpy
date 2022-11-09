screen talkShioUI:
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
                textbutton _("You are Shio?"):
                    action [Hide("talkShioUI"), Jump("hub" + currDay + "Shio")]
            textbutton _("Back"):
                action [SetVariable("hubSelectedChar", ""),
                Hide("talkShioUI"), Jump("hub")]
    # image goes on the right side
    add "[hubSelectedChar.img]":
        xalign 0.75

label talkShio:
    show screen talkShioUI
    "What should I do now?"
    jump talkShio

#####################
### All day 1 dialogue
#####################

label hubday_1Shio:
    show shio neutral at Position(xalign=0.75)
    pF "You are Shio?"
    sh angry "Yeah. What of it?"
    hide shio
    jump talkShio
