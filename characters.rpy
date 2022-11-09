init python:
    ## used for creating a Character for the profiles
    class CharProfile:
        def __init__(self, name = "???",
                    age = "???", height = "???",
                    weight = "???", affiliation = "???",
                    index = -1,
                    description = "???", notes = "", imageName = ""):
            self.name = name
            self.age = age
            self.height = height
            self. weight = weight
            self.affl = affiliation
            self.desc = description
            self.notes = notes
            self.index = index

            # portraits for the character
            self.img = "images/" + self.name + "/Neutral_" + imageName + ".PNG"

define yuzuki = CharProfile(name="Yuzuki", imageName = "LineY",
                            index = 0,
                            description="Yuzuki is a cheerful, happy go lucky person who managed to nail you your current job. He's a bubbly and cheerful lad, always with a smile on his face.",
                            notes="A great friend!")

define shio = CharProfile(name="Shio", index=1, imageName= "SketchSh")
define satsuki = CharProfile(name="Satsuki", index=2, imageName= "SketchSa")
define iroha = CharProfile(name="Iroha", index=3, imageName= "SketchI")
define tomoe = CharProfile(name="Tomoe", index=4, imageName="SketchT")

define allChars = [yuzuki, shio, satsuki, iroha, tomoe]
define lastCharIndex = 4
default selectedChar = ""
