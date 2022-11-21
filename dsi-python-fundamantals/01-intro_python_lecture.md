# Introduction to Python

### Numeric Variable Types
Today we are going to learn about base numeric variable types in Python, and learn how to write scripts (programs) that can compute useful things.

There are a number of base numeric variable types built into Python. The ones that we will be looking at today are `ints` (short for integers), `floats` (short for floating point decimal numbers), and `complex`, which contain real and imaginary parts stored as floats.

Let's experiment with using these types in the IPython console. Type the number 7 and hit enter. You should see something like this.

```python
In [1]: 7
Out[1]: 7
```

The IPython console will accept arbitrary Python commands, entered after the `In [#]:`, and execute them, handing you back the results of the computation, displayed after the `Out[#]:`.

You can test this out with other numbers. Try one with a decimal and another by passing two numbers to the `complex()` constructor (we will talk about what these things are later).

```python
In [1]: 7.5
Out[1]: 7.5

In [2]: complex(3, 4)
Out[2]: (3+4j)
```

One thing that is important to note about Python is that it is a duck typed language. What does this mean? The name duck comes from the classic "If it walks like a duck, and quacks like a duck, then it must be a duck" adage. As applied to our situation, it simply means that Python will determine what it thinks is the best type to call a variable when you use it, unless explicitly told otherwise.

To inspect what type Python thinks a number (or anything else is), you can pass it to the `type()` function. Let's see what we get out when we pass numbers of various types to this function.

#### Types

```python
In [1]: type(7)
Out[1]: int

In [2]: type(7.5)
Out[2]: float

In [3]: type(complex(3, 4))
Out[3]: complex
```

As you can see, Python assumes that a number with no decimal point is an `int`, those with a decimal point a `float`, and (surprise!) those from the `complex()` constructor as `complex`.

While very frequently these subtle differences won't matter too much, there are plenty of occasions where Python hiding this implementation detail will make you think that something will work, when really it won't. Making sure you know how to check is very important.

### Numeric Operations

At its base level Python is really just an awesome calculator that can do way more stuff than addition and subtraction. But let's focus on that functionality for now.

All of the simple operations that you think should be available are. Addition, subtraction, multiplication, division and exponentiation are all accessible via `+`, `-`, `*`, `/` and `**`, respectively.

```python
In [1]: 7 + 8
Out[1]: 15

In [2]: 7 - 8
Out[2]: -1

In [3]: 7 * 8
Out[3]: 56

In [4]: 7 / 8
Out[4]: 0.875

In [5]: 7 // 8
Out[5]: 0

In [6]: 7 ** 8
Out[6]: 5764801
```

All of these operations output exactly what we think they would, except one. The fifth one, where we divided 7 by 8, gave us 0, even though we know that it should be 0.875. This is because there are two types of division in Python 3: **floor division and floating point division.**

```python
n [1]: 7 // 8
Out[1]: 0

In [2]: 7 / 8.0
Out[2]: 0.875

In [3]: 7 / 8.
Out[3]: 0.875

In [4]: int(7 / 8.)
Out[4]: 0

In [5]: 7 // 8.
Out[5]: 0.0
```

Notice the difference between floor division and floating point division.  Floor division truncates the response, leaving out anything after the decimal point, while floating point division returns what's expected.  Also note that `8.0` and `8.` are both identical numbers of type `float` while `8` is assumed to be of type `int`.

We can manually cast the output of the 4th operation as an `int` by passing the result directly to the `int()` constructor. Manually casting in this way can be very useful when Python is interpreting things differently than you would like it to.

The last operation that we will go over is the modular division operator, `%`. This operation is the sibling to `//`. Where `71 // 7` gives us the integer number of times that 7 goes into 71 (10), `71 % 7` gives us the remainder from that integer division (1).

### Variables

One of the most powerful constructs in programming is the ability to store arbitrary values in what we call variables. You can think of variable assignment as giving a name to something so that it can be accessed later by different parts of your program.

In Python, variable assignment occurs with the `=` operator. So to assign a value to a variable name (i.e. declare it), you simply put the variable name on the left side of the `=` and the value you want to associate with that variable name on the right hand side. Now that this has happened, you can access the value in the variable simply by using it's name somewhere later in your code or IPython session.

