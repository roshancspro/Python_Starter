from decorator import do_twice

@do_twice
def greet(msg):
    print("Hello "+msg)

greet("Python")