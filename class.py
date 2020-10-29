class PartyAnimal(object):

    """docstring for PartyAnim"""
    x=0
    def __init__(self):
        print("I am Constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("Iam destructed", self.x)


an = PartyAnimal()
an.party()
an.party()

an=40
print("an contains", an)
