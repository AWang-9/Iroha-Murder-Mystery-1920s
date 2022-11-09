#####################
# flag for Tomoe things
default knowTomoeName = False
default readEverything = 0
default body = False
default desk = False
default floor = False
default tName = False
default kidnap = False
default reporter = False
default gather = False
#####################

transform focus:
    easein 0.3 zoom 1.03
transform unfocus:
    easeout 0.3 zoom 1.0

label day_2:
    $ currDay = "day_2"
    $ nextDay = "day_3"
    scene test_bg with fade
    "Tuesday morning, 6AM."

    pF "Ugh.."
    pF "I'm so tired."

    "As you prepare for the day, a knocking at your doorstep indicates that the paper boy is here. You smile."
    "You and Chang Shaoqing have been good friends for a while. Whenever he comes around, the two of you chat a bit and you give him his usual helping of bread."
    "You answer the door."

    pB "Good morning!"
    pF "Morning."

    "Chang Shaoqing promptly reaches into his basket and whips out the day’s newspaper."

    pB "You gotta see this one."
    pF "You say that about every one."
    pB "It's my job. Anyway! Have you heard what happened?"
    pF "You're the one who delivers the news."
    pB "And so I am! Cheng Zhengzhong died last night--you know, that really famous politician?"
    pB "And no one knows what’s going on."
    pB "There’s so little information it didn’t even make it into today’s paper."
    pF "So...The thing I had to see wasn't even in the paper?"
    pB "I'm supposed to say that, so."
    pF "...In any case."
    pF "Your bread for the day."

    "Chang Shaoqing beams as he accepts the bread roll, immediately taking a bite."

    pB "Thanks, [pFirst]! See you tomorrow!"

    "You watch as Chang Shaoqing bikes down the street, before glancing down at your watch."
    "It’s time to go to work already..."

label day_2_restauraunt_start:
    scene test_bg with fade
    "You arrive in the kitchens and you’re about to start washing some dishes, when you feel two hands grab you by the shoulders and forcibly turn you around."

    show yuzuki neutral with dissolve
    y "Did you hear? About the murder? You know, the politician?"
    pF "Yes, Chang Shaoqing told me this morning."
    y happy "Oh, Chang Shaoqing! How is he?"
    pF "He's doing well--growing up fast. But anyway, about the murder?"
    y neutral "Ah, right. Come with me!"

    hide yuzuki with dissolve

    "Yuzuki promptly grabs your wrist and drags you out of the kitchen and up to the second floor."
    "He drags you into the office you saw Satsuki leave from yesterday, and you find both Shio and Satsuki in there."

    show yuzuki neutral at left
    show satsuki upset at center
    show shio neutral at right
    with dissolve

    sh "Fuck. I’m going to find whoever did it and show them how it’s really done!"

    "Satsuki had appeared to be deep in thought, but plastered a customer service-y smile on his face upon seeing you."

    sa neutral "So this is what you meant when you said you had to go get something."

    if gender == "he":
        y "Yeah. Don't you see? He's a nobody!"
    elif gender == "she":
        y "Yeah. Don't you see? She's a nobody!"
    else:
        y "Yeah. Don't you see? They're a nobody!"

    pF "(wow, thanks)."
    y "So he’s perfect for further investigation."

    "You feel the other two stare at you intensely."

    y "I mean, you definitely can’t go, Shio. The way Cheng Zhengzhong was killed was unusually similar to how you kill--unless you actually did it?"
    sh angry "Of course I didn’t do it. You think I have that time?"
    show shio neutral
    y happy "Exactly~"
    y neutral "And you, Satsuki? People take one look at you and will think you’re the murderer."
    sa sadistic "Hm."
    show satsuki neutral
    y "So, it falls to me and my new friend, [pFirst] the reporter."
    pF "Reporter?"

    "A camera is abruptly shoved into your hands, and Yuzuki grins at you."
    y happy "That’s right, you’re a reporter now. Let’s go!"


