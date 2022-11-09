screen talkSatsukiUI:
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
            if currDay == "day_1":
                textbutton _("You are Satsuki?"):
                    action [Hide("talkSatsukiUI"), Jump("hub" + currDay + "Satsuki")]
            textbutton _("Back"):
                action [SetVariable("hubSelectedChar", ""),
                Hide("talkSatsukiUI"), Jump("hub")]
    # image goes on the right side
    add "[hubSelectedChar.img]":
        xalign 0.75

label talkSatsuki:
    show screen talkSatsukiUI
    "What should I do now?"
    jump talkSatsuki

#####################
### All day 1 dialogue
#####################

label hubday_1Satsuki:
    show satsuki neutral at Position(xalign=0.75)
    pF "You are Satsuki?"
    sa sadistic "Mhm."
    hide satsuki
    jump talkSatsuki
