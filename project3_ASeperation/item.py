class item:
    def __init__(self, name, description="this is an Item"):
        self.name = name
        self.seen = False
        self.description = description
    
    def describe(self, description):
        self.description = description

        