
# $ hairpin.next = bread
# $ bread.prev = hairpin

screen evidenceTOC():
    tag evidenceTOC
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
            background "gui/Notebook_1R.png"
            ysize 950
            xsize 910
            xpos 50
            vbox:
                xalign 0.5
                yalign 0.5
                grid 4 4:
                    spacing 70
                    imagebutton:
                        idle "button2"
                        action [SetVariable("selectedItem", hairpin),
                            Hide("evidenceTOC"),
                            Show("ePageDetails")]
                    imagebutton:
                        idle "button2"
                        action [SetVariable("selectedItem", hearsayEvid_ShioKillStyle),
                            Hide("evidenceTOC"),
                            Show("ePageDetails")]
                    imagebutton:
                        idle "button2"
                        action [SetVariable("selectedItem", bread),
                            Hide("evidenceTOC"),
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


screen ePageDetails():
    tag ePageDetails
    add "UI/bg peach.png"
    ## arrow before the frame
    # text "selected item info"
    # text "[all_items[0]]"
    hbox:
        ## left frame
        frame:
            background "gui/Notebook_1L.png"
            style_prefix "stats"
            ysize 950
            xsize 910
            ## useful for when there's no arrow on the screen
            # xpos 150

            if selectedItem.index != 0:
                imagebutton:
                    ypos 0.9
                    idle "leftArrowIdle"
                    hover "leftArrowHover"
                    action [SetVariable("selectedItem", all_items[selectedItem.index - 1]),
                        Show("ePageDetails")]
            vbox:
                xsize 775
                xoffset 120
                yoffset 75
                spacing 150
                text "[selectedItem.name]":
                    text_align 0.5
                    size 80

                text "[selectedItem.desc]":
                    size 35

            textbutton _("Back"):
                yoffset 750
                xoffset 120
                # action ShowMenu("charTOC")
                action [SetVariable("selectedItem", ""),
                    Hide("ePageDetails"),
                    Show("evidenceTOC")]

        ## Right frame
        frame:
            background "gui/Notebook_1R.png"
            ysize 950
            xsize 810
            xpos 50
            ## useful when there's no arrow on the screen
            # xpos 140
            vbox:
                xalign 0.5
                xoffset 75
                yoffset 100
                # yalign 0.99
                add "[selectedItem.img]":
                    xalign 0.5
                    zoom 0.75
            vbox:
                xpos 356
                ypos 299
                imagebutton:
                    xpos 511
                    ypos -225
                    idle "gui/button/CharaButton_1.png"
                    hover"gui/button/CharaButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("ePageDetails"),
                        Show("charTOC")]
                imagebutton:
                    xpos 511
                    ypos -178
                    idle "gui/button/EvidButton_1.png"
                    hover"gui/button/EvidButton_1H.png"
                    action [SetVariable("selectedChar", ""),
                        Hide("ePageDetails"),
                        Show("evidenceTOC")]
            ## Right arrow
            # xpos -50
            if selectedItem.index != lastItemIndex:
                imagebutton:
                    ypos 0.9
                    xpos 800
                    idle "rightArrowIdle"
                    hover "rightArrowHover"
                    action [SetVariable("selectedItem", all_items[selectedItem.index + 1]),
                        Show("ePageDetails")]
