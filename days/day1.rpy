label day_1:
    $ renpy.pause(hard=False)
    # fade into Balan's room
    # show screen gameUI
    scene test_bg with fade
    "Monday morning, 6AM."
    # jump testInterrogationMechanic
    # jump meetShio
    # jump show_everyone
    # jump meetSatsuki
    # jump testNotebook
    # jump test
    # jump hub
    # jump hub
    # jump within_politician_room
    # jump meetIroha
    pF "Ugh…"
    pF "First day of work today."
    pF "If it wasn’t for Qiu Rangxi I think I would be out on the street right now…."
    pF "I better go get ready, so I’m not late."
    pF "What should I wear?"

    "You get ready and put on your clothes relatively quickly.
    You had agreed to meet Qiu Rangxi at the food stand that both of you
    frequented when you were still students."

    scene test_bg
    show yuzuki neutral with fade

    pause 0.25
    y happy "Hey!"

    "He spots you from a couple feet away and raises his arm to wave at you."

    pF "Hey!"
    y neutral "Are you ready for your big day?"

    menu ready_day_1:
        "Yes!":
            y happy "That's great!"
        "No.":
            y "Ah, you'll be fine."


    y neutral "So, lemme give you a rundown of today."
    "He hands you a bun he bought from the stand as the two of you start to walk."
    y "It’s nothing too hard, anyone can do it."
    y happy "It's dishwashing!"
    y neutral "At least, that’s what you’ll be doing most of the time."
    y "For the other times? We can talk about that later."

    scene black

    "Other times…You had a general idea of what that meant…"
    "And that it wasn’t anything legal."
    "But a job was a job, and it beat living on the streets."

    scene test_bg with fade
    "You arrive outside a large restaurant on a bustling street.
    It was still early, with other shopkeepers and store owners opening up shop in the early morning sun."
    ###########################################
    ### TODO: Put in the rest of the scene here
    ###########################################

label meet_Shio:
    "YOu walk past several private booths, usually given to larger
    parties or reservations, when suddenly..."
    scene test_bg with hpunch
    pause 0.25

    pF "!!!"
    "A person falls out of one and onto the floor, right in front of you.
    Blood from the person’s head is rapidly pooling at your feet.
    Qiu Rangxi immediately pulls you a few steps back."

    show yuzuki worried with dissolve
    y "You okay?"

    menu you_okay:
        "I'm...okay.":
            y "As long as you say so."
            y "It’s okay if you’re not, it’s not everyday someone dies in front of you."

        "There's a dead person in front of me!":
            y "...Um."
            y happy "Great observation!"
            y worried "Don’t worry, in your work, you won’t be seeing a lot of this."

    show yuzuki worried at Position(xalign=0.25, yalign=1.0) with move

    show shio angry at Position(xalign=0.7, yalign=1.0) with moveinright
    "A man(?) walks out with blood splattered across his clothes."
    sh "Ugh."

    "He's scowling as he cleans a golden hairpin on a once-pristine white handkerchief, before sliding it back into his hair."
    "Qiu Rangxi doesn’t seem surprised at the sight at all."

    y angry "Who's gonna clean this up?"

    "The man shrugs."

    y "Shen Zhiying...Agh, whatever."
    y upset "[pFirst], this is Shen Zhiying, my youngest brother."
    y "Shen Zhiying, this is my newest employee."

    show shio neutral
    "You feel Shen Zhiying’s eyes scrutinizing you as he looks you up and down."
    sh "Tch. Did you pick him up off the street?"

    hide shio neutral with moveoutright

    "He leaves before Qiu Rangxi can respond."

    show yuzuki upset at Position(xalign=0.5) with move
    "Qiu Rangxi, albeit unsurprised, looks exasperated."
    y "You get used to his attitude. He’s all bark and…some bite."

