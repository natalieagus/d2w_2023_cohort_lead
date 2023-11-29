# There are THREE purposes for getter and setter in general: manipulation, validation, and computation

# manipulation would be to have different kind of values being shown depending on who's getting it, e.g: your exam grades are shown as actual exam value to instructor, but they're "None" in your view (remember that this is not computation)

# validation when setting
# protect self._celcius to be in a valid range
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            # a better way instead of printing "value is invalid"
            raise ValueError(
                "Temperature below absolute zero is not possible.")
        self._celsius = value


# Usage:
temp = Temperature(25)
print(temp.celsius)  # Output: 25
temp.celsius = 30
print(temp.celsius)  # Output: 30

# temp.celsius = (
#     -300  # Raises ValueError: Temperature below absolute zero is not possible.
# )


# computed properties are usually getters
# post process your instance attributes to show to different users
# a good practice (vs storing area and diameter as instance vars), makes the code modular because when we change radius, then diameter and area are automatically updated when called
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        import math

        return math.pi * self.radius**2


# Usage:
circle = Circle(5)
print(circle.diameter)  # Output: 10
print(circle.area)  # Output: ~78.54

# form validation


class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Username must be a string.")
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters.")
        self._username = value


# Usage:
user = User("JohnDoe")
print(user.username)  # Output: JohnDoe

# user.username = "JD"
# Raises ValueError: Username must be at least 3 characters.
