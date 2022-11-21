# Functions

### Motivation

Today we are going to learn about functions. In computer science terms, functions are known as subroutines. A **subroutine** is defined as a sequence of instructions that perform a specific task, packaged together as a unit - i.e. a small independent piece of code. Before we talk about how to define and use functions, it's important to know why we want to use them.

Our first reason for using functions is *reusability*. It stems from a methodology  called **Don't Repeat Yourself** (**DRY** for short). This methodology boils down to the idea that we want to be as concise as possible when writing code - we don't want to write unnecessary instructions, and want to avoid repeating the same or similar instructions over and over. Functions allow us to achieve this goal by giving us a tool that we can use to wrap up a set of instructions into a single independent unit. That independent unit can then be used to perform a specific task over and over, without needing to rewrite those instructions. They are written just once, in the function.

The second reason we want to use functions is *abstraction*. Consider the `type()` function that we have used. To use it we needed to know:

1. What the function is - i.e. its name
2. What the function expects passed to it - i.e. the arguments
3. What the function does
4. What the function gives back to us - i.e. returns

That's all we knew about `type()`, and we used it without any issues. The key takeaway here is that we don't need to know anything about how `type()` does what it says it's supposed to do! This is the idea of abstraction - the implementation within a function is hidden from the caller (abstracted away, if you will). There are a number of reasons why this trait is desirable.