```python
In [1]: x = 1

In [2]: x
Out[2]: 1

In [3]: x + 1
Out[3]: 2
```

The name you can give a variable can technically be any contiguous set of characters, but there are some conventions followed in Python and programming in general. Python follows a variable naming convention called snake case. To write something in snake case simply use a `_` anywhere you would use a space and make sure every word is lower case. For example, `this_is_a_variable`. Giving variables good names makes your code more readable and therefore maintainable. There is a big difference between seeing a variable called `degrees` and one called `y`. You should strive to give your variables well-defined, succinct names.

There are of course cases where using less than descriptive variable names follows convention and is, therefore, just fine to use. One that comes to mind is the use of `i` to keep track of an index (we will cover this idea next week, but it wouldn't be surprising if you understood the concept already). Because of its prevalent usage for this purpose, it is usually easy to understand what is happening in that context, and the lack of descriptiveness is okay. The important thing is that the code is **understandable**.

Note that we saw no output from the first command above. This is because the return value that would have been printed to the console for output was assigned to the variable `x`. This is why we had to view it in the next line with a simple call to `x`.

A large part of the power of variables is the fact that they can change. This allows us to use a single variable name to keep track of a single thing throughout the life of a program. The exact same syntax can be used to change the value stored in the variable.

Say we want to add 5 to `x` from the previous code example and store it in `x`.

```python
In [1]: x = x + 5

In [2]: x
Out[2]: 6
```

Notice how the first line is formatted. Python knows that the `=` means variable assignment, so when it sees the first line it evaluates the right side of the equals and then puts that value in `x`, even though `x` is part of the calculation on the right side.

Changing variables in this way occurs so commonly that there is built-in shorthand for it. The result of the first line could have been achieved with `x += 5`. This *syntactic sugar* is available for all the simple operations `+`, `-`, `*`, `/`, `**`, and `%` that we covered earlier.

### Logic

Now that we have a thorough understanding of base numeric types and how to play with them and store them in Python, let's keep building our tools so that we can use them to control the flow of our program.

The most simple way to control the flow of your Python program is with an `if` statement. From a high level, an `if` statement allows us to check whether or not a certain condition is true, and perform operations specific to that situation if the condition is true.

For example, say we're asked to write a program that takes a bunch of numbers and gives back to us those that are even. We would need to write an `if` statement that identifies whether or not a number is even (we'll talk about how to do this), and then give back only those that meet the even condition. This is a program that will be entirely within our ability to implement at the end of next week; for now though, let's focus on the `if` statement.

The general syntax of an `if` statement in Python is:

```python
if condition:
    if_block_statement
```

Notice how the `if` statement ends in a colon `:`. This is the way that Python declares the start of an indentation block. The purposes of indentation blocks manifest themselves in many different ways, but with our `if` statement just know that they mark a section of code that is run under specific circumstances.

#### Conditionals

Let's tackle this one part at a time. What does it mean to be a condition? Really, all an `if` is checking is whether the conditional evaluates to `True` or `False`. If the condition is true, then the body of the `if` statement is executed. If the condition is false, the `if` block is skipped. Intuitively, true and false are concepts that make perfect sense to us. But we should take the time to clearly define them in a programming context here.

`True` and `False` are what we call booleans in logic (`bool` for short), and what Python calls them. They are a special variable type with many potential uses; mainly they are used as a way to put a label on the truth of a statement. There are two specifically reserved words for bools in Python, `True` and `False`. Note that these begin with capital letters.

```python
In [1]: type(True)
Out[1]: bool

In [2]: type(False)
Out[2]: bool
```

In addition, a wide variety of statements can evaluate to booleans. The ones that we will focus on today are the equalities, *equal to* and *not equal to*, and the inequalities, *less than*, *greater than*, *less than or equal to* and *greater than or equal to*. These comparisons are available in Python via `==`, `!=`, `<`, `>`, `<=` and `>=`, respectively.

```python
In [1]: 1 == 2
Out[1]: False

In [2]: 1 != 2
Out[2]: True

In [3]: 1 < 2
Out[3]: True

In [4]: 1 > 2
Out[4]: False

In [5]: 1 <= 2
Out[5]: True

In [6]: 1 >= 2
Out[6]: False
```

#### Using the If

Now that we understand conditionals, let's talk about how we can use them with variables to make our programs dynamic. Consider the following code block.

