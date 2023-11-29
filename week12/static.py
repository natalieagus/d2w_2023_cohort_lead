# typical usage: implementation of standard formulas that are used by many other components in a project
# class Kinematics:
#     initialForce =
#     gravity =
#     mass =

#     # usually they are pure functions
#     @staticmethod
#     def computeProjectileForce(...):
#         return force_value

# force_value = Kinematics.computeProjectileForce(...)

class A:
    x = 5  # static/class variable

    def __init__(self, value):
        self.value = value
        print("value: ", self.value)

    # regular instance method
    def instance_method(self):
        print("this is self: ", self)

    @staticmethod
    # does not receive a self reference
    # typically used for computation of known formulas, or changing static variables
    def static_method():
        print("static method is called")


instance_one = A(10)
instance_two = A(20)
# this will call the instance method, with reference to SELF
instance_one.instance_method()

# this will call the static method, no reference to SELF (instance_one)
instance_one.static_method()
# instance variable: value
print(instance_one.value)  # 10
print(instance_two.value)  # 20

# we can access class variable from instance, BECAUSE these instances do NOT have "x" as instance variable
print(instance_one.x)
print(instance_two.x)

A.static_method()  # call static method, no "self" needed
A.x = 30  # access class variable from the class name, not the instance
print("after static variable modified:")
print(instance_one.x)
print(instance_two.x)

# remember python can create new instance variables outside the class? lets create x
instance_one.x = 99
print("after modifying instance_one x variable:")
print(instance_one.x)  # 99, accessing instance variable x because it exists
# 30, accessing CLASS variable because the instance does not have x
print(instance_two.x)
