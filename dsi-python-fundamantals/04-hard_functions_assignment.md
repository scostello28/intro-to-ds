# Hard Functions Exercise 1

# Instructions

For this assignment you'll be working through solving more problems, but this time by building functions from scratch. For each problem, you should build a function into your solution. While we'll discuss general workflow in the next class, tonight you can just build each function into it's own file, and then call it with some arguments right after you define it. For example, pretend all of the following is the solution to one of the problems, written in a function first and then called (for testing purposes) below.

```python
def my_func(param1, param2, param3):
    # Function code to solve the problem

print(my_func(param11, param21, param31))
print(my_func(param12, param22, param32))
print(my_func(param13, param23, param33))
print(my_func(param14, param24, param34))
print(my_func(param15, param25, param35))
```

Note above that `my_func` is called five times after it's definition. The output of each call is printed so running the script from the command line will print the tests. These tests should check that `my_func` works correctly with different sets of arguments. You should aim to test your functions at least 5 times tonight after you write them. It's good to try to think of tests that your function might not solve correctly (we call these **edge cases**). Not only does thinking like this help you solve the problem, but it also gives you more faith in your solution.

You can name each of the scripts you store your solutions and tests in, but know that its bad practice to start the names of scripts with numbers for reasons that we will see in future classes.

# Assignment Questions

### Part 1 - Basic Practice

For the first part of the assignment, we're going to get some practice taking something we've already written and translating it to a function. In continuation of prior assignments, let's work with a couple of the scripts that we wrote for `intro_python_assignment.md` in Week 1, Day 2, and then re-worked in `strings_lsts_assignments.md` in Week 2, Day 1. Let's start out and just move the first two into functions (for extra practice you could do this with the rest of the problems that we worked through in those assignments):

1. Write a function that computes the factorial for an inputted number.  
2. Write a function that determines whether or not an inputted number is prime, and then prints 'The number you inputted is a prime/ not a prime number.' depending on what your script finds (note that this means putting a `print` in front of the function when testing it will be redundant for this case).

### Part 2 - Advanced Practice

Now we're going to push our problem solving and programming skills even further by coding up functions to solve new problems. For each of the problems below, I would suggest coding it up in a similar way to how you did the other two (building the function, and then calling it some number of times (5) to test it out after that).

1. Write a function that counts the number of words in an inputted string, where we consider words to be separated by spaces.
2. Write a function that counts the number of words in an inputted string, where we consider words to be separated by a specified delimiter (so your function should accept two arguments, one for the string and one for the delimiter) and a space is defined as the default delimiter.  
3. Write a function that takes in a string, and returns a list that holds the length of each word in the phrase, separated by an inputted delimiter (so you're function should accept two arguments again). Make a space the default delimiter like you did in `2`. For example, if the arguments to your function were `This is a test string` (and nothing else), your function should return `[4, 2, 1, 4, 6]`. Go ahead and don't worry about removing punctuation (you can include it in the word length - e.g. "this." has five letters, if we count the period).
4. Write a function that returns all the prime numbers up to an inputted number (**Hint**: It might be helpful to use/modify the prime function you wrote earlier).    
5. Write a function that takes in a list of numbers, as well as an additional number (i.e. two arguments), and returns a list of `yes` or `no` depending on whether each number in the list is divisible by the second number. For example, if I input `[10, 25, 36, 12, 20]` as the list of numbers, and `5` as the additional number, your function should return `['yes', 'yes', 'no', 'no', 'yes']`.
6. Write a function that takes in a list of strings, as well as an inputted letter (which looks like a string with a single character), and returns a list of only those strings from the input list that end with that letter. For example, if I input `['I', 'am', 'in', 'love', 'with', 'Python']` as the list of strings, and `n` as the inputted letter, your function should return `['in', 'Python']`.
7. Write a function that takes in a list of strings, as well as an inputted substring (i.e. another string), and returns a list of the indices of the strings that contain that inputted substring. For example, if I input `['This', 'is, 'an' , 'example']` as the list of strings, and `is` as the substring, your function should return `[0, 1]`.

### Extra Credit

1. Let's build a calculator for figuring out how much I owe in taxes (and by calculator, I mean function). Write a function that takes in a list of tuples, where each tuple contains two values, as well as an income to compute the taxes on (so your function should accept two arguments). For the tuple list, the first value of a tuple will be an income upper bound, and the second will be a tax rate for all income up to the given income bound. You need to build a calculator that will calculate the tax for all income up to each income bound (if it goes up that high) for the given tax rate. You can assume that the list of tuples will be sorted by the income bound (e.g. the first value in the tuple), such that the lowest income bound will be first, and the highest last (see below for an example).  

 As an example, let's say my tax info is `[(50000, 0.08), (100000, 0.10), (150000, 0.15)]`. This means that the first 50k of income is taxed at 8%, the second 50k at 10%, and the rest at 15% (note here that any income that is left past the highest upper bound given is taxed at the rate for that highest upper bound). So, if the inputted income was 70k, then my taxes would be 50 * 0.08 + 20 * 0.10 = 6k. You should write your function to be generalized and accept any kind of list of tuples and any inputted income (so it'll accept two arguments).  

2. Now modify your solution to `Extra Credit 1` to accept a list of tuples that is not sorted by the income bound.

 **Hint**: Trying using the `sorted` function and working with the `key` argument (a [lambda](http://www.secnetix.de/olli/Python/lambda_functions.hawk) function will probably be helpful here).
