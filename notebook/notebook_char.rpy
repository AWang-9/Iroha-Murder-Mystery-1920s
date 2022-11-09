# # screen gameUI:
# #     imagebutton:
# #         xalign 1.0
# #         yalign 0.0
# #         # the notebook button itself
# #         # auto "UI/stats_%s.png"
# #         idle "Test_ButtonRect.png"
# #         action ShowMenu("charTOC")
# #     imagebutton:
# #         auto "UI/stats_%s.png"
# #         action ShowMenu("eTOC")
# #
# #
# # label testNotebook:
# #     show screen gameUI
# #     "Within testNotebook"
# #     "Now I'm here again"
# #     "and again..."
#
#
image idleSprite = im.Scale("TEST_CharaSprite.png", 200, 200)

screen charTOC():
    tag charTOC
    add "UI/bg peach.png"
    hbox:
        ## left frame
        frame:
            background "gui/Notebook_1L.png"
            ysize 950
            xsize 910
            # xpos 150
            # ypos 50

            vbox:
                xoffset 120
                yoffset 75
                text "Characters":
                    text_align 0.5
                    size 95

                textbutton _("Return"):
                    yoffset 90
                    xoffset 20
                    action Return()

        ## Right frame
        frame:
            background "gui/Notebook_1R.png"
            ysize 950
            xsize 910
            xpos 50

            vbox:
                yoffset 120
                xalign 0.5
                text "Characters":
                    text_align 0.5
                textbutton _("Yuzuki"):
                    text_align 0.5
                    action [SetVariable("selectedChar", yuzuki),
                        Hide("charTOC"),
                        Show("charPageSingle")]
                textbutton _("Shio"):
                    text_align 0.5
                    action [SetVariable("selectedChar", shio),
                        Hide("charTOC"),
                        Show("charPageSingle")]
                textbutton _("Satsuki"):
                    text_align 0.5
                    action [SetVariable("selectedChar", satsuki),
                        Hide("charTOC"),
                        Show("charPageSingle")]
                textbutton _("Iroha"):
                    text_align 0.5
                    action [SetVariable("selectedChar", iroha),
                        Hide("charTOC"),
                        Show("charPageSingle")]
                textbutton _("Tomoe"):
                    text_align 0.5
                    action [SetVariable("selectedChar", tomoe),
                        Hide("charTOC"),
                        Show("charPageSingle")]

            vbox:
                xpos 356
                ypos 299
                imagebutton:
                    xpos 511
                    ypos -225
                    idle "gui/button/CharaButton_1.png"
                    hover"gui/button/CharaButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("evidenceTOC"),
                        Show("charTOC")]
                imagebutton:
                    xpos 511
                    ypos -178
                    idle "gui/button/EvidButton_1.png"
                    hover"gui/button/EvidButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("evidenceTOC"),
                        Show("evidenceTOC")]


screen charPageSingle():
    tag charPageSingle
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
                        Show("charPageSingle")]

            vbox:
                xsize 775
                xoffset 150
                yoffset 75
                spacing 50
                text "[selectedChar.name]":
                    text_align 0.5
                    size 120
                add "gui/label_1_2.png"
                add "gui/label_1_2.png"
                add "gui/label_1_2.png"
                ## Description viewport
                ## must be scrollable
                textbutton _("Back"):
                    ## ==================================
                    # DUMMY VALUES TO HAVE VISIBLE BACK BUTTON
                    # yoffset 90
                    # xoffset 20
                    # ypos 450
                    ## =============================
                    action [SetVariable("selectedChar", ""),
                        Hide("charPageSingle"),
                        Show("charTOC")]
                frame:
                    xsize 600
                    viewport id "vp":
                        draggable True
                        mousewheel True
                        vbox:
                            text "[selectedChar.desc]\n[selectedChar.notes]":
                                color "#ffffff"
                            text "aaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\naaa\n":
                                color "#ffffff"
                    vbar value YScrollValue("vp")

            vbox:
                xsize 775
                xoffset 175
                yoffset 275
                spacing 72
                text "Age":
                    color "#ffffff"
                text "Height":
                    color "#ffffff"
                text "Weight":
                    color "#ffffff"
            vbox:
                xsize 775
                xoffset 175
                yoffset 275
                xpos 180
                spacing 72
                text "[selectedChar.age]":
                    color "#ffffff"
                text "[selectedChar.height]":
                    color "#ffffff"
                text "[selectedChar.weight]":
                    color "#ffffff"


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
                        Hide("charPageSingle"),
                        Show("charTOC")]
                imagebutton:
                    xpos 511
                    ypos -178
                    idle "gui/button/EvidButton_1.png"
                    hover"gui/button/EvidButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("charPageSingle"),
                        Show("evidenceTOC")]
            # Right arrow
            if selectedChar.index != lastCharIndex:
                imagebutton:
                    ypos 0.9
                    xpos 800
                    idle "rightArrowIdle"
                    hover "rightArrowHover"
                    action [SetVariable("selectedChar", allChars[selectedChar.index + 1]),
                        Show("charPageSingle")]
