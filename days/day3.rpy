label day_3:
    $ currDay = "day_3"
    $ nextDay = "day_4"

    # fade into kitchen
    scene test_bg with fade
    "Wednesday morning, 8AM."

    "You're at work and someone slapped a newspaper down on the counter."
    "It contains details about the politician's death."
    "We didn't write this part yet :/"
    "You're told to get back to work."

    # fade to black
    # fade back into kitchen
    scene test_bg with fade

    "You had been hard at work for a while now, when Yuzuki calls you over."

    show yuzuki neutral at center with dissolve
    y happy "Great news! We got the police off our back!"
    y neutral "And in other news, Shio’s asked to borrow you for the day. So get to it!"
    hide yuzuki with dissolve

label shio_office_morning:
    # should be Shio's office
    scene test_bg
    show shio neutral at center with fade

    sh "Took you long enough."
    sh "You’re going to be a distraction today."
    sh "I have a meeting with an important…client, but I need them to be alone."
    sh "Their partner never leaves them though--so your job is to pull them away."
    sh "Take them to \[some room here\[--my actually capable subordinates will take care of them."
    sh "Got it?"

    menu shio_assistant:
        "Yes.":
            sh "Good."
        "No.":
            sh "Too bad."

    "Shio gives you a disguise."

label shio_office_meeting:
    # should be another office
    scene test_bg with fade

    "Shio’s client walks in with their partner."
    "Shio gives you a hard pinch and jerks his head at the person’s partner."
    "You approach..."

    "And apparrently have another interrogation mechanic."
    "Anyway..."

    "With the help of Shio’s underlings, who seemed to have come from nowhere, you successfully knock out and lock the partner into a room."
    "You hurry back to the office, just in time to see--"

    # stab splatter sound effect
    scene test_bg with hpunch

    "--Shio's business partner toppling over on the carpet."
    "Shio's hairpin is embedded in the man's neck."
    show shio neutral at center with dissolve
    "Shio doesn't seem bothered by that fact, and just reaches down to pull out his hairpin."
    "He wipes it off and slides it back into his hair."
    "He glances at you."
    "<<<You can't help but notice that he is exceptionally free of blood, and the spread of blood is minimalized.>>>"

    sh "Did you do it?"
    pF "Yes."
    sh "You're marginally competent."
    sh "Now give me back my dress."

    # should be Shio's office
    scene test_bg with fade
    "The two of you head back to Shio’s office. You swiftly change."
    "As you do, you take a look around the room."
    "You notice an array of hairpins on a nearby shelf, resting on their soft velvet pillow, but one is missing."
    "Judging from the set’s style, the missing one is the one that Tomoe found."
    "But...All of them are quite dull."
    "Is the missing one the exception?"

    "As you’re about to leave, Yuzuki walks in."
    show yuzuki neutral at center with dissolve

    y "You done yet? The kitchens need you!"

    scene black

label debug_hub_day3:
    jump hub
