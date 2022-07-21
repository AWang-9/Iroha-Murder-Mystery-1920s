init python:
    ## used for creating a Character for the profiles
    class CharProfile:
        def __init__(self, name = "???",
                    age = "???", height = "???",
                    weight = "???", affiliation = "???",
                    description = "???", imageName = ""):
            self.name = name
            self.age = age
            self.height = height
            self. weight = weight
            self.affl = affiliation
            self.desc = description

            # portraits for the character
            self.imageName = "images/" + imageName + ".PNG"

default yuzuki = CharProfile(name="Yuzuki", imageName = "%_sSketchY")