label meet_Satsuki:
    scene test_bg
    show yuzuki neutral at Position(xalign=0.2, yalign=1.0) with fade
    "Qiu Rangxi leads you down the walkway. As you walk, a door ahead of you clicks open."
    """
    A man wearing a suit and carrying a tall stack of papers
     walks out. A very expensive watch glistens on his wrist.
    """
    "Someone else follows the man out."
    "You can faintly make out some of the words they’re saying."

    watchMan "Shipment…tomorrow…"
    npc "Damaged…Expenses…Uncooperative…"
    watchMan "How many people…?"

    y "Xue Sahui!"
    show satsuki neutral at Position(xalign=0.75, yalign=1.0) with moveinright
    sa "Hm?"

    "The man with the watch turns around. When he notices you, he waves away the other man."

    y "Let me help you carry that. By the way, this is [pFirst], who'll be working with me from now on."
    y "[pFirst], this is Xue Sahui, my younger brother."

    "Just like Shen Zhiying, Xue Sahui takes his time observing you, looking at you from head to toe."

    sa "Nice to meet you."

    menu nice_to_meet_you:
        "The pleasure is all mine.":
            sa "Hm."
        "Are you gonna kill me, too?":
            show satsuki sadistic
            sa "Haha!"
            sa "I hope you have a will written. It may come in handy soon."
            show satsuki neutral

    "Xue Sahui simply turns around and leads the way down the hall, you and Qiu Rangxi trailing behind him."

    y "Oh, right!"
    y "You might want to send someone downstairs to clean up. Customers are going to come in soon."

    sa sadistic "Why don’t you send your new employee to do so?"
    if gender == "he":
        sa "I think he'll do a great job."
    elif gender == "she":
        sa "I think she'll do a great job."
    else:
        sa "I think they'll do a great job."

    "Both of them turn to look at you. Xue Sahui’s gaze is expectant, while Qiu Rangxi’s is concerned."

    menu clean_up_body:
        "...":
            y happy "Haha."
            y upset "Nice try."
        "My job is to wash dishes. I don't clean up dead bodies.":
            sa neutral "Ah. You're the bold type."
            sa "I wonder how long you'll make it here."

label meet_Iroha:
    scene test_bg
    show yuzuki neutral at Position(xalign=0.1, yalign=1.0)
    show satsuki neutral at Position(xalign=0.9, yalign=1.0)
    show iroha neutral at Position(xalign=0.5, yalign=1.0)
    with fade
    """
    You arrive at a large office. It’s a spacious place, with ornate decorations placed tastefully throughout and expensive art pieces hanging off the walls.
    A haze of smoke perpetually rests over the entire office.
    At the back of the room is an intimidating man,
    lounging with his pipe.
    """

    "This must be Xia Caiye."

    y "Alright, we're here."
    sa "Father, here are your files."

    "Xue Sahui places them on a nearby table. The man barely looks up."

    i "Thank you. Dismissed."

    "Xue Sahui gives a quick bow, before walking out."
    hide satsuki neutral with moveoutright

    y "Father! I have someone for you to meet. This is [pFirst]-"
    i "Ah, the friend you always talk about."
    if gender == "he":
        y "He's going to be working for me now."
    elif gender == "she":
        y "She's going to be working for me now."
    else:
        y "They'll be working for me now."

    menu introduce_to_Iroha:
        "Make an impression.":
            "You walk around the table and into the man’s line of sight."
            "You bow."
            pF "My name is [pF], sir."
            pF "I will work hard, and do my best not to disappoint."
            i "I would hope so."
        "Stay where you are.":
            pF "I'm [pF]. Nice to meet you, sir."
            i "Hm."

    y happy "We’ll get back to work now."
    "After Xia Caiye gives a dismissive nod, Qiu Rangxi gestures for you to follow him out of the office."
    y neutral "Come on, the restaurant’s opening soon. I’ll show you to the kitchens."

    scene test_bg with fade

    """You practically spend the entire day standing by the sink and washing dishes.
     You’re not sure how much time has passed,
     but your feet are aching for a break."""

    show yuzuki neutral at Position(xalign=0.5) with hpunch
    y "Hey!"

    menu yuz_hey:
        "Oh...Hi.":
            y "You good? You look kind of out of it."
            pF "Just tired..."
            y "Ah. Well, don’t worry! Your day is almost over!"
        "You scared me!":
            y happy "Sorry, ddin't mean to!"

    y neutral "You have one more thing to do today."
    y "You remember what I said about ‘other times’?"
    y "Well, now is the ‘other time’!"
    y "Follow me!"

label sell_drugs_day1:
    scene test_bg
    show yuzuki neutral at Position(xalign=0.5) with fade
    y "I’m sure you’ve already figured this out, but we’re selling drugs."
    y "You won’t always be going out to meet people in strange alleyways, but tonight is the exception."
    y "I’ve already talked with them, so all you have to do is seal the deal."

    menu seal_deal:
        "I got this.":
            y happy "That's great!"
        "Are you sure I can do this?":
            pF "Maybe you should show me first?"
            y happy "You'll be fine!"
            "He pats you on the back, maybe too hard."

    y neutral "They're here!"

    "A small, meek, but well-dressed woman comes to stand across from you in the alleyway."
    "You feel a sharp pain in your back as Qiu Rangxi shoves you forward with his elbow."
    "You plaster the most customer service smile you can manage on your face."
    jump testInterrogationMechanic

label debug_seal_deal_success_fail:
    menu succeed_fail:
        "Success.":
            "The woman walks away with her newly purchased goods. She seems pleased."
            y "See? You were great!"
        "Fail.":
            "The woman looks offended and walks away with a huff."
            y neutral "..."
            y angry "Did you do that on purpose?"
            y "You just lost us a lifelong customer."
            y upset "It’s not so bad here, but if you fail these later down the line? You should be worried for your neck."

label debug_hub_day1:
    jump hub
