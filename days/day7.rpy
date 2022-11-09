### Flags for menus
### who framed Yuzuki
default who = False
default justOne = False
default why = False
########################

label day_7:
    $ currDay = "day_7"
    $ nextDay = "-1"

    # fade into Iroha's office
    scene test_bg
    show yuzuki neutral at center with fade
    "Sunday morning, 10AM."

    "You’re sitting across from Yuzuki in Iroha’s office."
    "It's only the second time you've been here, but it's still intimidating."
    "Iroha isn't here right now. It's just you and Yuzuki."
    "The both of you are trying to figure out who would frame Yuzuki."

    menu who_framed_Yuzuki:
        "Who would do this?":
            y thinking "I don't know, but so far it's been targeting the three of us."
            y "Does that mean Iroha is next?"
            $ who = True
        "Do you think it's just one person?":
            y thinking "I'm not sure."
            y "But you took a look at all those scenes, yeah?"
            y "Was there something that connects them all together?"
            $ justOne = True
        "Why is this happening?":
            y thinking "I mean."
            y "What we do isn't exactly legal, hm?"
            y "Maybe someone has something against us."
            y neutral "Understandable, honestly."
            $ why = True
        "Finish talking.":
            if who and justOne and why:
                jump backward_interrogation
            else:
                pF "There's still more to figure out."
    show yuzuki neutral
    jump who_framed_Yuzuki


label backward_interrogation:
    show yuzuki neutral at Position(xalign=0.25, yalign=1.0) with move
    show iroha neutral at Position(xalign=0.75, yalign=1.0) with moveinright
    "Iroha walks in and somehow knows what you’ve already been talking about."

    i "These murders have gotten troublesome."
    i "You've been investigating, no?"
    pF "Yes."
    i "Tell me what you know."

    "8888888888 ERROR BACKWARDS INTERROGATION NOT FOUND 8888888888888"

label after_backwards_interrogation:
    show yuzuki shocked
    pF "It's Tomoe?!"
    i "Ah. You know him."
    y thinking "Uh, who?"

    i "888888888888 ERROR. DIALOGUE NOT FOUND. 88888888888"

    show yuzuki worried
    i "Honestly."
    i "He never learns."
    i "Yuzuki, go fetch your brothers and bring them here."

    hide yuzuki with dissolve
    show iroha neutral at center with move

    "Yuzuki does so with haste. When they all get back..."

    i "Come with me. We have a manhunt to do."

label final_day_bar:
    # should be the bar
    scene test_bg with fade

    "You enter the bar first, so as to not cause suspicion in Tomoe."
    show tomoe neutral at center with dissolve
    "Tomoe is there, as expected, sitting at his usual table."

    t "Oh, hello."
    t "Don't normally see you at this time."

    menu caught_Tomoe:
        "The game is up, Tomoe!":
            t shocked "What are you talking about?"
        "Why would you do this?":
            t "Do what?"

    show tomoe neutral
    pF "You know exactly what you did."
    pF "I thought you stood for justice! How could you stoop so low?"
    t "..."
    t thinking "I think you're confused."


    "8888888888 Iroha DRAMATICALLY ENTERS. 8888888888888888"

    show tomoe neutral at Position(xalign=0.25, yalign=1.0) with move
    show iroha neutral at Position(xalign=0.75, yalign=1.0) with moveinright

    i "I don't think he is."

    "Tomoe rises to his feet."

    t angry "...Iroha."

    "Iroha lets out a light sigh."

    i "you’ve caused me quite a bit of trouble, hm? Why don’t we take this outside?"
    t "Are you here to repent? Or to keep ripping apart lives?"
    i "I don't know what you're talking about."
    i "Have you gone mad?"
    i "Is this you, trying to be a hero?"
    t "This is me, trying to remind my FRIEND (italics be added later) where he came from."
    i "Oh?"
    i "Those times are long gone. Pull yourself out of the past."
    t "So you're fine with it?"
    t "Being like those rich parasites?"
    t "Bleeding the poor dry and throwing them out like trash once you’re done?"
    i "Look between the two of us. Who's struggling?"

    "Tomoe sighs and slumps in resignation."

    t thinking "I suppose my friend really is dead."
    t angry "Well then-"
    show iroha shocked

    "He whips out a pocket knife and lunges."

    menu choose_ending:
        "Help Iroha.":
            jump help_Iroha
        "Help Tomoe.":
            jump help_Tomoe

