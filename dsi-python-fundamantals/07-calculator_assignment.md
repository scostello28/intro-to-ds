## Reverse Polish Notation Calculator

Your assignment today is to implement a program that functions as a calculator. This won't be just any calculator, though, but a Reverse Polish notation calculator. There's a good chance you've never heard of this particular flavor of calculator, so here's a quick overview.

### Reverse Polish Notation

Many of us are solely used to entering computations into a calculator by putting an operation between two values. For example:

| value | operation | value |
|:-----:|:---------:|:-----:|
|   3   |     +     |   4   |

However, there are other notations that can be used to express mathematical operations. Two of these are *prefix* and *postfix*. *Prefix* notation is sometimes known as *Polish Notation* (for the Polish logician Jan Łukasiewicz who invented it), and so *postfix* notation is also known as *Reverse Polish* notation. Today we will be building a calculator that implements Reverse Polish Notation ([RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)). For example, instead of writing `3 + 4` as we did above, we would write `3 4 +`, like this:

| value | value | operation |
|:-----:|:-----:|:---------:|
|   3   |   4   |     +     |

This method of inputting computations actually makes it easier to write logic to perform the operations (for the computer, anyway). This is because the format lends itself to storing computations in a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). A stack is a specific type of sequence (know as last in, first out, or *LIFO*)  which only supports two types of operations - pushing and popping.

