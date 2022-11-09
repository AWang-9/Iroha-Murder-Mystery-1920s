screen talkIrohaUI:
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
                textbutton _("You are Iroha?"):
                    action [Hide("talkIrohaUI"), Jump("hub" + currDay + "Iroha")]
            textbutton _("How old are you?"):
                action [Hide("talkIrohaUI"), Jump("hubday_1IrohaGuessedAge")]
            textbutton _("Back"):
                action [SetVariable("hubSelectedChar", ""),
                Hide("talkIrohaUI"), Jump("hub")]
    # image goes on the right side
    add "[hubSelectedChar.img]":
        xalign 0.75

screen guessAgeUI:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            text "Guess his age":
                color "#ffffff"
            input default "":
                value VariableInputValue("guessedAge")
            textbutton "OK":
                action Jump("hubday_1IrohaFinishedGuessedAge")
                keysym('K_KP_ENTER', 'K_RETURN')

label talkIroha:
    show screen talkIrohaUI
    "What should I do now?"
    jump talkIroha

#####################
### All day 1 dialogue
#####################

label hubday_1Iroha:
    show iroha neutral at Position(xalign=0.75)
    pF "You are Iroha?"
    i "Yes."
    hide iroha
    jump talkIroha

label hubday_1IrohaGuessedAge:
    show iroha neutral at Position(xalign=0.75)
    pF "How old are you?"
    i "Guess."
    show screen guessAgeUI
    $ _preferences.afm_enable = False
    $ renpy.pause(hard=True)

label hubday_1IrohaFinishedGuessedAge:
    hide screen guessAgeUI
    pF "[guessedAge]."
    if guessedAge == "37":
        i "Ha. Cheater."
    else:
        i "Nice guess."
    $ guessedAge = ""
    hide iroha
    jump talkIroha
