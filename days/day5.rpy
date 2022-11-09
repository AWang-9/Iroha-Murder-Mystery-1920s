############
### Menu flags
### Reading articles
default readGirl = False
default readCities = False
default readReportings = False
default readVulnurable = False

### talking to Tomoe
default howLong = False
default danger = False
default inspired = False
############

label day_5:
    $ currDay = "day_5"
    $ nextDay = "day_6"

    # fade into restaraunt
    scene test_bg with fade
    "Friday morning, 6AM."
    "You weren’t able to sleep well last night, with the dead girl lingering heavily on your mind."
    "But you’re not allowed to come in late today, so you show up on time."
    "As you enter the restaurant from the back door, you overhear Iroha’s voice."
    "The man had left a strong impression on your first day."
    "You didn’t think you’d forget him anytime soon."
    "You see him downstairs, in the main area of the restaraunt."
    "It's rare to see him here. What's happening?"
    "Curious, you find a spot within hearing range to hide in."
    "Iroha isn't the only one down here."
    "There's an unknown man with him. The man is on his knees, begging."

    npc "I’ll have the money, I swear! I just need a week!"
    i "Another week of snorting yourself silly?"
    npc "No, I-"
    npc "I get paid next Monday and I’ll--I’ll be able to scrounge something else up, too. You’ll have your money, I swear."
    i "If I recall correctly, those were your exact words last week."
    i "Tsk."
    i "But there is one way you can pay off your debt and have some to spare."
    npc "What? I'll do anything!"
    i "Become the merchandise."

    "The man starts screaming for mercy and what sounds like a scuffle. His desperate pleads fade away as he’s dragged away."
    "You have the feeling you've stumbled upon something you weren't supposed to see."
    "To avoid getting caught eavesdropping, you scramble to leave."

    scene test_bg with hpunch
    "Before you can get very far, the doors slam open."
    show iroha sad at center with dissolve
    "Iroha steps out and looks you right in the eye, as if he had long known exactly where you were even without seeing you."
    i "Some people just never learn the consequences of paying off debts until it's too late."
    i thinking "Such a shame."
    i neutral "You should get back to work."

    hide iroha with dissolve
    "He leaves with that ominous statement."
    "Listening to the person who just sold off someone is a very good idea, so you hurry back to your station in the kitchen."
    "As you diligently dishwash, something keeps bothering you about the events of this morning."
    "Clearly, that man just got sold off. But there’s something else."

    pF "That girl from yesterday...Did she go through something similar to the man?"

    show yuzuki neutral at center with hpunch
    y "What girl?"
    pF "!!!"
    y happy "Haha!"
    y neutral "..."
    y worried "You okay?"
    y "You don't look so good..."

    menu do_not_look_good:
        "I'm fine.":
            pF "I'm fine."
            y "You really don't look fine."
        "I didn't sleep well.":
            pF "Haha, you caught me...uh, I was just falling asleep?"
            y thinking "..."
            y "What?"

    y worried "Maybe this whole week has been a lot for you."
    pF "Yeah, maybe you're right."
    y neutral "I know what you need!"
    pF "(A different job?)"
    y "You should take half a day off!"
    y happy "There’s a library nearby! I go there sometimes to relax y’know."
    y shocked "Are you staring at me because I don’t look like I read?"
    y happy "You’re right! I don’t! I only go there to get books per Satsuki’s requests. And they give free refreshments."
    y neutral "Isn’t it cool? A library that allows food and drink?"
    y "Yeah, it'll be a great place for you."
    y "Just get back here in time for your night shift, okay?"

    hide yuzuki with dissolve
    "Yuzuki leaves no room for argument and ushers you out of the restaurant, but not before giving you directions to the library."
