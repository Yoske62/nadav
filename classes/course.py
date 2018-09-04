class course:
    a = "a"
    b = "b"

    @property
    def a(self):
        return self.a

    @property
    def b(self):
        return self.b

    def toString(self):
        return self.a + self.b

    def bla(val):
        return val + val;