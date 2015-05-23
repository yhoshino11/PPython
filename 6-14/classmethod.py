class Spam:
    def method(self):
        """Normal instance method."""
        print(self)

    @classmethod
    def clsmethod(cls):
        """Class Method"""
        print(cls)


Spam.clsmethod()

spam = Spam()
spam.method()
spam.clsmethod()
