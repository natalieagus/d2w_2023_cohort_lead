# purpose of property:  validation, computation, and manipulation
class Person:
    def __init__(self, name, age, email, designation):
        self._designation = designation
        self._name = name
        self._age = age
        self._email = email

    @property  # getter returns as-is but this age property is more important in the setter's side
    def age(self):
        return self._age

    @age.setter  # validate someone's age
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter  # common validation for email structure
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value

    # manipulation (we show things differently to the caller of this function, but it's more of preference)
    @property
    def name(self):
        output = self._designation + " " + self._name
        return output

    # No need for a setter for name in this example
    @property  # computed property based on age
    def birth_year(self):
        current_year = 2023  # Assuming the current year is 2023
        return current_year - self._age

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Email: {self._email}, Birth Year: {self.birth_year}"


# Creating a Person instance
person = Person("Alice", 30, "alice@example.com")

# Using computed property
print(person.birth_year)  # Output: 1993 (assuming current year is 2023)
