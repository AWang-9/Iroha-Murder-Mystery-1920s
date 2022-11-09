screen talkTomoeUI:
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
                textbutton _("You are Tomoe?"):
                    action [Hide("talkTomoeUI"), Jump("hub" + currDay + "Tomoe")]
            textbutton _("Back"):
                action [SetVariable("hubSelectedChar", ""),
                Hide("talkTomoeUI"), Jump("hub")]
    # image goes on the right side
    add "[hubSelectedChar.img]":
        xalign 0.75

label talkTomoe:
    show screen talkTomoeUI
    "What should I do now?"
    jump talkTomoe

#####################
### All day 1 dialogue
#####################

label hubday_1Tomoe:
    show tomoe neutral at Position(xalign=0.75)
    pF "You are Tomoe?"
    t "Yes."
    hide tomoe
    jump talkTomoe
