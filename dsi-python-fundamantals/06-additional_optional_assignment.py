'''
With this class:
    1) Figure out a better way to print the turtle's name
    2) Capture the turtle's size
    3) Compare two turtle's sizes
    4) Use the turtle class in another script
Time Permitting:
    5) Create a function that has the turtle eat and grows its size
    6) Add docstrings
    7) Use a name block
'''

class Turtle():
    def __init__(self, name, color):
        self.greeting = "Hi, I'm a turtle"
        self.name = name
        self.color = color

    def whats_your_name(self):
        print("Hi, my name is {}".format(self.name))

my_turtle = Turtle("Franklin", "green", 32.4)
my_other_turtle = Turtle("Joey", "brown", 32.4)
