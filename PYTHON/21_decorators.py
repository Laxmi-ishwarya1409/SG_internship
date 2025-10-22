# def my_decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After function call")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()






# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function call")
#         result = func(*args, **kwargs)
#         print("After the function call")
#         return result
#     return wrapper

# @my_decorator
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Laxmi")
