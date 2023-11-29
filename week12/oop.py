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

# shouldn't do this but let's discuss it for fun


class MyClass:
    def __init__(self, value):
        # this function actually is just meant to initialize INSTANCE variable
        self.value = value
        print("Initialized with value:", self.value)


# this calls the function that CREATES a new instance, and another function that INITIALISES the instance variable
obj = MyClass(5)

# what's happening under the hood
# Create an instance
obj = MyClass.__new__(MyClass)

# Call __init__ without creating a new instance explicitly
MyClass.__init__(obj, 10)  # Pass the instance as the first argument explicitly
