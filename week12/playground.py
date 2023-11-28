def function_one(x):
    return x*x


def function_two(y):
    return function_one(y) + function_one(y)


text = "ABC"


def function_three(z):
    text += "DEF"


def function_four(a):
    if (text == "ABC"):
        return a
    return None

# in a pure function, the same input produces the same output
