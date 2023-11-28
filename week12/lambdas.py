# Lambdas are anonymous functions in Python, often used for small, ONE TIME purposes
# format ---> lambda arguments : expression

double_lambda_function = lambda x : x*2


def double_function(x):
    return x*2


print(double_lambda_function)
print(double_function)

result_from_lambda_function = double_lambda_function(5)
print("result_from_lambda_function", result_from_lambda_function)


complicated_lambda_function = lambda x,y,z: (x+y) * z if x > y else (y-x)/z


def complicated_function(x, y, z):
    if x > y:
        return (x+y)*z
    return (y-x)/z


# functions as an input
data = [
    {"name": "Alice", "age": 25, "salary": 25},
    {"name": "Trudy", "age": 45, "salary": 80},
    {"name": "Eve", "age": 105, "salary": 90},
    {"name": "Bob", "age": 35, "salary": 10},
]

# want to sort the list of dicitionaries by age
# key in sorted function should be a FUNCTION that tells sorted HOW to sort
sorted_data = sorted(data, key=lambda x: x["age"])

# sorted function (default python) will USE your lambda function, or get_age and call it to use that as the value to compare with within the elements of data


def get_age(person):
    return person["age"]


sorted_data_by_function = sorted(data, key=get_age)


def test_lambda(x): return [[y*y for y in z] for z in x]


print(test_lambda([[1, 2], [4, 2], [3, 5], [5, 4]]))
