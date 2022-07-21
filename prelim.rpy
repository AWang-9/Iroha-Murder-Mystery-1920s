define pF = Character("[pFirst]")
define pL = Character("[pLast]")
define pG = Character("[gender]")

default pFirst = "Balan"
default pLast = "Knight"
default gender = "he"

label start:
    # jump show_everyone
    # jump testNotebook
    jump day1
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
    python:
        valid = 0
        while valid == 0:
            gender = renpy.input("What is your gender? he/she/they, all lowercase", length=32)
            gender = gender.strip()
            if gender != "he" and gender != "she" and gender != "they":
                valid = 0
            else:
                valid = 1

    jump day1
    # jump show_everyone
    # "wow you did it!"
    # "now save and quit and come back"
    #
    # "Here is your full name: [pFirst] [pLast]"
    # "you are a [gender]"
