class A:
    def __init__(self, inp):
        self.inp = inp

    def method(self):
        print("A")

# inheritance
# a B instance is an A


class B(A):
    def method(self):
        super().method()
        print("B")

# inheritance
# A C instance is a B


class C(B):
    # overriding of methods
    def method(self):
        super().method()
        print("C")


c = C(5)
c.method()
print(c.inp)
c.inpp = "something"  # adding additional attributes outside of the class
print(c.inpp)
