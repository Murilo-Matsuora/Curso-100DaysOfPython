import time

def decorator_function(function):
    def wrppaer_function():
        time.sleep(2)
        function()
    return wrppaer_function

@decorator_function
def say_hello():
    print("Hello!")

@decorator_function
def say_bye():
    print("Bye!")

def say_greeting():
    print("How are you?")
