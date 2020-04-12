class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.daysold = self.dayOld()

    def greeting(self):
        print("Hi, My Name is", self.name)

    def dayOld(self):
        days = 365 * int(self.age)
        return days