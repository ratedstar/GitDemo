

def func():
    return 1

print(func)
print(func())

def hello():
    return 'hello!'

greet = hello
print(greet())
print(hello())

del hello
#print(hello())
print(greet())
# when are getting an error after del hello again calling hello
# But when we are calling greet we are getting o/p even though we del hello greet is still pointing to the original
#function object
# return function within another function
def hello(name='yoga'):
    print("This hello() function has been executed!")
    def greet():
        return "\t This is greet() inside hello!"
    def welcome():
        return "\t This is welcome() inside hello!"
    # print(greet())
    # print(welcome())
    # print("This is the end of the hello function")
    print("I am going to return a function")
    if name == "jose":
        return greet
    else:
        return welcome


my_func = hello("jose")
#welcome() we get an error because scope is limited to hello
#print(my_func)
print(my_func())

def cool():

    def super_cool():
        return "I am super cool"
    return super_cool

#function as an argument
def hello():
    return 'Hi Jose'
def other(some_def_function):
    print("Other code runs here!")
    print(some_def_function())
#other(hello()) #'str' object is not callable if we pass method name with paranthesis
other(hello)
# without decorator
def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function")
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
# with decorator
def new_decorator2(original_func):
    def wrap_func1():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function")
    return wrap_func1()
@new_decorator
def func_needs_Tobe():
    print("I am decorated by decorator")
func_needs_Tobe()