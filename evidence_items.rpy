####
#ORDER FOR EVIDENCE ITEMS:
# 1) Hairpin
# 2) Bread
####

init python:
    ## used for creating an item
    class itemInfo:
        def __init__(self, name = "???",
                    description = "???", notes = "???",
                    index = -1,
                    imageName = ""):
            self.name = name
            self.desc = description
            self.index = index

            # portraits for the item
            self.img = "images/" + imageName + ".PNG"

        def setPrev(self, prevItem):
            self.prev = prevItem

        def setNext(self, nextItem):
            self.next = nextItem

define hairpin = itemInfo(name="hairpin", imageName = "test_hairpin",
                index = 0,
                description = "Found in Shio's room.\nIt's part of a set.\nSaid to be the murder weapon, but doesn't look like it.")
define hearsayEvid_ShioKillStyle = itemInfo(name = "Shio's killing style",
                                        imageName = "test_button",
                                        index = 1,
                                        description = "Found when discussing the death of a politician.\n'The method of killing is eerily reminiscent of how Shio makes his kills.'")
define bread = itemInfo(name="bread", imageName = "test_bread",
                index = 2,
                description = "A piece of warm, fluffy bread.\nMmm, bread...")

define all_items = [hairpin, hearsayEvid_ShioKillStyle, bread]
define lastItemIndex = 2

default selectedItem = ""
