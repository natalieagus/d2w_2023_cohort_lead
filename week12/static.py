# class VectorHelper:
#     GRAVITY = ...
#     BASE_MASS = ...

#     def compute_trajectory(body1, body2):
#         ...
#         return ...

#     def compute_force(body1, body2):
#         ...
#         return ...


class A:
    x = 5

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print("this is self: ", self)

    def method_two():
        print("method two is called")


a_one = A("hello")
a_two = A("world")
# a_two.method_two()
print(A.method_two())

# at first, a_one does not have x instance variable, so it takes x STATIC/class variable
print(a_one.x)
print(a_two.x)

a_one.x = 20  # once set, when we print, we print the instance variable x

print(a_one.x)  # instance variable
print(a_two.x)

a_one.instance_method()
a_two.instance_method()

print("A.x: ", A.x)  # print class variable from the class name
print("A call instance method on a_one: ", A.instance_method(a_one))
