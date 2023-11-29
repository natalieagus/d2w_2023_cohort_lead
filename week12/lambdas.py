def double_function(x): 
    return x*2 

# lambda args : expression
double_function_lambda = lambda x : x*2

print("result from lambda: ", double_function_lambda(5))

data = [
    {"name": "Alice", "age": 25, "salary": 25},
    {"name": "Trudy", "age": 45, "salary": 80},
    {"name": "Eve", "age": 105, "salary": 90},
    {"name": "Bob", "age": 35, "salary": 10},
]

# lambda z is only used for this sorted function, and NOT anywhere else in the code, so it's neater to define it as a lambda (anonymous function) instead of a full blown function (with def keyword)
sorted_data = sorted(data, key= lambda z : z["salary"])
print("sorted_data", sorted_data)

def get_age(person):
    return person["age"]

sorted_data = sorted(data, key=get_age)
print("sorted_data", sorted_data)

# x, y are lists, z is an int
complicated_function = lambda x, y, z : [[i for i in x] for j in y] * z

print(complicated_function([1,2], [2,3], 5))







