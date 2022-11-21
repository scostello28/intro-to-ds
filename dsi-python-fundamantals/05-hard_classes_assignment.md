# Instructions

Tonight we'll be working on building out the `OurClass` class that we looked at in lecture, as well as building out another class that we'll have interact with `OurClass`. We'll call that class `Member`. Your goal by the end of the night is to implement these classes by following along with the guidelines below (i.e. implementing the classes with the attributes and methods discussed below), such that you have a firmer grasp on building your own classes and having them interact with each other.  

# Assignment Questions

### Part 1 - Building out `OurClass`

We're going to rework `OurClass` a little. As a reminder, here is what we settled on during lecture:

```python
class OurClass():

    def __init__(self, name, location, size=0):
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False

   def add_question_asked(self, question):
        self.questions_asked.append(question)

   def add_class_members(self, num):
        self.size += num

        if self.size >= 20:
            print('Capacity Reached!!')
            self.at_capacity = True

   def check_if_at_capacity(self):
        return self.at_capacity
```

1. The first thing you are going to do is to remove the `add_question_asked` method from `OurClass`. You can also remove the `questions_asked` attribute that is stored on the class, too. In terms of the `add_question_asked` method though, we are going to end up moving it into the `Member` class we will build, so it might be a good idea to keep that code in your back pocket.  
2. Next, you should add an attribute to the class called `members`. Modify the `__init__` function so that it takes an additional parameter, called `members`, which will be stored as the `members` attribute on the class. Make the default value in the `__init__` method definition for this `None`. Then, in the `__init__` method itself, if a value for the `members` parameter is passed in, use that to assign to the `members` attribute. Otherwise, initialize the `members` attribute to an empty list (**Note**: We didn't use an empty list as the default value for the `members` attribute because it is bad practice to use mutable data types for default values).
3. Now, alter the `add_class_members` method in `OurClass` to not take in a number (e.g. the `num` parameter), but instead a new member. Change the function definition to take in that member parameter, and then add that member to the `members` list attribute of the class. You should keep the rest of the code the same (i.e. adding 1 to the `size` attribute of the class and checking the `at_capacity` attribute of the class).  
4. Finally, let's refactor our code a little bit. We're checking the capacity twice above, once in the `__init__` method and then once in the `add_class_members` method. Let's instead just build this into the `check_if_at_capacity` method. Change that method so that we simply check if we are over a certain size (lets say 31) and return a `True` or `False`. After modifying this method, change the code in the `__init__` and `add_class_members` methods to take advantage of it.

### Part 2 - Building out the `Member` class

Now we're going to start working on the `Member` class. Then, we'll cycle back to actually have the `Member` class interact with the `OurClass` class.

1. Start out and define the `Member` class. Construct it such that users of the class need to instantiate it with an inputted `name`, `hair_color`, and `birthdate` (i.e. these will be accepted in the `__init__` method).  
2. Now, alter the `__init__` such that it creates a `questions_asked` attribute that starts out as an empty list.  
3. Build a method called `add_question_asked` that takes in `question` as a parameter and adds it to the `questions_asked` attribute on the `Member` class.  
4. Build a new method into the class called `add_coded_line` that takes in a string (of supposed code), and appends that string to an attribute called `lines_of_code` (you'll also have to add this to the `__init__` method). Also in that method, increment an attribute called `num_lines_coded` (you'll also have to add this to the `__init__` method). You can initialize it with a 0 for its value.  
5. Now, let's build upon that `add_coded_line` method. Within that method, we're going to call another method, named `get_coding_level`, that we will now create. In `get_coding_level`, we want to determine what the coding level is of our `Member`. If they've coded less than or equal to 100 lines of code, they will be a `beginner`; more than 100 but less than or equal to 1000, a `novice`; more than 1000 but less than or equal to 10000, an `intermediate`; and greater than 10000, a `master`. So, `get_coding_level` should use the attribute to determine what `coding_level` the `Member` is at. Note that this means you will have to do a couple of things:

* Define the `coding_level` attribute on the `Member` class. Initialize it to be `beginner`.
* Define and build the `get_coding_level` method, as described above.
* Anytime that you add a line of code in the `add_coded_line` method, check if adding that line of code puts the `Member` at a new coding level by calling the `get_coding_level` method.  

### Part 3 - Having our `Member` and `OurClass` classes interact

For this part, we're going to assume that the `members` attribute that you create in `OurClass` holds a bunch of instantiated `Member` objects (remember we just instantiated it as an empty list earlier).

1. Now, let's have the two classes we have built interact with each other. The first thing you'll do is write a method in `OurClass` that takes each of the members in the `members` attribute and calculates the total number of questions asked across all members. Call this method `get_num_questions_asked`. You can simply have the total number of questions asked across the class be returned from this method, rather than assigned as an attribute on the class.
2. Next, let's do the same, but this time calculate the total number of lines of code that have been written by all our members. Let's put this in a method called `get_num_lines_code`.

### Part 4 - Test it all out

Now, play with the code that you wrote! Build a list of `Member` objects, and then build an `OurClass` object that takes in those members. Test out and play around with all of the methods that you have built on both classes. Make sure that they work, and that you have a good grasp on how these classes are interacting with each other.

# Extra Credit

1. Create a new class, called `Instructor`, that has two attributes - `name` and `questions_answered`. Here, `name` is an argument that users of the class have to pass in when instantiating it, and `questions_answered` is initialized as an empty list.  
2. Create a method on the `Instructor` class, called `add_question_answered`, that takes in a string (a `question` parameter), and adds it to the `questions_answered` attribute.
3. Now, on the `OurClass` class, build a method that calculates the total number of questions answered across all the instructors. This will involve a few things:

    * Adding an `instructors` attribute (here it'll be a list) to the `__init__` method.
    * Building a method, which we'll call `get_num_questions_answered`, that cycles over the instructors list (which we'll assume is full of a bunch of `Instructor` objects), and calculates the total number of questions answered across all instructors.  

4. Now, write a method that checks whether there are any outstanding questions not answered (**Hint**: Use the results from the `get_num_questions_asked` and `get_num_questions_answered` methods that you have already written).