```python
if x > 5:
    x += 10
print(x)
```

**Note**: The print function simply pipes the value passed to it to the console.

In the above code we don't need to know what the value of `x` is, but we can say that if it's greater than 5, it will come out of the code block 10 greater than before the `if` statement.

From what we know so far, this functionality isn't super useful. So let's quickly go over a way that we can make our Python more flexible. Until now, we've had to hard code any variable or value that we want to use in our program. Python has a built in way to accept input from the user of a program. Let's examine this now. Consider that the following code was stored in a file named `print_number.py`.

```python
x = input('Please enter a number: ')
print(x)
```

If we then ran the script from IPython, we would would see:

```python
In [1]: run print_number.py
Please enter a number:
```

**Note**: The `input()` function accepts character input from the keyboard, printing the message it is passed as a prompt.

We can then type a number followed by enter, and the script will print that number.

```python
In [1]: run print_number.py
Please enter a number: 3
3
```

**Note**: `input()` halts the execution of your script, so nothing will happen until you type something and press enter.

Now that we have a way to get arbitrary input from the user of our program, we can begin to see the full power of the `if`. Let's combine the last two code blocks from above, and say we stored it in a script named `print_number_with_if.py`.

```python
x = int(input('Please enter a number: '))
if x > 5:
    x += 10
print(x)
```

**Note**: `input()` actually interprets the input as strings, so we have to manually tell Python to treat the number we pass as an integer with `int()`. We'll talk about strings more next week.

If we then ran the script from IPython as above, let's look at two ways we could interact with it.

```python
In [1]: run print_number_with_if.py
Please enter a number: 3
3

In [2]: run print_number_with_if.py
Please enter a number: 8
18
```

Notice that the first time we run `print_number_with_if` and give it 3, it acts just like `print_number`. However, the second time, when we give it 8, it adds 10 and prints 18. Why did it do this? Because 8 is greater than 5, so our program added 10 to it before it was printed.

This may seem like a trivial example, and therefore, not very exciting. Let me assure you, though, that what you have just learned is amazingly powerful! So congratulations!

#### Building on the If

Ok, so, the `if` is cool. But it seems like, due to it's structure, there are only so many things you can do with it. Let's summarize this with what's known as a *flow diagram*.

