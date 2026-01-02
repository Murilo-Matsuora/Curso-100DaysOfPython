# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#         else:
#             print("User is not logged in. Action denied.")
#     return wrapper

# @is_authenticated_decorator
# def create_blog_poster(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user = User("Murilo")
# new_user.is_logged_in = True
# create_blog_poster(new_user)

# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")
        return function(*args)
    return wrapper

def mult(args):
    total = 1
    for element in args:
        total *= element
    return total


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)

@logging_decorator
def b_function(*args):
    return mult(args)
    
a_function(1,2,3)
b_function(1,2,4)