label day5_library:
    # library background
    scene test_bg with fade

    "You arrive at the library, which is small and cozy. There are rows upon rows of books tightly packed together."
    "The receptionist gives you some complimentary tea."
    "You wander the aisles up and down, reading numerous book titles but not processing a single one."
    "Maybe Yuzuki was right, you really are out of it."

    show tomoe neutral at center with hpunch
    t "Ah."

    "He catches your arm as you stumble and it’s a miracle your tea did not spill all over him."

    pF "..."
    pF "Sorry."
    pF "I wasn't looking where I was going."

    "You look up at Tomoe and notice how his tall and wide stature looks like it’s barely fitting between the shelves of books."

    t "It's alright."
    pF "..."
    t "..."
    pF "...I didn't expect to see you here."
    t "Likewise."

    "Another awkward silence falls between the two of you."
    "You avert your attention to the shelves, trying to appear preoccupied with scanning book titles."
    "To your surprise, Tomoe speaks first."

    t "What brings you here?"
    pF "I'm taking a break."
    t "Mm."
    pF "What are you doing here?"
    t "Connecting the dots."
    pF "The dots?"

    "Tomoe takes you around to a small study table, littered with books and newspaper clippings and a notebook."
    "You lean down to take a look."
    "All of it is about human trafficking."

    pF "So, you’re investigating all of this?"

    "Tomoe nods."
    "You look again at the articles, and this time one of them catches your eye."
    "Under the headline is a photo of the girl you had found yesterday morning!"
    "Under this newspaper clipping you find more photos of the girl."

    t "Have you already written one?"
    pF "Written? Written what?"
    t "About the case."
    "He’s looking at you with a slight frown."
    "With a pang, you remember that he knows you as a reporter."

    pF "Oh, uh--not yet. Things have been…busy."
    t "Let me help."

    "He hands you some photos of the girl."

    pF "Then I assume you’ve already written an article on this?"
    "Tomoe nods."
    "He points down to one of the newspaper clippings on the desk. It’s the very one you had just looked at."
    "It's his name under the author."
    "Upon closer examination, you notice that all of these various articles on human trafficking are written by Tomoe."

    pF "You've done a lot."
    pF "You must be really invested in this."

    "Your mind flashes back to the scene this morning. Would Tomoe be writing about that eventually?"

    t "Yes."
    t "This is my life."
    t "I cover topics that don't show in conventional media."
    t "Like human trafficking."
    t "My goal is to bring these things to light and expose them."
    pF "These photos…look like they were taken up close. How did you get past the police?"
    t "I quickly learned the police never help."
    t "So I ignored them."
    t "Too many people don't want to hear about these topics."
    t "I learned how to get to places I shouldn't, on my own."

    "That explains the day you first met."
    "Tomoe lapses into silence and you take the opportunity to look through all the articles."

    menu tomoe_articles:
        "Article about the girl.":
            pF "She was just a child."
            pF "No one knows how she died."
            pF "'A sad accident.'"
            $ readGirl = True
        "Cities with the highest rates of human trafficking.":
            pF "Huh..."
            pF "One of the areas is the city where I work."
            $ readCities = True
        "Human Trafficking Reportings.":
            pF "All the recent reportings involve people of older age."
            pF "But the girl is an outlier...?"
            $ readReportings = True
        "Popular Human Trafficking Targets":
            pF "Drug addicts, and people heavily in debt."
            pF "It reminds me of the guy I saw this morning."
            $ readVulnurable = True
        "Finish looking.":
            if readGirl and readCities and readReportings and readVulnurable:
                pF "(Now's a good time to talk to Tomoe, too.)"
                show tomoe neutral at center with dissolve
                jump talk_Tomoe_day5
            else:
                pF "There's still more for me to read."
                jump tomoe_articles
    jump tomoe_articles

label talk_Tomoe_day5:
    menu talk_Tomoe_options:
        "How long have you been investigating this?":
            pF "How long have you been investigating this?"
            t "Around 10 years."
            $ howLong = True
        "Have you ever been in danger because of what you do?":
            pF "Have you ever been in danger because of what you do?"
            t "Yes."
            pF "How do you get out of it?"
            t "Through luck."
            $ danger = True
        "What inspired you to chase these topics?":
            pF "What inspired ou to chase these topics?"
            t angry "..."
            t "A friend."
            show tomoe neutral
            pF "(He seems unhappy with the thought. I shouldn't press.)"
            $ inspired = True
        "Finish talking.":
            if howLong and danger and inspired:
                jump go_lunch_with_Tomoe
            else:
                pF "Wait, there's more to talk about."
                jump talk_Tomoe_options
    jump talk_Tomoe_options

label go_lunch_with_Tomoe:
    "You check your watch and realize how long you’ve been talking."
    "And you realize that your stomach is growling."
    "Tomoe must be hungry as well--it’s past lunchtime."

    pF "Have you eaten?"
    t "No."
    pF "Let's go eat, then."
    t "Okay. There's a place I've been meaning to try."

    # should show a restaraunt/street background
    scene test_bg
    show tomoe neutral at center with fade
    "You follow Tomoe out of the library and head to a small nearby restaurant."
    "It's a cozy place, with 8888888888888888888888descriptions8888888888888888888."
    "As you sit down, Tomoe retrieves the chopsticks for both of you."

    pF "Thanks."
    t "Mm."

    "Not even a moment later, the owner of the restaurant comes and hands the both of you a menu. This place is clearly run by a family."

    pF "How did you find this place?"
    t "I know the owner."
    t "She's my neighbor."
    t "Also, try the dumplings."
    pF "Have you known each other long?"
    t "88888888888888 ;no clue what goes here, the doc was EMPTY;88888888888"

    # street background
    scene test_bg
    show tomoe neutral at center with fade
    "Your lunch date goes well and you both leave in high spirits."
    t "I hope we meet again."
    hide tomoe with dissolve
    "He walks away with that remark."

    pF "That was a nice experience."
    pF "It would be nice if we could meet more often."
    pF "But I should get back to work, before Yuzuki bites my head off."
    pF "'Be back for your night shift...' He should just give me the whole day off, if he's gonna be like this."
    pF "Whatever..."

    scene test_bg with fade


label debug_hub_day5:
    jump hub
