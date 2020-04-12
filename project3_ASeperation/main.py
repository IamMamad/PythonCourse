from item import item
from room import room


book = item("Book")
book.describe("Two Centuries of Silence")

doll = item("Doll")
doll.describe("this is a stuffed Zebra")

bedroom = room("Bed Room", "This is your bedroom")
bedroom.addItem(book)
bedroom.addItem(doll)
bedroom.printItems()

