class Secretive:
    def __inaccessible(self):
        print ("Bet you can\'t see me...")

    def accessible(self):
        print ("The secret message is:")
        self.__inaccessible()


s = Secretive()
s.accessible()
print(s.__class__)