You can think of a stack as a `list` with less functionality. (**Note**: you could use a [deque](https://docs.python.org/3/library/collections.html#collections.deque) class instead, though it will only add a bit of additional functionality). What an RPN calculator does is accept input one element at a time and push it onto the stack in turn. In Python `list` lingo, pushing to the stack just means appending them to a `list`. When the user wants to perform an operation, the values necessary to perform the operation are [popped](https://docs.python.org/3/tutorial/datastructures.html) off the stack, in turn. The value resulting from that operation is then pushed back onto the stack.

### RPN Example

Say we want to calculate the value resulting from the calculation: `6 + ((5 + 3) / 4) - 3`. In RPN, that calculation is written: `6 5 3 + 4 / + 3 −`. To input this calculation into a RPN calculator, one would enter those elements (in turn), and the corresponding operations would occur in the following order.

| Input |  Operation   |    Stack    |                   Other                        |
|:-----:|:------------:| ----------- |:----------------------------------------------:|
|   6   |  Push Value  | [ 6 ]       |                                                |
|   5   |  Push Value  | [ 6, 5 ]    |                                                |
|   3   |  Push Value  | [ 6, 5, 3 ] |                                                |
|   +   |     Add      | [ 6, 8 ]    | Pop two values (3 then 5), push result (5 + 3) |
|   4   |  Push Value  | [ 6, 8, 4 ] |                                                |
|   /   |    Divide    | [ 6, 2 ]    | Pop two values (4 then 8), push result (8 / 4) |
|   +   |     Add      | [ 8 ]       | Pop two values (2 then 6), push result (6 + 2) |
|   3   |  Push Value  | [ 8, 3 ]    |                                                |
|   -   |   Subtract   | [ 5 ]       | Pop two values (3 then 8), push result (8 - 3) |

If you want to play around with an RPN calculator to get a feel for them and how they operate, check out [this](http://www.meta-calculator.com/learning-lab/reverse-polish-notation-calculator.php) link.

### RPN Calculator

Your assignment is to implement a calculator that operates with Reverse Polish notation. While this is supposed to be an OOP lab, this problem can be done solely with functions. So while you can start off by writing functions that solve the problem, you are encouraged to begin with an OOP approach.

The following steps are suggestions, and while they could possibly make your journey through this programming assignment easier, they do not need to be followed. Remember, there are always multiple ways to solve programming problems. Sometimes there's an obvious solution, and sometimes not so much. Sometimes there's a more elegant solution, and sometimes they all function about the same. At a high level, the purpose of this lab is to have you work through a problem from start to finish so that you can get a good feel for what that process is like. In addition, the instructor will be around if you have any questions or concerns about how you are wanting to implement your solution.

Rather than reading the assignment straight through and then starting to code, follow the directions as you read them. Thinking about the best approach before reading our suggestions will help you learn how to solve a programming problem. Talk about the problem with your classmates and/or the instructor at any time; frequently, one of the biggest hurdles when trying to solve a problem is trying to figure out what the problem actually is. Trying to explain it to someone, and having a conversation about it, can go a long way towards understanding the problem.

#### Step 1: Interact with the Problem at a High Level

Take a look at wikipedia's description of the [algorithm](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_algorithm) for evaluating a string of operations in RPN. This is a great outline of what your program will need to be able to do. Follow along with the example, making sure you understand how the algorithm is evaluating the sequence and what the state of the stack is at each step.

#### Step 2: Think about the Interface.

The first part in any programming problem is understanding the interface. If you're writing a function, you need to know the inputs and outputs - the parameters and return values. If it interacts with a user, you should think about how that should work.

There are many ways you could do this. At this point you're playing as the designer (or product manager) so think about what would work for the user. The real requirement is that the user can enter numbers and operators and get results, and it should save the stack so the user can keep working. Beyond that:

* Should the user be able to enter a string of numbers and operators and numbers, or just one at a time?
* If the former, how are they separated? Spaces are easy, but you could allow a string like "3 4+".
* When should the user expect a result? Should it print out the whole stack every time or just the top? Should it evaluate input immediately or only when the user requests it?

If you aren't sure: allow the user to enter a line of space-separated operators and positive integers, evaluate them immediately, print out the resulting stack. For example:

```
Operation(s)/Value(s): 4 5 +
Stack: 9
Operation(s)/Value(s): 2 3 2 *
Stack: 9, 2, 6
Operation(s)/Value(s): + -
Stack: 1
```

#### Step 3: Devise a Plan

You'll be writing a class, so think about how that will look. What data does it hold? What are the most important methods? What other methods will those call? Think about this before reading the next step. Once you have some ideas, move on to the next step which will provide recommendations.


#### Step 3: Build a Class

The first concept of object-oriented is encapsulation, that you have some data that you access through associated functions. In this case, the data is the current state of the calculator, in particular, the stack.

To start your class you want at least two methods: `__init__` and `run`. The first shouldn't do much, just instantiate the data. The second should include a loop that will get user input and print the results.

At this point (if you haven't already) you should write your class in a file with these two methods. Don't include any other code yet, just put `pass` in the functions so you can create an object. Add docstrings to the beginning of each method that describe what each function will do. Test this out with a `if __name__ == '__main__':` block at the end that creates an object of that class and calls the `run` method, and run the program from the terminal. It won't do anything yet, but (once it's working) it shouldn't give you any errors.

If it does give you errors, that's part of the process. It's pretty common for any new code to have bugs, even just a few lines, even written by skilled programmers. The best way to fix them is to run the code early and often, while you still remember what you changed and you haven't added more bugs on top of them.

#### Step 4: Add Stub Methods

Right now the `run` method will do nearly all the work. In line with the top-down tactics that we have previously discussed, consider how this problem can be broken down into smaller pieces that are easier to be solved. What will the big problem be? Consider making a function that will take a string of elements (separated by spaces) and evaluate on the stack. Some questions to ask yourself:

* What would that function look like?
* What would you call it?
* What parts of what it needs to do could be assigned to other functions?
* What would they be called?

Add a few more methods to your code, writing only the `def` statements and docstrings. Spend some time here before moving to the next step.

#### Step 5: Decide on the Data

The calculator needs to know about its current state, based on what has already been entered. You probably want it to just store the current stack. You could use a list for this, or some fancier class such as `deque` (in the collections module). Create this in the `__init__` method.

#### Step 6: Add More Methods

In addition to `run` and `__init__`, some other methods you might have are:

* A method that takes a string of space-separated symbols and evaluates it,
* A method that takes a single symbol and evaluates it,
* A method that pushes the a number onto the stack,
* A method that pops the number on the top of the stack, and returns it, and
* A method that takes handles an binary operator, taking a single function as input (using the above two functions) updates the stack.

That last one is definitely optional; it will make the code shorter but is tricky to implement. The operators aren't functions themselves, but there are functions for each one in the `operator` library. If you do use it, you might make a method to handle unary operators (e.g., sqrt) as well.

For each method you want, write the `def` statement and the docstring, and a `pass` for the body of the method. Once that's done make sure your program still run. Again, it won't do anything but it shouldn't give an error; if it does, fix it.

#### Step 7: Pseudocode

Now that you've moved from the outline of the algorithm to thinking about how you will task out parts of it to functions, you are in a great position to begin pseudocoding. Pseudocode can take on a variety of different appearances. It can be simple notes to yourself about steps you want to take. It can be instructions that are semi-code like (e.g. if you're going to loop over some container you might write a line of pseudocode that looks like `for thing in stuff`, giving better names to each `thing` and the `stuff`). It can be almost functioning code. In general, it's good to keep it in comments so your program will still run.

The nice thing about pseudocode in Python is that you can often write it in nearly accurate Python syntax. While variables you want to reference or functions you want to call might not exist yet, this isn't a problem because its just pseudocode! Then, when you want to go fill in the pseudocode and make it "real" code, you already have some lines that will work in Python. In addition, you should have great names for everything you'll need to name. For example, if I'm trying to solve a problem that needs to load a list of words, and then loop through that list and make a dictionary with the number of words of different counts, my pseudocode might look like the following:

```python
def get_word_count_dict():
    word_list = load_word_list()
    count_dict = make_count_dict()
    return count_dict


def load_word_list():
    with open get file(s):
        load words from files to list
    return word_list


def make_count_dict():
    for word in word_list:
        build up dictionary
    return dictionary
```

Now that this skeleton exists, it's easier to see what types of parameters each function will take, and think about how the whole program will flow. You might notice that both `load_word_list()` and `make_count_dict()` will need to accept parameters. Now that we've written this pseudocode, though, that's way easier to see than when you first thought about how to solve the problem.


#### Step 8: Implement Real Code

At this point you should have a decent, nearly code-like structure for your program to create a class to calculate an RPN operation. Now you can go through and make the pseudocode working code by filling it in. Along the way, you'll start seeing places where you can make functions out of certain routines that do their own thing and/or are run in a loop, and that's great! You're well on your way to a working program.

#### Step 9: Debug

As you fill in code, continue running your program and fixing errors. Start at the top-level functions so you can run the program, even if it does almost nothing at all (e.g., asked for input repeatedly and ignore what the user types).  As you fill in the methods it will do more and more. Start with partial functionality, say, just pushing numbers onto the stack, and then adding numbers.

You will always make errors as you code; don't let this frustrate you. Every programmer has to debug; embrace this and learn from your mistakes.

There are many methods by which you can debug. You can read through your code for syntax/logic errors, or you can print things out to make it easier to follow the flow of your program as it actually runs. You can also use the Python Debugger, or [pdb](https://docs.python.org/3/library/pdb.html) for short. This tool can be really helpful if you want to interact with your program similarly to the way you interact with IPython. `pdb` allows you to pause the Python interpreter while it is running your script. This gives you the opportunity to poke around and check the state of your program, the variables that exist, what their values are, etc, at any step. You can use `pdb` at any point in your programs execution (you just have to use it the right way). Check out this [blog post](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/) for a great introduction on using this tool.

#### Step 10: Check the Input

Try to break your program by entering calculations that make no sense. Can you make your program robust to these poorly/incorrectly formatted inputs? It's good to think about these things, though frequently it's very difficult to foresee all the possibilities of bad input. Ideally, the program should respond gracefully no matter what the user does.


#### Step 11: Add More Features

If you have this all working add more features to your calculator. Perhaps you might add more unary functions like `sin` and `cos` or a command to switch the top two elements on the stack.

#### Step 12: Refactor Your Code

At this point your program might be hard to understand. If you didn't add that last method in step 6 using the `operator` module, that might simplify your code. Break your methods into smaller methods. Give your variables better names. Add docstrings. As you do this, continue to run and test the program to make sure you don't break anything. Refactoring (generally in the presence of tests) is a big part of making maintainable code.


