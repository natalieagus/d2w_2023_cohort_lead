class A:
    def __init__(self, inp):
        print("A is initialized")
        self.inp = inp

    def method(self):
        print("A")

    def __str__(self):
        return "This is A"


# B is an A
a = A("hello")


class B(A):
    # override
    def method(self):
        super().method()
        print("B")

# C is a B


class C(B):
    # override
    def method(self):
        super().method()  # do not call super()
        print("C")


c = C("hello")
c.method()  # C, B, A
print(c.inp)
c.inpp = "world"  # set attributes outside of class
print(c.inpp)
