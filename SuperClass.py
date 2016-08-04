class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

s = Filter()
s.init()
print (s.filter([1, 2, 3]))

# s1 = SPAMFilter()
# s1.init()
# print (s1.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))

class Calculate:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print ('Hi, my value is', self.value)

class TalkingCalculator(Calculate, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

hasattr(tc, 'talk')
hasattr(tc, 'fnord')
