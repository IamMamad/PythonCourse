from item import item

class room:
    def __init__(self, name, description="this is a Room"):
        self.name = name
        self.description = description
        self.items = []

    def describe(self, description):
        self.description = description

    def printItems(self):
        for item in self.items:
            print("there is", item.name, "in the room")

    def addItem(self, item):
        self.items.append(item)