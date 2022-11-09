###########################
### Flags for the office
default lookedOffice = False
default showedLetter = False
############################


label day_4:
    $ currDay = "day_4"
    $ nextDay = "day_5"

    # fade into Balan's room
    scene test_bg with fade
    "Thursday morning, 7AM."

    "Taking advantage of Yuzuki’s kind offer, you sleep in and wake up an hour later than usual."
    "You still have some time before you have to go in for work so you take a walk."

    # fade to street
    scene test_bg with fade
    # put in scenery description
    # put in sus alleyway description
    "88888888888-SCENERY DESCRIPTION GOES HERE"
    "888888888-You see something sus in an alleyway and step closer to look."
    "As you get closer, you realize it’s a person--no, a preteen."
    "<<<There’s a white powder on her face.>>>"
    "They're not moving."
    "Nor breathing."
    "They're dead."

    pF "!!!"

    "You immediately back out of there and call the authorities."
    "They arrive promptly and close off the scene."
    "They interview you, but you don't have much information to give."
    "Ultimately, there’s not much you can do but watch them take the body away."
    "Shaken, you start to head to work again when you hear a crunch from under your shoe."
    "You look down."
    "There’s a piece of paper stuck to the bottom of your shoe--when did that happen?"

    # image of paper goes here
    "8888888888888-Show image of paper here"
    "It's a letter, in Xue Sahui's handwriting."
    "...Even if you wanted to give it to the police, they're long gone."
    "Best keep it for now."


label restaraunt_start_day_4:
    # should be restaraunt interior
    scene test_bg with fade

    "Yuzuki greets you as you enter the restaurant."

    show yuzuki neutral at center with dissolve

    y "You’re coming with me today."
    y worried "...But why do you look so pale? Did you meet a ghost or something on your way here?"
    pF "Actually..."

    "You describe what you saw this morning and show Yuzuki the letter."

    y "Huh. This is Satsuki’s handwriting. Why would a dead girl have it?"
    y neutral "Don’t worry too much about this, though--it doesn’t concern you."
    y happy "What does concern you is this sale!"
    pF "In broad daylight?"
    y "Yup!"

    scene black
    "You go with Yuzuki to seal another drug deal."

    # should be restaraunt interior
    scene test_bg with fade
    "When you get back, Yuzuki hands you a small notebook and asks you to deliver it up to Satsuki’s office."
    "You don’t really have a choice, so you do so."

    # should be Satsuki's office
    scene test_bg
    show satsuki neutral at center with fade
    "You knock on the door, Satsuki lets you in."
    "You hand him the notebook, and he thanks you politely."

    sa "Give me a moment, I’ll record this and then you can hand it back to Yuzuki."
    sa sadistic "Feel free to look around, if you want."
    show satsuki neutral

    "You look around his office in the meantime."
    "You also have that letter in his handwriting."

label look_Satsuki_office:
    menu satsuki_office_day_4:
        "Look around the office.":
            # describe the office
            "There's books with people's pictures and notes."
            "The dead girl you saw this morning...she's in one of these books."
            "There's a number next ot her photo."
            "There's also a note between a stack of folders."
            "It's a shipment to a faraway location."
            "And the girl's number is here."
            $ lookedOffice = True

        "Show Satsuki the letter.":
            sa shocked "Where did you find this?"
            sa neutral "I wrote it a while ago and sent it off, but my recipient never got it."
            sa "So I wrote another one. It was irritating."
            $ showedLetter = True
        "Wait for Satsuki to finish.":
            if lookedOffice and showedLetter:
                jump leave_satsuki_office_day4
            else:
                pF "I could be doing something else while I wait..."
                jump look_Satsuki_office
    jump look_Satsuki_office


label leave_satsuki_office_day4:
    sa neutral "Thank you for waiting, I’ve finished."
    "Satsuki closes the ledger he had been scribbling in and hands you back the small notebook."
    "You carefully take it back and exit quietly."

    scene black
    "After delivering the notebook to Yuzuki, you spend the rest of your day uneventfully washing dishes."

label debug_hub_day_4:
    jump hub
