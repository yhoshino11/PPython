class Spam:
    def __init__(self):
        self.__ham = 0

    @property
    def ham(self):
        return self.__ham

    @ham.setter
    def ham(self, value):
        self.__ham = value

    @ham.deleter
    def ham(self):
        del self.__ham


spam = Spam()
print(spam.ham)
spam.ham = 100
print(spam.ham)
del spam.ham