label day_2_outside_politician_house:
    scene test_bg with fade
    show yuzuki neutral at center with dissolve
    "The two of you walk until you reach the politician’s house. The place is swarming with reporters and the police."

    pF "So what exactly are we doing here?"
    y "Truthfully, this morning, we received some inside information about the murder."
    y "As I said before, the method of killing is <<<eerily reminiscent of how Shio makes his kills.>>>"
    y "But…Shio didn’t do this one. We know this for sure."
    y "So, we have to investigate. Someone’s going around and framing us."
    y "And local death is bad for business, you know?"
    y happy "Now get in there!"

    hide yuzuki with dissolve

    "Yuzuki shoves you into the crowd of people, and you try your hardest to push your way to the front."
    "But despite your best efforts, you keep getting buffeted back."
    "A hand suddenly grips the back of your shirt and you get dragged to the side and out of the crowd."

    pF "Excuse me–"
    npc "This way."

    "You try to resist, but this man holding your collar is a lot taller and a lot stronger than you are."
    "You helplessly look around for Yuzuki, but he’s nowhere in sight."

    pF "(Am I really getting kidnapped on my second day of work?)"

    "The man drags you around to the back of the house, where there’s only a few officers stationed."
    "He makes an abrupt stop and ducks into the bushes, pulling you down with him."

    pF "Rude."
    show tomoe neutral at center with dissolve
    npc "Look."

    "The man points at a window in the house. It looks to be slightly warped, or something--it looks to be marginally open."

    npc "The lock is broken on that one."
    pF "So why'd you drag me here?"
    npc "Aren't you a reporter?"
    pF "Yes...?"
    npc "You can get inside."

    "Before you can ask any more questions, the man starts to move, creeping out of the bush."
    "He hops the fence without a moment of hesitation, and watches you expectantly."
    "Left with no other choice, you do your best to keep up with him as he sneaks through the broken window."
    "You end up in the living room of the house. There’s no one else inside--presumably, all the authorities are dealing with the crowds outside."
    "It looks like something...THAT WE HAVEN'T WRITTEN YET."
    "Now's as good of a time as any to gather evidence."
    "And also as good of a time as any to talk to your mysterious kidnapper."

label within_politician_room:
    menu check_room_or_talk_Tomoe:
        "Investigate the room.":
            jump investigate_room
        "Talk to the mysterious man.":
            jump talk_to_Tomoe
        "Finish investigation.":
            if body and desk and floor and knowTomoeName and kidnap and reporter and gather:
                jump after_politician_investigation_with_Tomoe
            else:
                pF "Wait, I think there's still more."
                jump within_politician_room



label investigate_room:
    menu look_around_room:
        "Look at the body.":
            "The policitian died to a needle stab in the neck."
            $ body = True
        "Look at the desk.":
            "There's some of the drug there."
            $ desk = True
        "Look at the floor.":
            "There's a strand of white hair there."
            "There's also some dried blood."
            $ floor = True
        "Finish":
            jump within_politician_room

    jump look_around_room

label talk_to_Tomoe:
    hide tomoe with dissolve
    menu Tomoe_questions:
        "What's your name?":
            show tomoe neutral at center with dissolve
            t "Tomoe."
            $ knowTomoeName = True
        "Why did you kidnap me?":
            show tomoe neutral at center with dissolve
            if knowTomoeName == True:
                t "I didn't kidnap you."
                t "I helped you out."
            else:
                npc "I didn't kidnap you."
                npc "I helped you out."
            $ kidnap = True
        "You're a reporter?":
            show tomoe neutral at center with dissolve
            if knowTomoeName == True:
                t "Yes."
            else:
                npc "Yes."
            pF "(...Helpful.)"
            $ reporter = True
        "What did you gather?":
            show tomoe neutral at center with dissolve
            if knowTomoeName == True:
                t "I'll show you once you're finished."
            else:
                npc "I'll show you once you're finished."
            $ gather = True
        "End conversation.":
            jump within_politician_room
    jump talk_to_Tomoe

label after_politician_investigation_with_Tomoe:
    show tomoe neutral at center with dissolve
    t "Something else I found."

    "<<<He shows you a beautiful hairpin, with a deadly point on the end.>>>"

    t "I found this under a nearby bush, in the garden. I tried to show it to the police..."
    t "but no one thought any of it."
    pF "Why were you nearby, anyway?"
    t "I live in the area. Now let’s go before we get caught."

    "You hastily leave the crime scene with the man."
    "You manage to slip outside undetected, much to your relief."

    y "[pFirst]!"

    hide tomoe with moveoutright

    pF "Tomoe?"

    "Yuzuki catches up to you and pulls you back to the crowd of reporters."

    show yuzuki worried at center with dissolve

    y "Who was that?"
    pF "Not sure."
    y "Didn’t your parents tell you not to go off with strangers?"
    y happy "But they also probably told you not to be friends with criminals, and here you are~"
    y neutral "But anyway. Did you get something?"
    pF "Yeah, I got--"
    y "Save it for when we're away from prying ears, hm? Let's head back to the restaraunt for now."

label debug_hub_day2:
    jump hub
