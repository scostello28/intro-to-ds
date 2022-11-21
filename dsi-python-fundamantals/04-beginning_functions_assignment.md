# Beginning Functions Exercise 1

# Instructions

Tonight we'll work through building functions and getting practice with their syntax. We'll begin by having you complete function definitions that are already written, and then move on to you writing function definitions for code that is already written. Next, we'll work on translating some of the code we've already written into functions. We'll finish up by writing some functions of our own, from start to finish.  

For each of the functions you build tonight, you should be sure to test them out multiple times to make sure that they work correctly! We would also suggest that you code each function up separately in its own script.

# Warmup

### Part 1

For the first set of problems below, fill in the given function definition to achieve the desired results.  

1. Remember the song '99 bottles of beer on the wall'? Well, we've written a function that will take in a number (`n`), and we want you to complete it such that it prints a line from the song. `n` will hold the number of bottles of beer on the wall, and we want you to complete the function assuming that there are `n` bottles of beer on the wall. After completing it, test that it works by calling it some number of times.

 ```python
    def calc_beers_on_the_wall(n=99):
        """Print how many beers remain on the wall.

        Args:
            n: int
                Holds the number of beers that remain on the wall.
        """
        pass
```

 * What does it mean for me to write `n=99` in the function definition, as opposed to just `n`? Try calling your function both with and without an argument given - what happens in each case? Why does this happen?
 * Change the `99` to `50`. What do you expect to happen? Call your function, and verify that you get the intended results.

2. Remember [Elsa](http://pre11.deviantart.net/7144/th/pre/f/2014/027/b/d/let_it_go_by_impala99-d740xws.png) from `Frozen`? We've heard mixed reviews of her song 'Let It Go'. We've written a function below that will take in a boolean (the `fan` parameter), where this boolean holds whether or not a person is in favor of 'Let It Go' (i.e. if `fan` is `True`, they are in favor, and if it is `False`, they are not in favor). We want you to complete the function such that:

 * If the person is a fan, then it prints "I love Elsa! She's my favorite!"
 * If the person is not a fan, then it prints "Let It Go, it's not that great."  

 ```python
    def check_elsa_fan(fan):
        """Print a certain phrase depending on the value of fan.

        Args:
            fan: boolean
        """
        pass
```

 * Change the function definition so that it **defaults** to the person being a fan. Try calling your function both with and without arguments now - how does this effect what gets printed out?

### Part 2

For this next set of problems, you're going to get a block of code that solves some problem (which we'll describe). Your goal is to write a function definition statement that uses that block of code (this is the opposite of what we did in the first part).  

3. Below, I've written a line of code that will print `Hello, <name>`, where `name` will be a parameter in the function definition. Write a function that takes in one parameter, `name`, and then uses the line of code below to print 'Hello' to that `name`.   

 ```python
 print('Hello {}'.format(name))
 ```

 * Did you write the function definition according to the verb/noun adage? Does your function have a good name that at least hints at what it does?
 * Test out your function by passing in different values for `name`. Does it print the expected output?
 * Now, alter your function definition such that it **by default** says hello to "Josh" if no value for `name` is passed in.

4. Now for something a tad more intricate. Below is some code that relies on two unknowns, `n` and `potential_divisor`. This code returns a `True` or `False` depending on whether or not `n` is evenly divisible by `potential_divisor`. Your first goal is to write a function that accepts these two parameters in its definition and has the code below as its body.

 `return n % potential_divisor == 0`

 * First off, how/why does this work? Why does it return either a `True` or `False`?
 * After building your function definition, test it out to make sure that it works correctly (remember that it should take in two parameters, `n` and `potenial_divisor`).  
 * Now, alter your function definition so that **by default** the `divisor` is equal to 2 (i.e. by default it just checks if the inputted `n` is even). Now that you've made one of the parameters have a default, what stipulations come with that change (*Hint*: Remember, order of the parameters now matters).   
 * Now that we've got two parameters, try calling them *by position* and *by keyword*, and mixing the two (e.g. one argument by position and the other by keyword, and vice versa). What stipulations come with these kinds of calls (*Hint*: Remember, order matters)?

# Assignment Questions

### Part 1 - Basic Practice

For the first part of the assignment, we're going to get some practice taking code we've already written and making it a function. Let's work with a couple of the scripts that we wrote for `intro_python_assignment.md` in Week 1, Day 2.

Let's start by making changing problems three and four from that assignment into functions (for extra practice you could do this with the rest of the problems that we worked through in those assignments). Below are the original problem statements. To move these to functions, we will no longer take user input, but instead pass an argument(s) into a function and consider that to be the "user input".

If you haven't written a solution to these problems feel free to use the solution's code. While you could also try to solve this problem, the point of this part is to get you practice with functions by using code you've already written. The idea is that you can get practice moving already existing code into functions.

1. Write a function that computes and prints all of the divisors of a user inputted number.

 * Here we won't take a user inputted number, but build a function that accepts one parameter, a number, and then computes all the divisors of that number. The solution to the previous assignment *might* need to be modified for it to work in a function.

2.  Write a function that computes the least common multiple between two user inputted numbers.

 * Here we won't take any user inputted numbers, but build a function that accepts two numbers as parameters, and then computes the least common multiple of those two numbers. Again, whatever code you have that does this *might* have to be modified to work in a function.

### Part 2 - Advanced Practice

Now we're going to work our problem solving and programming skills by coding up functions to solve new problems.  

1. Write a function that figures out whether or not we have any beers left on our wall. It should take in a number, and then print 'No beers left' if we are at the end (i.e. there are `0` beers left) or 'Beers left!' if we are not at the end (i.e. there are not `0` beers left).
2. Let's imagine that I know all of the Elsa fans out there, and they're just Cary, Josh, and Sean (it's okay, we're the three best friends anybody could ever have). Write a function that takes a `name`, and then returns a `True` or `False` as to whether or not they are an Elsa fan. You can use the knowledge that if they aren't Cary, Josh, or Sean, they aren't an Elsa fan. Also, remember that checking membership using a `set` is incredibly fast! Try to use a `set` if you can.
3. Write a function that computes the sum of the numbers in an inputted list. Use a `for` loop to do this. When you're done, look up the [sum](https://docs.python.org/3/library/functions.html#sum) function (and notice that this does the same thing as what you just wrote!).

 * Example: If I input `[1, 2, 3]`, your function should return `6` (1 + 2 + 3 = 6).

4. Write a function that computes the product of the numbers in an inputted list. Use a `for` loop to do this as well.  

 * Example: If I input `[2, 3, 4]`, your function should return `24` (2 * 3 * 4 = 24).

5. Write a function that takes in an arbitrary list, and returns a list of the numbers in that list that are even.

 * Example: If I input `[2, 4, 5, 7, 10]`, your function should return `[2, 4, 10]`.
