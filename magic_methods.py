class Bird:
  def __init__(self):
    self.hungry = True
  def eat(self):
    if self.hungry:
      print ('Aaaah...')
      self.hungry = False
    else:
      print ('No, thanks!')

class SongBird(Bird):
  def __init__(self):
    self.sound = 'Squawk!'
    Bird.__init__(self)
  def sing(self):
    print (self.sound)

#Test
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
