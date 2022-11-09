##################
### flags for body investigation
default lookedSleeve = False
default lookedWrist = False
default lookedFace = False
default lookedFloor = False
##################


label day_6:
    $ currDay = "day_6"
    $ nextDay = "day_7"

    # fade into restaraunt
    scene test_bg with fade

    "Saturday morning, 11AM."
    "You're taking your lunch break when Yuzuki comes in and sits across from you."

    show yuzuki neutral at center with dissolve
    y "Hey."
    pF "What's up?"
    y "So, I talked with Chang Shaoqing today--you know, the paper boy?"
    y "He gave me this."

    "Yuzuki tosses a newspaper onto the table. On the headline, another person has died."
    "Someone well-known for their generosity and desire to do goodwill."
    "They’re someone who constantly donates to charity and has funded countless nonprofit volunteer organizations."

    pF "Who would do this? It's awful?"
    y "Me, apparently."
    pF "Excuse me?"
    y "Keep reading."

    "You speedily read through the article."
    "The person was confirmed dead from a <<<coerced drug overdose.>>>"
    "There were clear signs of a struggle."
    "You recognize the drug in question."
    "It’s one of the ones you sold with Yuzuki, on your first day."

    pF "But if they overdosed, how is it your fault?"
    y "But that’s the thing. <<<We never sold to this guy>>>. He wouldn’t even buy from us in the first place, anyway--"

    scene test_bg
    show yuzuki shocked with hpunch

    "The police burst in abruptly."
    show yuzuki upset
    "Yuzuki’s face flickers in alarm, before he gestures for you to stay still and seated."
    "He doesn’t answer your questioning whispers and just walks away from your table, going to greet the officers."
    hide yuzuki with dissolve

    "You watch as the police disperse into the restaurant and begin to pull people aside."
    "You lower your gaze to your food and try not to stand out."
    "No luck. After a bit, an officer taps you on the shoulder and asks to speak to you to the side."
    "As you go with them, you glance up to the second floor."
    "<<< Iroha and another officer are speaking with each other. They seem relaxed.>>>"

    "Your heart is racing a million miles an hour. While you are innocent, you’re not exactly an upstanding citizen of society."

    pol "Who are you? What are you doing here?"
    pF "‘I'm [pF]. I’m a dishwasher here."
    pol "What? No, I mean, who do you work for?"
    pF "Uh, the restaraunt?"
    pol "No. I mean: Yuzuki, Satsuki or Shio."
    pF "Oh, uh..."

    "You glance uselessly at the kitchen door, like Yuzuki would walk in if you willed it enough."

    pol "Calm down."
    pol "I already know you sell drugs."
    pF "!!!"
    pol "Oh, you're new here. That explains it."

    "The police doesn’t seem that interested in your nightly activities, even with how illegal they are."
    "Instead…they already seem to have details on the case."
    "They’re not gathering evidence--they’re asking for your perspective."

    pol "How often do you sell?"
    pF "Every night, so far."
    pol "Hm, that doesn't help. Once a week, huh?"
    pF "Excuse me?"

    "The police stares at you and deliberately writes something down, without breaking eye contact."

    pol "You sell once a week. What day?"
    pF "Um, Mondays?"
    pol "You sell on Sundays."
    pF "...Well, alright."

    "For some reason, the police seem like they’re making you an alibi."
    "With Sunday being the sale day, there's no way you could have sold to the person who died last night."
    "Which was a Friday."

    pol "You're a small fry. Don't worry."

    "He sends you back outside so he can continue his questioning undisturbed."

    pF "...Huh."

    "As you walk out, you spy Tomoe turning the corner."

    pF "Tomoe!"

    "Tomoe looks up at your call, and approaches."

    show tomoe neutral at center with dissolve

    t "Hello."
    pF "What are you doing here?"
    t "Reporting. Isn't that what you're here for?"
    pF "..."
    t "..."
    pF "Oh yeah--yes, that is what I'm here for."

    "Tomoe looks at the building you’d just come out of."
    show tomoe angry
    "Distaste crosses his face. Its the most emotion you’ve ever seen him express."

    pF "Is...Something wrong?"
    t "I don't like this place."
    t thinking "8888888888888 ERROR no EXPOSITION FOUND 88888888888888"
    t neutral "Anyway."
    t "Did you find anything in here?"
    pF "No, not really. It's hard to get through the police."
    t thinking "Hm."

    "You don’t like that look on Tomoe’s face. Before he can suggest something crazy to get past them, you scramble to distract him."

    pF "How about we go see the crime scene instead? I haven’t gotten close yet."
    t neutral "Good idea. If the police are here, there will be less there."
    t "And I need to go there anyway."

label charity_death_location:
    # fade into charity guy death location
    scene test_bg with fade
    show tomoe neutral at center with dissolve

    "88888888888 ERROR. Scene description not found. 88888888888"

    pF "The body is still here?!"
    pF "Really...I guess the police really haven't gotten here yet."
    pF "Why were they so quick to get to the restaraunt, though?"
    t "Hmm..."

    menu examine_charity_death_body:
        "Examine the ripped sleeve.":
            "You pull the sleeve up the arm and see a red pinprick."
            pF "(An injection site?)"
            $ lookedSleeve = True
        "Examine the person's wrist.":
            "There's a red mark there, in the shape of a handprint."
            $ lookedWrist = True
        "Examine the person's face.":
            "There's a white powder on their face."
            $ lookedFace = True
        "Examine the room.":
            "There's a cufflink that belongs to Yuzuki here, just on the carpet."
            $ lookedRoom = True
        "Finish examination.":
            if lookedSleeve and lookedWrist and lookedFace and lookedRoom:
                jump finish_charity_death_examination
            else:
                pF "There's still more to see..."
    jump examine_charity_death_body


label finish_charity_death_examination:
    scene black
    "After you investigate the crime scene, the two of you part ways and you head back to the restaurant."
    "You find the place has been closed for the day."

label debug_hub_day6:
    jump hub