label help_Iroha:
    show iroha sad
    "Tomoe lunges for Iroha with his pocket knife."
    "You don’t know what overcomes you, but you’re lunging forward and catching Tomoe around the waist."
    "Your body weight interrupts his movements somewhat--until a huge hand grabs your arm and bodily flings you away."

    t "Don't."

    "Off to the side, you glimpse Shio whipping out his killing hairpin and lunging while Tomoe is distracted."
    "Yuzuki also runs forward to grab Tomoe’s knife."
    "Satsuki has run to the phone, and is calling the police--the corrupt police, you know now."
    "Iroha is just watching, no emotion on his face, as Shio’s hairpin sinks into Tomoe’s neck."
    show tomoe shocked
    "When Shio pulls it out, a spray of blood follows."
    "Tomoe collapses, and you watch him collapse."

    # grey him out and drop him if possible
    hide tomoe with dissolve
    hide iroha with dissolve

    "You stare at his dying body, breathless and in shock from what you’ve just seen."
    # make things blurry if possible
    "Things are blurry. There’s sounds and voices around, but you aren’t hearing them."
    "You stay there in a state of numbness until a hand touches your shoulder and shakes you."

    show yuzuki worried at center with dissolve
    y "[pFirst]!"
    y "Are you okay--that's a stupid question."
    y "Just look at me, okay?"
    y "Don't look to the side."
    y "Just look atm e. Focus on me."

    "He grabs your arms and hauls you back up to your feet. You sway and he catches you before you can fall."

    y "Shit."
    y "Stay with me, okay?"

    "He hurries you out of the bar."

    scene black
    jump epilogue

label help_Tomoe:
    "Tomoe lunges for Iroha with his pocket knife."
    "You see a glimmer from the side and see Shio whipping out his killing hairpin."
    "You lunge at Shio and tackle him before he gets a chance to move."

    sh "You fucker--"

    "Shio’s a lot smaller than you are, so while he’s a slippery little thing, you manage to keep him down."
    "Long enough to hear the wet sound of wet gasping, and of Yuzuki and Satsuki’s shouts."
    "Tomoe has slit Iroha's throat."
    "You suddenly feel a sharp pain in your neck."
    "Slowly looking down, you realize Shio is reaching up to your neck."
    "And your neck hurts."
    "He's stabbed you with the needle."
    "Scowling, Shio tosses you off and rips his needle out, and the pain makes you white out for a moment."
    scene test_bg with fade
    "When you come to again, the world is sideways."
    "It’s getting cold, but something so warm is pooling underneath your neck."
    "You blurrily see Yuzuki staring at you."

    show yuzuki worried at center with dissolve

    y "[pFirst], why?!"

    "Your eyes drift back to where Iroha is dying. Despite everything, you smile."

    pF "888888888 MAY CHAOS TAKE THE WORLD 888888888888888888"
    pF "Thank you...for everything."
    pF "See you soon."

    jump end_credits

label epilogue:
    scene black with fade
    "It’s been two weeks since Tomoe’s death."
    "When the police arrived, they were paid off by Iroha."
    "They roped the area off and cleared the man of any suspicion."
    "When the news covered the murder, Tomoe was painted as a mentally unstable villain."
    "Iroha and the others were just unlucky bystanders."
    "You're still working at the restaraunt, but your job has changed."
    "Now, you work with Satsuki, doing simple clerical tasks."
    "You don't have to go out to sell anymore, and your pay has also doubled--probably because Yuzuk felt bad you saw the murder."
    "Iroha is cold, but...he's right."
    "There's no point in struggling and slaving away with trying to bring 'justice'."
    "It'll just end in failure, anyway."
    "The world is already against the poor."
    "You can only do what you must to survive."

    jump end_credits