![If Flow](http://www.tutorialspoint.com/cprogramming/images/if_statement.jpg)

You can see that there are two branches created by the `if` statement, one when the condition is true, and the other when it is false. In the former case, the conditional code is executed, and in the latter, the conditional code is ignored. But what if we wanted to check more than one thing (i.e. have more than two branches in our flow diagram)?

Python gives us two ways to do this. One by offering other conditionals, `elif` and `else`, and the other by allowing us to combine conditions with logicals `and`, `or` and `not`.

##### Elif and Else

In addition to the `if`, Python provides us with two other statements to build out those logical trees, the `elif` and the `else`. The `elif` is just like the `if` - it accepts a condition to check the truth of and has an indented code block that is executed when that condition evaluates to `True`. The `else` is similar, but it doesn't accept a condition. Instead, it mainly acts as a catch all for any other situation that you don't need to cover with your `if`s and `elif`s. Note that there can only be a single `if` and up to a single `else`, but any number of `elif`s in an `if`-`elif`-`else` block. Let's take a closer look at this in the following code block that we'll store in `if_elif_else.py`.

```python
x = int(input('Please enter a number: '))
if x < 0:
    print('You entered a negative number.')
elif x > 0:
    print('You entered a positive number.')
else:
    print('You entered the number 0.')
```

Running the program and passing a number when prompted will cause the conditions to be checked and result in the following output.

```python
In [1]: run if_elif_else.py
Please enter a number: 10
You entered a positive number.

In [2]: run if_elif_else.py
Please enter a number: -10
You entered a negative number.

In [3]: run if_elif_else.py
Please enter a number: 0
You entered the number 0.
```

Let's specifically talk about how the `if`-`elif`-`else` statements work. The programmers of Python designed these statements so that they would execute highly efficiently. They achieved this by making it so that when Python is going through your `if`-`elif`-`else` statements and encounters a condition that evaluates to `True`, it will execute the corresponding conditional code block and then skip to the line directly following the last conditional block. Let's examine this in the following code saved again in `if_elif_else.py`.

```python
x = int(input('Please enter a number: '))
if x > 5:
    print('You entered a number bigger than 5.')
elif x > 0:
    print('You entered a positive number.')
elif x < 0:
    print('You entered a negative number.')
else:
    print('You entered the number 0.')
```

Running this program produces slightly unexpected results. But, they will soon make perfect sense, and knowing what is going on will allow you full control over the flow of your programs.

```python
In [1]: run if_elif_else.py
Please enter a number: 5
You entered a positive number.

In [2]: run if_elif_else.py
Please enter a number: 6
You entered a number bigger than 5.
```

In the first example we got something unsurprising. The only condition that evaluates to true when `x` is 5 is the second one. However, the second example yields only 'You entered a number bigger than 5.', even though 6 is greater than 0. This shows that only one of the conditional blocks in an `if`-`elif`-`else` statement will ever be evaluated, and once this happens the rest are skipped.

**Note**: The `else` part of the statement is actually optional. If it is not included, then we'd notice that at most one of the conditional blocks in an `if`-`elif` statement will be evaluated.

##### And, Or and Not

There are plenty of times when we want to execute some specific code when more than one condition is true. Check out the following code snippet.

```python
if x > 5:
    if x < 10:
        print(x)
```

We can see that what this **nested** `if` statement is checking for are numbers that lie in the interval (5, 10), and if it finds one it prints it. We can intuitively guess that there is a better way to check for this condition. And there is!!!

Python gives us full access to what are known as boolean operations. The ones that we will use most often are `and`, `or` and `not`. Both `and` and `or` take two conditions as inputs, while `not` takes only a single condition. They all return a single boolean, with `and` requiring both conditions to be `True` to return `True`, and the `or` requiring only one of the conditions to be `True` to return `True`. The `not` switches the truth of the input condition. These operations are derived from formal logic, and you can find a full discussion of their intricacies found [here](https://en.wikipedia.org/wiki/Truth_table).

What this means is that we now have a natural way to combine conditions. The previously nested `if` statement can now be written as a simple `if x > 5 and x < 10`. We can also chain other interesting conditionals together.

```python
if x > 10 or x < 5:
    print(x)

if not (x <= 10 and x >= 5):
    print(x)
```

Notice how the first `if` in the above code snippet uses an `or`, printing `x` if it is greater than 10 or less than 5. Inherently this statement is also saying that it will print `x` if `x` is not between 5 and 10, which is expressed in the second `if` statement. This illustrates an important point - there is always more than one way to accomplish the same thing in programming.

### Looping

We are now prepared to learn about another extremely powerful programming construct. Everything that we learned in the last section on logic is part of an idea called **control flow**. Flow refers to the order in which statements in your program are executed. Controlling this flow can be done in many ways; so far we have learned about `if`-`elif`-`else` statements, but there are a number of others.

One thing that we find in programming is that we want to do something over and over (and over), possibly under the same circumstances each time, but frequently under slightly different circumstances each time. With the tools that we currently possess, we have to write out a line of Python for each time that we want to do that something. Let's go through a more concrete example.

Consider that you are asked to write a program to calculate the sum of the numbers between 1 and 8 (without the use of any built-in Python functions). We could write an extremely simple program to do this for us.

```python
sum_1_8 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
print(sum_1_8)
```

While this definitely works, there are a couple of things I want to draw your attention to (which will become themes about how to analyze how well code is written). First, what happens if we want to add the numbers 1 through 9 together? Not that hard, just add 9 to `sum_1_8` you say. Ok, fine. What if you want to add 2 through 9 together? Now we could take `sum_1_8`, add 9 and subtract off 1. And that works, but it involves some thinking to make this new idea work with the existing code that we have written.

Instead of having all of these **hard coded** values in our definition of `sum_1_8`, we could instead **abstract** away part of our problem. What is this abstraction? In programming, we talk about abstraction when we want to refer to an idea whose implementation is more general and/or hidden from us. In the above example, we see exactly what we're doing to sum the numbers 1 through 8. This isn't abstracted at all. So how are we to solve this problem more abstractly?

This is a question that you will frequently be faced with; how do you do something... in code? A good strategy to solve these problems is to approach the problem from a high level (i.e. in plain English, no code).

So let's do that with our coding problem above. We were asked to add together the numbers 1 through 8. This can be thought of as given a starting number, 1, and then adding on the next number, 2, to get 3. Then we can repeat this process, taking the next number, 3, and adding it on, giving us 6. We could then continue this process until we reach the final number, 8, and then stop. (This is inherently what we were doing in that single line of Python when we said `1 + 2 + 3 + 4 + 5 + 6 + 7 + 8`, but that implementation is what we call **brittle** - it only works for that specific case and breaks whenever we want to do something even slightly different.)

#### While Loops

Notice how in our high level description of the problem solution, we kept saying "and then". This repetitious language brings us to our next control flow tool, loops. There are two types of loops in Python, but today we're going to focus on `while` loops. `while` loops are an amazing tool which simply allow us to have a predefined chunk of code which we tell Python we want to run over and over under certain conditions.

So what are these conditions? They are in fact the conditions we learned about in the logic section (i.e. any expression that is evaluated to a boolean). So how does this work with `while`? Let's take a look at the structure of a `while` statement.

```python
while condition:
    while_block_statement
```

As with  `if`, a `while` statement has a condition; unlike the `if`, the while block will execute over and over again as long as the condition is `True`. This is where we get the name `while` loop from - as long as the condition evaluates to `True`, we will execute the code inside the `while` block, looping over it. The `while` condition is checked each time before the `while` statement block is executed.


Let's look at how we can harness this new structure to solve our previous problem. Take a look at the following code.

```python
total, x = 0, 1
while x <= 8:
    total += x
    x += 1
print(total)
```

Let's break down this code to see what is going on. On the first line, we declare a couple of variables (here you see the Python syntax used to do multiple assignments in a single line), `total` and `x`. `total` is the variable that we are going to aggregate our sum into, and `x` is the first number that we start our adding at. The next line declares the start of our newly learned `while` block. It's condition is x <= 8, and naturally reads as: "while x is less than or equal to 8", do stuff in the block. The block then says we are to add the current value of `x` to total, then add one to `x`.

We know that this `while` statement will loop through the `while` block many times, but the values of `total` and `x` will change each time through the loop. So, let's take a look at what the values of both of these variables are throughout the execution of the loop.

| After loop #  |   total   |   x   |   x <= 8   |
| ------------- |:---------:|:-----:|:----------:|
| 1             |  1        |   2   |    True    |
| 2             |  3        |   3   |    True    |
| 3             |  6        |   4   |    True    |
| 4             |  10       |   5   |    True    |
| 5             |  15       |   6   |    True    |
| 6             |  21       |   7   |    True    |
| 7             |  28       |   8   |    True    |
| 8             |  36       |   9   |    False   |

We see that as we continue through the loop, `total` is growing by the value of `x` from the previous execution of the loop, and this continues until the condition `x <= 8` evaluates to `False`. This happens when `x` is 9, at which point we exit the loop, and `total` has accrued the sum of the numbers 1 through 8. Magic!!

To solidify this idea in the framework of control flow, take a look at the structure of the `while` loop as a flow diagram.

![While Flow](http://www.programiz.com/sites/tutorial2program/files/C_while_loop.jpg)

We see that the trick to the loop, in terms of control flow, is that we return to check the condition each time after the `while` block is executed to determine if we should execute it again.

#### Infinite Loops

While the power of this looping construct is undeniable, there is one extraordinarily important thing that should be on your mind when you're writing `while` loops.

Notice that our condition in the `while` loop example made sense because we were changing the value of `x` each time through the loop (with the line `x += 1`). What would happen, though, if we didn't do this incrementing (other than not calculating the correct value for `total`)?

Let's take a look at what the loop table would look like in this situation.

| After loop #  |   total   |   x   |   x <= 8   |
| ------------- |:---------:|:-----:|:----------:|
| 1             |  1        |   1   |    True    |
| 2             |  2        |   1   |    True    |
| 3             |  3        |   1   |    True    |
| 4             |  4        |   1   |    True    |
| Etc.          |  Etc.     |  Etc. | **Always** True |

Aside from the obvious problem that we aren't finding the sum of the values 1 through 8, we run into another, very egregious issue. Will the condition `x <= 8` ever evaluate to `False`? No. So will the loop ever finish executing?? It won't!!

We call this idea getting stuck in an **infinite loop**. They are almost *always* bad, and they usually manifest themselves as your program running for way longer than you would expect it to run, at which point you realize that something weird is happening. The common cause of these infinite loops is almost always having a condition that always evaluates to `True`.

#### More Control Flow

##### Continue

So what if we want even more control over how the body of our loop is executed? Let's motivate this idea with a problem. Say we want to add all the numbers from 1 to 8... but not 5. Again, we could solve this with our current solution, and then subtract off 5. But, again, that takes a lot of manipulation. Instead, we can use the main structure of our current loop and add in a new condition with an `if` and use a new tool to interrupt our program's flow.

Enter `continue`. What `continue` does is simply tell Python that it should skip the rest of the body of the `while` block, and jump (`continue`) to the next iteration of the loop. Let's take a look at `continue` in action.

```python
total, x = 0, 1
while x <= 8:
    if x == 5:
        x += 1
        continue
    total += x
    x += 1
    print(total, x)
print(total)
```

In this updated program we can see that we will, at each iteration of the loop, check to see if the current value that we're about to add on to `total` is 5. If it isn't, we go on with our aggregation of `total`. If `x` is 5, we add one to `x` (do you see why we need to do this?), and skip adding `x` to total by executing a `continue`, jumping immediately to the next iteration of the loop. Let's see how this would look in the loop table.

| After loop #  |   total   |   x   |   x <= 8   |    x == 5   |
| ------------- |:---------:|:-----:|:----------:|:-----------:|
| 1             |  1        |   2   |    True    |    False    |
| 2             |  3        |   3   |    True    |    False    |
| 3             |  6        |   4   |    True    |    False    |
| 4             |  10       |   5   |    True    |    True     |
| 5             |  10       |   6   |    True    |    False    |
| 6             |  16       |   7   |    True    |    False    |
| 7             |  23       |   8   |    True    |    False    |
| 8             |  31       |   9   |    False   |    False    |

During the fourth iteration of the loop, when `x` is 5, we see that `total` does not get 5 added to it.  Therefore, the final answer is, as we'd expect, 31.

##### Break

In addition to the continue, we have another, more aggressive, method to control the flow of our programs - `break`. Where `continue` allowed us to skip the rest of the loop's code block and jump directly to the next iteration of the loop, `break` allows us to manually leave the loop entirely.

Time for an illustrative example. Consider trying to write a program that adds the numbers 1 to 8, but only up to 25. If the sum exceeds 25, the total is set to 25 and the message, "The sum exceeded the max value of 25." is printed. We could certainly complete this task with the tools that we already possess, but `break` is better suited to meet the needs of this situation. Let's take a look at what this implementation would look like.

```python
total, x = 0, 1
while x <= 8:
    if total > 25:
        total = 25
        print('The sum exceeded the max value of 25.')
        break
    total += x
    x += 1
print(total)
```

At this point I'm confident that you are tired of looking at tables of values, but let's do this one last time for consistency under the above program specifications.

| After loop #  |   total   |   x   |   x <= 8   | total > 25  |
| ------------- |:---------:|:-----:|:----------:|:-----------:|
| 1             |  1        |   2   |    True    |    False    |
| 2             |  3        |   3   |    True    |    False    |
| 3             |  6        |   4   |    True    |    False    |
| 4             |  10       |   5   |    True    |    False    |
| 5             |  15       |   6   |    True    |    False    |
| 6             |  21       |   7   |    True    |    False    |
| 7             |  28       |   8   |    True    |    True     |

At this point `total` is set to 25 and the message "The sum exceeded the max value of 25." is printed. The loop is exited and then 25 (the value of `total` now) is printed to the screen.

##### Pass

There's one more statement that allows us control over our programs - `pass`. All `pass` does is tell Python to do nothing. Because of this, it is rarely used for control flow, since the same result could be achieved by doing nothing. Instead, it is frequently offered as a place holder, since Python will complain about empty code blocks.

So while you're building up the skeleton of a program, `pass` can be useful as a method to get the framework written up without focusing on implementation. To illustrate...

```python
if x < 0:
    pass
elif x > 0:
    pass
else:
    print('x is the value of 0.')
```

In the above example, we have set it up so that if `x` is 0, then our program tells us so. Otherwise, we know that we're going to do something specific when `x` is positive and something different when `x` is negative.  We have used pass to suggest that we either haven't figured those things out yet, or simply haven't implemented them.