First, it allows callers of the function to not be concerned with how the function itself works. Rather, they stay safe in the assumption that the function will work (know, though, that this assumption does not always prove true, in which case you'll have to do some of your own trouble shooting). This allows functionality to be easily shared, and makes it easier to build more complex things. By using functions that other people have built, you're able to stand on their shoulders and build more complex programs.

Second, since the implementation is hidden from the caller, that actual implementation can change (so long as those four things listed above stay the same) and the caller won't know the difference. This makes it easy to split up problems into smaller pieces, and when something in one of those pieces needs to change, it won't affect the rest of the pieces.

### Intro to Functions

#### Built-in Functions  

In our programming journey so far, we've actually seen a number of functions. We've worked with the `len()` function, which returns the length of an inputted iterable. We've also worked with the `range()` function, which returns a generator of numbers from an inputted minimum number to an inputted maximum number. There are many built-in functions that are available in Python, and you can find them [here](https://docs.python.org/3/library/functions.html). Each one of these functions is constructed in a very similar way, and they all take some arbitrary number of arguments. What if we want to have functions that perform tasks other than those available to us in the built-ins, though? Tonight, we'll learn how to define our own functions in such a way that we can use them as we have been using the built-ins!

#### Function Definitions: Part 1

The first thing we're going to figure out how to do is actually define functions. To build up to this, let's take a look back at some code we previously wrote to output a list of all of the even elements in `some_collection`.

```python
evens = []
for element in some_collection:
    if element % 2 == 0:
        evens.append(element)
```

Now, let's imagine that `some_collection` is actually just a list of numbers from 0 to 9 (i.e. `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`). Remember, we can use the `range()` function to create this list. To get a list of all the even numbers from 0 to 9, then, we can modify our code as follows.

```python
evens = []
for element in range(10):
    if element % 2 == 0:
        evens.append(element)
```

**Note**: Remember that a `range(n)` call gives us a list from 0 up to but not including `n`, which is why we use `range(10)` above to get our list from 0 to 9.

What if we wanted to put this code into a function, so that we could then get a list of evens from 0 to 9 anytime we wanted without having to write the above 4 lines of code every time? This is a simple but straightforward example of reusability.

While not every function definition in Python will look the same (they'll have different names, different arguments passed to them, etc.), there is a general syntax that every function definition will follow. This syntax will look somewhat similar to the `while` and `for` loops in the sense that we will start off with some line (this line will define the function), followed by an indented block of code. That indented block of code will define what the function does. Okay, awesome! What goes on that first line, though?

The first line will always start off with a `def` statement followed by a space. What follows will then be the function name, a set of parentheses (without or without function parameters in them), and finally a colon. Let's see what this looks like.

```python
def my_func():
    pass # This pass just acts as a filler right now.
```
Let's dive a little more into each of the parts and note what's important about them. First off, the `def` statement. This is what tells Python that a function definition is being declared. This is what makes Python store your function so that it is callable later in your program. Second, the function name. The only real thing to note about this is that function naming conventions follow variable naming conventions (i.e. *snakecase*, where we lowercase our words and separate them by underscores). Next up are the parentheses. These are going to be filled with an optional and arbitrary number of parameters (which will dive into a little later). Finally, the colon, `:`. This is what is going to signal to Python that the function definition is over, and what follows will be the block of code that makes up the body of the function.

Given all this information, how would we build our `evens` code from earlier into a function? All we have to do is simply copy and paste that block of code after our function definition, and indent all the lines by one level. Let's be sure to give it a more descriptive name, though...

```python
In [1]: def get_evens():
   ...:     evens = []
   ...:     for element in range(10):
   ...:         if element % 2 == 0:
   ...:             evens.append(element)
```

Awesome! Now we can use this function anytime. To do so, all we have to do is call it by name, making sure to end with parentheses. **Note**: The parentheses are necessary because calling `get_evens` without the parentheses has Python look for a variable called `get_evens`, not a function.

```python
In [2]: get_evens()
```

Hmmm, we didn't get anything back out, though? Weren't we expecting the list of evens, 0 to 10? Why aren't we getting anything back? It's because we didn't tell it to give us anything back! Remember, we have to be explicit about what we want Python to do when we program. The computer won't know that we want our evens list back unless we tell it to give it back.

How do we do this, then? Python offers a special keyword, `return`, that we use to specifically return something back from a function. (**Note**: This `return` keyword is specific to functions, and Python will throw an error if you try to use it outside of a function.) With this in mind, let's fix up our function to actually return our list of evens.

```python
In [1]: def get_evens():
   ...:     evens = []
   ...:     for element in range(10):
   ...:         if element % 2 == 0:
   ...:             evens.append(element)
   ...:     return evens
```

Now, when we call this function, it will actually give us back that list of evens...

```python
In [2]: get_evens()
Out[2]: [0, 2, 4, 6, 8]
```

Let's take a little bit more time to discuss the `return` statement. It's nice that it allows us to get back something from a function, but we do have to be careful with it, and make sure that we are using it in the way that we want. `return` is similar to the `break` statement that we learned about in Week 1. As soon as our function sees the `return` statement during execution, it will immediately exit from the function. Let's alter the `return` statement in our `get_evens()` function to see how this works.

```python
In [1]: def get_evens():
   ...:     evens = []
   ...:     for element in range(10):
   ...:         if element % 2 == 0:
   ...:             evens.append(element)
   ...:             return evens

In [2]: get_evens()
Out[2]: [0]
```

So we moved the `return` statement into the `if` block of our function. Now, when we call `get_evens()`, we get a different result. This is because the function immediately gives back our `evens` list as soon as it encounters that `return evens` statement. When we called `get_evens()` above, it encountered that `return` statement in our first iteration through our `for` loop, when `element` was equal to `0`. As a result, `0` got appended to the `evens` list, and then in the next line that `evens` list got returned from the function.

Note that this isn't necessarily a bad thing. Sometimes we want a function to return something as soon as a condition is met. In this case, we'll want to use the `return` in a similar fashion as shown above. Thus, it's good to know about this quality of the `return`.

#### Function Definitions: Part 2

Up to this point, we have just worked with functions that return the same output every time. What if we want a function to act in different ways depending on some input? As we've hinted at, functions can be defined so that their behavior changes depending on what values are **passed** to them. You can pass any data structure(s) to a function, so long as it expects the right number of them. Values that are passed to a function are called **arguments**.

How does a function "expect" arguments to be passed to it? In the parentheses of a function definition, we put the names of the variables that we expect a user of our function to pass to it. We call these special variables **parameters**. This is where functions get their flexibility. When you define a function with a certain number of parameters, you can then refer to those parameters within the body of the function. Since those parameters are set when a user passes arguments to the function, they are actually controlling what happens inside the function!

Let's look at how we can make a function flexible by changing the `get_evens()` function that we defined above. Instead of creating a list of evens from 0 to 10 every time, let's have `get_evens()` build an arbitrarily sized list of evens, from 0 to a number the user passes in. Using our current `get_evens()` as a base, we'll begin by adding in a parameter to the function definition. This parameter will control the size of the evens list that our function builds.

```python
In [1]: def get_evens(n):
   ...:     evens = []
   ...:     for element in range(n):
   ...:         if element % 2 == 0:
   ...:             evens.append(element)
   ...:     return evens
```

With this implementation of our function, we can now pass in an arbitrary number to our function call, and then we will search for evens in a `range()` built with that arbitrary number. How exactly does this work, though? We've told Python that our function should expect one and only one argument. When we call the function and pass in that argument, it will get assigned to whatever name we have given in the function definition - `n` in this case. Then, anytime we reference that parameter, `n`, within the function, it will be the value that was passed to the function. Let's check out a couple of different calls to this function and see what they return.

```python
In [1]: def get_evens(n):
   ...:     evens = []
   ...:     for element in range(n):
   ...:         if element % 2 == 0:
   ...:             evens.append(element)
   ...:     return evens

In [2]: get_evens(5)
Out[2]: [0, 2, 4]

In [3]: get_evens(14)
Out[3]: [0, 2, 4, 6, 8, 10, 12]

In [4]: get_evens(20)
Out[4]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Neat, huh!? Turns out we're just getting started...

In addition to defining our function with the ability to have arguments passed in, we can also build it so that our parameter gets a value **by default** if the function is called without an argument passed in. This is useful if we want to build our function to have some default behavior, but still allow users to pass in arguments that change the default behavior or build off of it somehow. How do we specify a default parameter value for a function? It's actually pretty simple. In the function definition itself, we just place an equals sign (`=`)  after the parameter name, and then the default value that we want to specify (**Note**: Python formatting convention dictates that there should be no spaces surrounding equals signs used in this way).

```python
In [1]: def get_evens(n=5):
   ...:     evens = []
   ...:     for element in range(n):
   ...:         if element % 2 == 0:
   ...:             evens.append(element)
   ...:     return evens

In [2]: get_evens()
Out[2]: [0, 2, 4]

In [3]: get_evens(5)
Out[3]: [0, 2, 4]

In [4]: get_evens(14)
Out[4]: [0, 2, 4, 6, 8, 10, 12]

In [5]: get_evens(20)
Out[5]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Here, we've specified the default value for `n` to be 5. That is, if no value is passed in for `n`, it gets assigned the value of 5 by default. You'll notice in the first function call to `get_evens()` where we pass no arguments, we get the same output as if we pass in the value 5 (which makes sense, since we set 5 as the default). Meanwhile, when we pass in other values, we get the same results as we saw when no default value was set. This is the point of setting a default parameter value - if the caller of the function specifies a value for that parameter, then that is the value used in the function; otherwise, the specified default value is used.

Okay, so those are the basics! We can also define our functions with multiple parameters, and then pass in multiple arguments for those parameters when calling the function. Similar to specifying a default value for a single parameter, we can specify default values for multiple parameters. Let's first modify our function so that we by default return a list of evens from the user inputted range, defined by `n`, but also give the user the option to input a different divisor (instead of 2 for the evens) that will then return numbers in the inputted range that are divisible by the inputted divisor (i.e. the multiples of that number). We'll also change our function name and the name of the returned list (`evens`) so that they become more descriptive (our function is no longer outputting just evens).  

```python
In [1]: def get_multiples(n=5, divisor=2):
   ...:     multiples_lst = []
   ...:     for element in range(n):
   ...:         if element % divisor == 0:
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst

In [2]: get_multiples()
Out[2]: [0, 2, 4]

In [3]: get_multiples(5)
Out[3]: [0, 2, 4]

In [4]: get_multiples(5, 2)
Out[4]: [0, 2, 4]

In [5]: get_multiples(10, 2)
Out[5]: [0, 2, 4, 6, 8]

In [6]: get_multiples(10, 3)
Out[6]: [0, 3, 6, 9]

In [7]: get_multiples(100, 10)
Out[7]: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

As you can see from the first three examples above, the output of our function looks the same as `get_evens()` - by default we still output a list of the even numbers up to 5, and when we pass in 5 as the value of `n` and 2 as the value of `divisor`, we also output a list of the evens up to 5. The other function calls also give us access to the new, generalized version of `get_evens()`, just as we wanted.

Let's take a quick look at a syntactic "rule" that we have to follow when we define functions with default values. When we do this, we have to make sure that any parameters we are giving default values are **after** any parameters that we are not giving default values. Let's check out some examples...

```python
In [1]: def get_multiples(n, divisor=2):
   ...:     multiples_lst = []
   ...:     for element in range(n):
   ...:         if element % divisor == 0:
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst

In [2]: def get_multiples(n=5, divisor):
   ...:     multiples_lst = []
   ...:     for element in range(n):
   ...:         if element % divisor == 0:
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst
  File "<ipython-input-2-fa1c095e8bea>", line 1
    def get_multiple(n=5, divisor):
SyntaxError: non-default argument follows default argument
```
The above code demonstrates this "rule". In the first case, we defined our parameters that have default values (which is only one, `divisor`) after defining our parameters that don't have default values (which is only one, `n`). In this case, everything worked fine! In the second case, we defined a parameter with a default value before a parameter without a default value. That's a no no, and Python let us know!

#### Parameters vs Arguments

As a quick reminder, it may seem like the terms "parameter" and "argument" are being used seemingly interchangeably. These two terms have specific and distinct definitions. A **parameter** is the name of a variable given in a function definition. An **argument** is the value that is passed to a function when it is called.

#### Calling Functions with Positional Versus Keyword Arguments

So far, when we call a function and pass arguments to it we have seen Python assign those arguments to the correct parameters (for example, 5 to `n` and 2 to `divisor`, above). But how exactly does this happen - how does Python know that when we call `get_multiples(5, 2)`, 5 should get assigned to `n` and 2 should get assigned to `divisor`?

It turns out that, by default, Python simply matches up the position of the arguments that are passed in with the position of the parameters that are given in the function definition. In our `get_multiples(5, 2)` call, it takes the first argument passed, `5`, and assigns that to the first parameter in the function definition, `n`. Similarly, it takes the second argument passed, `2`, and assigns it to the second parameter in the function definition, `divisor`. This method of passing arguments is **by position**, and the arguments `5` and `2` in this example are considered to be **positional arguments**.

As you might have guessed from the title of this section, there is another method of passing arguments, and that is **by keyword**. The way this works is that instead of passing just the values in the function call, we call the values with the parameter name that they correspond to followed by an equals sign. Building off of our example above, using **keyword arguments** would mean our function call would look like this: `get_multiples(n=5, divisor=2)`.

Okay, got it! But, there are one or two more things that we need to cover with regards to this topic. In the above examples, we used either **all** positional arguments or **all** keyword arguments. However, there is the possibility that we can use a mixture of positional and keyword arguments if we'd like. The only caveat is that we have to pass all positional arguments **before** passing any keyword arguments. For example:

```python
In [1]: def get_multiples(n=5, divisor=2):
   ...:     multiples_lst = []
   ...:     for element in range(n):
   ...:         if element % divisor == 0:
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst

In [2]: get_multiples(5, 2) # All arguments passed by position.
Out[2]: [0, 2, 4]

In [3]: get_multiples(n=5, divisor=2) # All arguments passed by keyword.
Out[3]: [0, 2, 4]

In [4]: get_multiples(10, divisor=3) # Okay mix of positional and keyword arguments.
Out[4]: [0, 3, 6, 9]

In [5]: get_multiples(n=10, 3) # Not okay mix of positional and keyword arguments.
File "<ipython-input-15-e4167d3728c9>", line 1
    get_multiples(n=10, 3)
SyntaxError: non-keyword arg after keyword arg
```

### Variable Scope

Variable scope is a topic in and of itself, but up until now we haven't really had a good reason to discuss it. **Variable scope** is going to define the part (or block) of your program in which a variable is visible. We typically refer to one of two scopes for variables - **global** scope and **local** scope. A variable with **global** scope is visible everywhere. It can be used anywhere in your script, including any of the functions you have written (it can even be used inside of a function written inside of a function). A variable with **local** scope, on the other hand, is only visible in the scope in which it is enclosed (typically a function).

When referencing a variable, Python will search the following scopes (in order) to resolve the reference:

1. The current function's scope.
2. Any enclosing scopes (like other containing functions).
3. The scope of the module (i.e. script) that contains the code (often referred to as the **global** scope).
4. The built-in scope (contains the built-in functions).

This is kind of a confusing concept to grasp, so let's look at a concrete example.

```python
In [1]: my_global_var = 5

In [2]: def my_test_func():
   ...:     print("My global variable:",  my_global_var) # Accessible and will print.
   ...:     my_local_var = 10 # Only accessible in my_test_func.
   ...:     print("My local variable:", my_local_var)  
   ...:

In [3]: my_global_var # Remember it's accessible anywhere.
Out[3]: 5

In [4]: my_test_func()
My global variable: 5
My local variable: 10

In [5]: print(my_local_var)
NameError                                 Traceback (most recent call last)
<ipython-input-4-b0b2b2a41781> in <module>()
    > 1 print(my_local_var)

NameError: name 'my_local_var' is not defined
```

Notice that `my_global_var` is accessible anywhere - both inside and outside of our function. This is because it is in the **global scope**. `my_local_var`, on the other hand, was defined within `my_test_func`. As a result, it is enclosed within the scope of `my_test_func`, and not accessible outside of it.   

### List and Dictionary Comprehensions

The last topic we'll cover today is a different way to construct lists and dictionaries. Up to now, every time that we have built up a list or dictionary, we began by initializing it. We then took advantage of their mutability inherent to build them up one element or key-value pair at a time. However, there is a more succinct way to accomplish the vast majority of your list and dictionary construction tasks.

#### List Comprehensions

Before we dive into the specifics about how this new tool (list comprehensions) works, let's look at an example question where we build a list.  We can then show how to perform the same task with our new tool and learn how it works.

Let's imagine that we have the list `[1, 5, 9, 33]` stored in the variable `my_list`. Now, let's assume that we want to make a new list of the squares of all the values in `my_list` and call it `my_squares`. With the tools we have covered so far, you might write:

```python
my_squares = []
for num in my_list:
    my_squares.append(num ** 2)
```

Now, `my_squares` will hold the list `[1, 25, 81, 1089]`. To get this, we were simply specifying a bunch of stuff that we wanted to add on to the end of the `my_squares` list, with a starting point at `my_list`. So, from a high level, we can write the framework of creating a list in code as:

```python
list_were_building = []
for thing in iterable:
    list_were_building.append(transform(thing))
```

With this structure in mind, we can use the following syntax to perform the same task of building up a list in a single line! Check it out, along with how it would look for the construction of `my_squares`.

```python
list_were_building = [transform(thing) for thing in iterable]
```

This last line of code does the exact same thing as the three lines above! In this line, the thing that we would pass to the `append()` method, `transform(thing)`, comes at the beginning of the statement in the `[]`.  These `[]` allow for the final product to be defined as a list. Then, the `for` loop statement that we had written is at the end. This is the basic idea behind the [list comprehension](https://en.wikipedia.org/wiki/List_comprehension).

Similarly, we can build our `my_squares` list using a list comprehension:

```python
my_squares = [num ** 2 for num in my_list]
```

But wait! There's more! Remember in all the examples where we were getting evens, we had a condition to decide when to append a value to a list? We can also use conditions to determine what "transformed things" get added in a list comprehension! Let's look at the evens list builder to hammer this home.

```python
# Old way of constructing list of evens
evens = []
for num in range(10):
    if num % 2 == 0:
        evens.append(num)

# Old way at high level
list_were_building = []
for thing in iterable:
    if condition:
        list_were_building.append(transform(thing))

# List comprehension way of constructing list of evens
evens = [num for num in range(10) if num % 2 == 0]

# List comprehension way at high level
list_were_building = [transform(thing) for thing in iterable if condition]
```
The way `transform()` was called in the above examples, as though it were a function, is an option when writing list comps. For example, the `my_squares` example could be accomplished in the same way with:

```python
def square(num):
    return num ** 2

my_squares = [square(num) for num in my_list]
```

This might seem silly, since we could just write `num ** 2` directly in the list comp as we did above. However, this calling of a function in the list comp becomes a powerful idea when you want to transform the values being iterated over in a complex way.

#### Dictionary Comprehensions

Just as list comprehensions are a more succinct way of constructing a list, we have the same ability for dictionaries. Dictionary comprehensions operate in the same way as their list counterparts, except for one fundamental difference. Recall that dictionaries have no `append()` method, and that a new key-value pair is added to the dictionary with the syntax: `my_dict[new_key] = new_value`. In this way, it makes sense that we need syntax to pass both the key and value to the dictionary comprehension.

Luckily, Python gives a simple way to pass a key and value pair, and it is already very familiar to you! You just separate the key and value that you want to enter into the dictionary with a colon, like we did when we were hardcoding the contents in the `{}` dictionary constructor, i.e. `my_dict = {1: 1, 2: 4}`. Let's look at an example where we make a dictionary with the keys as the numbers 1 - 5, and the values as the squares of the keys. We'll do this with both the old way of constructing a dictionary, and then with a dictionary comprehension so that we can see the similarities.

```python
In [1]: squares_dict = {}

In [2]: for num in range(1, 6):
   ...:     squares_dict[num] = num ** 2
   ...:

In [3]: squares_dict
Out[3]: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

In [4]: squares_dict = {num: num ** 2 for num in range(1, 6)}

In [4]: squares_dict
Out[4]: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

We can see that in both cases, we're going through the numbers 1 - 5 with `range(1, 6)` and those `num`s are being assigned as keys. The values assigned to those keys are the squares of the keys, assigned with `squares_dict[num] = num ** 2` and `num: num ** 2`, respectively. Just as with list comprehensions, dictionary comprehensions read as the first thing being the `key: value` pair being added to the dictionary. Then, left to right (top down in the old way), we have what the loop definition would look like. And, just as with list comps, we can add a condition to filter what gets put into the dictionary.

Say that we want a dictionary with a random integer between 1 and 10, associated with each of the values in the list of words: `['cow', 'chicken', 'horse', 'moose']`. Let's look at how we'd do that with a dictionary comprehension. (We're importing from the Python library `random` to get our random integers. We'll talk more about importing later in the course.)

```python
In [1]: from random import randint

In [2]: animals_list = ['cow', 'chicken', 'horse', 'moose']

In [3]: animals_dict = {animal: randint(1, 10) for animal in animals_list}

In [4]: animals_dict
Out[4]: {'chicken': 2, 'cow': 10, 'horse': 9, 'moose': 8}
```

#### Other Comprehensions

You can actually use the syntax from the list comprehensions to construct a tuple in what seems like a dynamic way. Take the example.

```python
In [1]: my_tuple = tuple(num for num in range(10) if num % 2 == 0)

In [2]: my_tuple
Out[2]: (0, 2, 4, 6, 8)
```

All we are doing here is passing `num for num in range(10) if num % 2 == 0` to the tuple constructor, `()`. Since the tuple constructor takes any iterable, which that statement produces, it makes a tuple out of the contents. Note that it would be impossible to make a tuple with statements like this the "old way", since tuples don't support appending or mutation of any kind!

For this reason, in addition to their readability, comprehensions of all types are considered the most Pythonic way of constructing new data structures.
