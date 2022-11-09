###########
### Defined characters
define y = Character("Qiu Rangxi", image="yuzuki")
define sh = Character("Shen Zhiying", image="shio")
define i = Character("Xia Caiye", image="iroha")
define t = Character("Feng YouHui", image="tomoe")
define sa = Character("Xue Sahui", image="satsuki")

define npc = Character("???")
define watchMan = Character("Man with Watch")
define pB = Character("Chang Shaoqing")
define pol = Character("Police")

$ scale = 200

###########


######################################
### Images for all characters
image test_bg = "TEST_BG.PNG"

image yuzuki angry = "Yuzuki/Angry_LineY.PNG"
image yuzuki blush = "Yuzuki/Blush_LineY.PNG"
image yuzuki happy = "Yuzuki/Happy_LineY.PNG"
image yuzuki neutral = "Yuzuki/Neutral_LineY.PNG"
image yuzuki shocked = "Yuzuki/Shock_LineY.PNG"
image yuzuki thinking = "Yuzuki/Thinking_SketchY.PNG"
image yuzuki upset = "Yuzuki/Upset_LineY.PNG"
image yuzuki worried = "Yuzuki/Worried_LineY.PNG"
image yuzukiFaceSprite = im.Scale("Yuzuki/Yuzuki_FaceS.png", 200, 200)

image shio angry = "Shio/Angry_SketchSh.PNG"
image shio blush = "Shio/Blush_SketchSh.PNG"
image shio happy = "Shio/Happy_SketchSh.PNG"
image shio neutral = "Shio/Neutral_SketchSh.PNG"
image shio sad = "Shio/Sad_SketchSh.PNG"
image shio shocked = "Shio/Shocked_SketchSh.PNG"
image shio thinking = "Shio/Thinking_SketchSh.PNG"
image shioFaceSprite = im.Scale("Shio/Shio_FaceS.png", 200, 200)

image iroha angry = "Iroha/Angry_SketchI.PNG"
image iroha blush = "Iroha/Blush_SketchI.PNG"
image iroha neutral = "Iroha/Neutral_SketchI.PNG"
image iroha sad = "Iroha/Sad_SketchI.PNG"
image iroha shocked = "Iroha/Shocked_SketchI.PNG"
image iroha thinking = "Iroha/Thinking_SketchI.PNG"
image irohaFaceSprite = im.Scale("Iroha/Iroha_FaceS.png", 200, 200)

image tomoe angry = "Tomoe/Angry_SketchT.PNG"
image tomoe blush = "Tomoe/Blush_SketchT.PNG"
image tomoe happy = "Tomoe/Happy_SketchT.PNG"
image tomoe neutral = "Tomoe/Neutral_SketchT.PNG"
image tomoe shocked = "Tomoe/Shocked_SketchT.PNG"
image tomoe thinking = "Tomoe/Thinking_SketchT.PNG"
image tomoeFaceSprite = im.Scale("Tomoe/Tomoe_FaceS.png", 200, 200)


image satsuki angry = "Satsuki/Angry_SketchSa.PNG"
image satsuki neutral = "Satsuki/Neutral_SketchSa.PNG"
image satsuki sadistic = "Satsuki/Sadistic_SketchSa.PNG"
image satsuki shocked = "Satsuki/Shocked_SketchSa.PNG"
image satsuki thinking = "Satsuki/Thinking_SketchSa.PNG"
image satsuki upset = "Satsuki/Upset_SketchSa.PNG"
image satsuki worried = "Satsuki/Worried_SketchSa.PNG"
image satsukiFaceSprite = im.Scale("Satsuki/Satsuki_FaceS.png", 200, 200)

######################################


########################################
## Information about the player
define pF = Character("[pFirst]")
define pL = Character("[pLast]")
define pG = Character("[gender]")
########################################

########################################
##### default variables and values
##########
# player info
default pFirst = "Balan"
default pLast = "Knight"
default gender = ""
##########

#########
# hub info
default hubSelectedChar = ""
default guessedAge = ""
##########

######
# day info
default currDay = "day_1"
default nextDay = "day_2"
######


#########
# notebook info
image button = im.Scale("test_button.png", 100, 100)
image button2 = im.Scale("test_button2.png", 100, 100)
image rightArrowIdle = im.Scale("gui/button/Arrow_R.png", 110, 165)
image rightArrowHover = im.Scale("gui/button/ArrowHover_R.png", 110, 165)
image leftArrowIdle = im.Scale("gui/button/Arrow_L.png", 110, 165)
image leftArrowHover = im.Scale("gui/button/ArrowHover_L.png", 110, 165)
#########


#################
# Get gender frame

screen getGender:
    frame:
        xsize 600
        ysize 250
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.2
            text "What is your gender?":
                color "#ffffff"
            hbox:
                ypos 25
                xalign 0.5
                textbutton _("He"):
                    action[SetVariable("gender", "he"),
                    Hide("getGender"), Jump("day_1")]
                textbutton _("She"):
                    action[SetVariable("gender", "she"),
                    Hide("getGender"), Jump("day_1")]

                textbutton _("They"):
                    action[SetVariable("gender", "they"),
                    Hide("getGender"), Jump("day_1")]


###################

######################################
# GAME START
label start:
    # jump show_everyone
    # jump testNotebook
    # jump day_3
    python:
        pFirst = renpy.input("Enter your first name: ", length=32)
        pFirst = pFirst.strip()
        if not pFirst:
            pFirst = "Balan"

    jump getLast

label getLast:
    python:
        pLast = renpy.input("Enter your last name: ", length=32)
        pLast = pLast.strip()
        if not pLast:
            pLast = "Knight"

    jump getGender

label getGender:
    show screen getGender
    $ _preferences.afm_enable = False
    $ renpy.pause(hard=True)
    # python:
    #     valid = 0
    #     while valid == 0:
    #         gender = renpy.input("What is your gender? he/she/they, all lowercase", length=32)
    #         gender = gender.strip()
    #         if gender != "he" and gender != "she" and gender != "they":
    #             valid = 0
    #         else:
    #             valid = 1
