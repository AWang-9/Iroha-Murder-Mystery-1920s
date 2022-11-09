                    # imagebutton:
                    #     idle "button2"
                    #     action [SetVariable("selectedItem", bread),
                    #         Hide("evidenceTOC"),
                    #         Show("ePageDetails")]
                    # imagebutton:
                    #     idle "button2"
                    #     action [SetVariable("selectedItem", egg),
                    #         Hide("evidenceTOC"),
                    #         Show("ePageDetails")]

screen talkCharaUI:
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
            textbutton _("How are you?"):
                action [Hide("talkCharaUI"), Jump("hub" + currDay + hubSelectedChar.name)]
            if hubSelectedChar.name == "Iroha" and currDay == "day_1":
                textbutton _("How old are you?"):
                    action [Hide("talkCharaUI"), Jump("hubday_1IrohaGuessedAge")]
            textbutton _("Back"):
                action [SetVariable("hubSelectedChar", ""),
                Hide("talkCharaUI"), Jump("hub")]
                # Hide("ePageTest"),
                # Show("eTOC")]
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
            text "Guess his age"
            input default "":
                value VariableInputValue("guessedAge")
            textbutton "OK":
                action Jump("hubday_1IrohaFinishedGuessedAge")
                keysym('K_KP_ENTER', 'K_RETURN')

screen charPage():
    tag charPage
    add "UI/bg peach.png"
    hbox:
        ## left frame
        frame:
            background "gui/Notebook_1L.png"
            ysize 950
            xsize 910
            ## left arrow
            if selectedChar.index != 0:
                imagebutton:
                    ypos 0.9
                    idle "leftArrowIdle"
                    hover "leftArrowHover"
                    action [SetVariable("selectedChar", allChars[selectedChar.index - 1]),
                        Show("charPage")]

            vbox:
                xsize 775
                xoffset 150
                yoffset 75
                spacing 50
                text "[selectedChar.name]":
                    text_align 0.5
                    size 120
                add "gui/label_1_2.png"
                text "Age":
                    xpos 20
                    ypos -100
                    color "#ffffff"
                text "[selectedChar.age]":
                    xpos 150
                    ypos -188
                    color "#ffffff"
                add "gui/label_1_2.png"
                text "Height [selectedChar.height]":
                    xpos 20
                    ypos -100
                    color "#ffffff"
                text "Weight [selectedChar.weight]"
                textbutton _("Back"):
                    ## ==================================
                    # DUMMY VALUES TO HAVE VISIBLE BACK BUTTON
                    # yoffset 90
                    # xoffset 20
                    # ypos 450
                    ## =============================
                    action [SetVariable("selectedChar", ""),
                        Hide("charPage"),
                        Show("charTOC")]

                ## Description viewport
                ## must be scrollable
                frame:
                    xsize 600
                    viewport id "vp":
                        draggable True
                        mousewheel True
                        vbox:
                            text "[selectedChar.desc]\n[selectedChar.notes]"
                            text "aaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\n"
                    vbar value YScrollValue("vp")


        ## Right frame
        ## Notice that we're using selectedCharacter to show the variables here.
        frame:
            background "gui/Notebook_1R.png"
            ysize 950
            xsize 910
            xpos 50
            vbox:
                xalign 0.5
                yalign 0.6
                add "[selectedChar.img]":
                    xalign 0.5
            vbox:
                xpos 356
                ypos 299
                imagebutton:
                    xpos 511
                    ypos -225
                    idle "gui/button/CharaButton_1.png"
                    hover"gui/button/CharaButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("charPage"),
                        Show("charTOC")]
                imagebutton:
                    xpos 511
                    ypos -178
                    idle "gui/button/EvidButton_1.png"
                    hover"gui/button/EvidButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("charPage"),
                        Show("eTOC")]
            # Right arrow
            if selectedChar.index != lastCharIndex:
                imagebutton:
                    ypos 0.9
                    xpos 800
                    idle "rightArrowIdle"
                    hover "rightArrowHover"
                    action [SetVariable("selectedChar", allChars[selectedChar.index + 1]),
                        Show("charPage")]


# frame:
#     if selectedChar.index == 0:
#         imagebutton:
#             ypos 0.4
#             idle "gui/button/Arrow_L_Disable.png"
#             action NullAction()
#     else:
#         imagebutton:
#             ypos 0.4
#             idle "gui/button/Arrow_L.png"
#             hover "gui/button/Arrow_L_Select.png"
#             action [SetVariable("selectedChar", allChars[selectedChar.index - 1]),
#                 Show("charPage")]



screen eTOC():
    tag eTOC
    add "UI/bg peach.png"
    hbox:
        ## left frame
        frame:
            style_prefix "stats"
            ysize 950
            xsize 910
            xpos 150
            ypos 50
            text "Evidence":
                text_align 0.5
                size 95

            textbutton _("Return"):
                yoffset 90
                xoffset 20
                action Return()


        ## Right frame
        ## Notice that we're using selectedCharacter to show the variables here.
        frame:
            ysize 950
            xsize 910
            ypos 50
            vbox:
                xalign 0.5
                yalign 0.5
                grid 4 4:
                    spacing 70
                    imagebutton:
                        idle "button2"
                        action [SetVariable("selectedItem", hairpin),
                            Hide("eTOC"),
                            Show("ePageDetails")]
                    imagebutton:
                        idle "button2"
                        action [SetVariable("selectedItem", bread),
                            Hide("eTOC"),
                            Show("ePageDetails")]
                    imagebutton:
                        idle "button2"
                        action [SetVariable("selectedItem", egg),
                            Hide("eTOC"),
                            Show("ePageDetails")]
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"
                    imagebutton:
                        idle "button"


screen StatsUI():
    tag statsUI
    add "UI/bg peach.png"
    hbox:
        ## left frame
        frame:
            style_prefix "stats"
            ysize 950
            xsize 910
            xpos 150
            ypos 50
            vbox:
                xsize 910
                ysize 950
                text "Yuzuki":
                    xalign 0.5
                text "Name: N/A"
                text "Blood Type: N/A"
                text "Major: N/A"


                text "Affection"
                ## We're creating a bar with the max affection of 10
                ## You can change the max affection to 100 or whatever value you want.
                bar value 10 xsize 300 xoffset 80
            add "images/Yuzuki/Happy_SketchY.PNG" xalign 0.5 yalign 0.5


        ## Right frame
        ## Notice that we're using selectedCharacter to show the variables here.
        frame:
            ysize 950
            xsize 910
            ypos 50
            vbox:
                xalign 0.5
                yalign 0.5
                grid 3 3:
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"
                    imagebutton:
                        idle "idleSprite"

                textbutton _("Return"):
                    yalign 0.5
                    yoffset 90
                    xoffset 20
                    action Return()
