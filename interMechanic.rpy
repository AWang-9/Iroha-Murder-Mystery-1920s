default chosenGift = ""
default evidence = ""

label testInterrogationMechanic:
    scene test_bg with fade
    "WElcome to the test interrogation mechanic."
    "Here, we'll be trying to prove something."

label beginInterrogation:
    pF "It's Yuzuki's birthday today, so I should make him something nice."
    pF "What do I know about him?"
    pF "He's loud and extraverted."
    pF "He's the oldest of his brothers."
    pF "He likes cake a lot."
    pF "He loves his desserts."
    pF "I saw he ran out of cocoa powder recently."
    pF "So, the thing I should make him is..."


    menu YuzukiDessert:
        "A chocolate cake.":
            $ chosenGift = "cake"
            pF "I'll bake him a cake. Why?"
        "A cheese casserole.":
            $ chosenGift = "casserole"
            pF "I'll make him a cheese casserole. Why?"
        "Nothing at all--he'd appreciate a new book.":
            $ chosenGift = "book"
            pF "I'll get him a new book. Why?"

    menu justify:
        "He's the oldest of his brothers.":
            $ evidence = "he's the oldest of his brothers."
        "He's loud and extraverted.":
            $ evidence = "he's loud and extraverted."
        "He likes cake a lot.":
            $ evidence = "he likes cake a lot."
        "He loves his desserts.":
            $ evidence = "he loves his desserts."
        "I saw he ran out of cocoa powder recently.":
            $ evidence = "he ran out of cocoa powder recently."

label confirmStatement:
    pF "So, I'll give him a [chosenGift], because [evidence]"
    pF "Does this make sense?"
    menu confirm:
        "Yes.":
            jump testInterrogConclusion
        "No.":
            pF "let me think on this again."
            jump testInterrogationMechanic


label testInterrogConclusion:
    pF "I'll give him a [chosenGift], because [evidence]."
    "You have completed the interrogation."
    jump hub
