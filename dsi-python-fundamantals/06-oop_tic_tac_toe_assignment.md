# Object Oriented Programming (OOP) Exercise

# Instructions

This assignment is designed to get you thinking about problems in an OOP framework. A great way to immediately jump into this mindset is by taking a problem that you've already solved and try to fit it into the OOP box. A perfect problem to get us going with this is the tic-tac-toe game from week 3. This entire problem with revolve around a solution to that problem that was written with functions. So if you haven't worked on that problem yet, you have one of two options. First you can go back and work on a solution for it. This is somewhat advised since programming is very much a game of practice makes perfect. Otherwise, if you want to jump into working with some hard classes you can work from the solution in the solutions repo as a starting point for this assignment.

Tonight's assignment is going to walk you through turning the tic-tac-toe game into a class, or rather, a couple of classes. We'll give you some ideas for classes you should construct, what attributes and methods they should have, and then let you dive in. Since you have already solved this problem in the procedural paradigm and have code to do so, we won't give too stringent of guidelines here, as we hope that you can reuse most/all of the code you wrote when solving this problem before. 

As a final note, it might be worth it to read over the entire assignment to get an idea of everything that you are tasked with doing tonight, and then take a little bit of time to plan out how you are going to approach this problem. While code can always be refactored, an extra 10-15 minutes of planning upfront is usually worth it.

## The `Board` Class

The first class that I would build would be a `Board` class, as this is the centerpiece of the game. Previously you likely stored the board as a list of lists. While this usage of lists seemed fairly well suited for the tic-tac-toe problem, now that you know about classes, can you see why it makes more sense to have a class devoted entirely to the board? This will allow you to take advantage of encapsulation.

I would imagine that this class would have two attributes - the `board_size` and the actual `board` data. In terms of methods, the `Board` is probably going to need methods to handle some of the logic that occurs during the game - checking if certain coordinates on the board are taken and/or valid given it's size, actually filling a spot on the board when a player inputs valid coordinates, and then determining whether or not anybody has won. Also, it'd be nice if the `Board` has a method that displays what it looks like.

Some notes: 

* While you can imagine that you could simply get the `board_size` by taking the `len()` of the board, it might make sense to store the `board_size` as an attribute, since you will want to know it pretty frequently (this way we avoid having to call `len()` over and over again when we want to get the size of the board). 
* In terms of breaking up some of the logic when a player inputs coordinates, I imagine this to happen in two steps: (1) Checking to see if the inputs are properly formatted - this check looks at whether or not **two numbers** were inputted, and (2) Checking to see if the inputs are valid, **given** the board - this check looks at what spots are currently taken on the board, and if the inputted coordinates are contained within the board's dimensions. 

In an OOP framework, we should be thinking about where to implement checks like these. The reason this is important is because there is going to be more than one class in this tic-tac-toe solution, and also in many of your future OOP solutions. Therefore, it's good to get used to thinking about what classes should contain what logic or methods required for a solution. As applied to this problem, since `(1)` doesn't involve the board, I would think that this check shouldn't be done in the `Board` class (we'll figure out where it will be done soon). `(2)` does involve the `Board` class, though, and so I can imagine that it should be done in the `Board` class.

## The `Player` Class

After building the `Board` class, I would move on to building a `Player` class, since this is the other part of the game that we need for it to run. Once we have players and a board, we could actually have a game! As you'll see, though, I would suggest that we also build a `Game` class, which will allow our entire tic-tac-toe game to be wrapped up in one nice encapsulated class.  

In terms of the `Player` class, I imagine that it will just have a couple of different attributes, and that's it. I think that all the necessary logic for the game should be built into the `Board` and `Game` classes, leaving very few things for our `Player` class. 

So, what should the `Player` class have, then? Well, every player is going to need a `name`, and so I would think that should be one of the class' attributes. In the game, every player is also going to have a symbol that they are using (either ' X ' or ' O ' in our game) to make their plays. I think that it would be useful to store that on the `Player` class as well. 

## The `Game` Class

After building up the `Player` and `Board` class, I would have all the parts of the game that I need. Now, all I would need would be some kind of game engine to run it. While I could code this up solely with functions like we did when we first built our game, I think it makes sense to encapsulate my game within a class. 

So, what does the `Game` class need to do? Well, we know that we've already got a `Player` and `Board` class, and that our tic-tac-toe game is going to need to have a `Board` and two `Player`s. This means that our `Game` is going to have to keep track of these - it'll need a `board` and `players` attributes. I imagine that the `board` attribute is just a `Board` object, and that the `players` attribute is a `tuple` (since the number and specifics of the players won't be changing within the course of a single game) of `Player` objects (2 of them).

Cool... what's next? Or rather, what's left? What else do we need to run this game? Well, we need to have the entire game actually set up - this means our `Game` class will need to instantiate a `Board` object, as well as two `Player` objects. I would think that this should take place when the `Game` object is first initialized.  After that, our `Game` object simply needs to allow our players to play the game! This will involve all the logic that hasn't yet been implemented - asking a player for a coordinate, checking that the coordinate is valid (regardless of the board), telling the board to do what it needs to, and then printing out the final results. Much of this logic can be adapted from your previous solution!

Some notes: 

* I've mentioned that I think that the `Board` object and two `Player` objects should be created when the `Game` object is first initialized. While this does mean that it should happen **via** the `__init__` method, that would be a lot of code to place directly in the `__init__`  method itself. In situations like this, it is common practice to build the initialization into it's own method (or methods), and then call that method (or methods) from within the `__init__` method. For example, I would personally build one method for initializing the players (call it `_initialize_players(self)`), and another one for initializing the board (call it `_initialize_board(self)`). Then, my `__init__` method would involve calling those two initialization methods. 
* Above, I stated that one of the steps that the `Game` object should implement is to tell the board what it needs to do. This is part of the beauty of OOP - the `Game` object doesn't really have to think about what the `Board` object is doing; it just has to tell the `Board` object what to do, and know what the `Board` object is going to do. So, I wrote above that the `Board` object should check if a set of coordinates is valid, then fill in that set of coordinates if it is valid, and finally check if there is a winner. In this case, all the `Game` needs to know is if that process was successful, and if there is a winner (i.e. can/should the players continue playing, do they need to input another coordinate because they inputted an invalid one, is there a winner, etc.).  

## Some final thoughts

The above are just suggestions, and you are free to use them or choose to tackle the problem a different way. The end goal of the night is to get more practice working in an OOP framework, and coding! And again, we've specifically left this somewhat open-ended in terms of the instructions, since we are hoping that you use some/all of the code that you wrote when we took a functional approach to this problem. 

### Extra Credit

1. Alter your `Board` class to use the `__repr__` magic function when being displayed (you can check out the `__repr__` magic function [here](http://www.rafekettler.com/magicmethods.html#representations)). 
2. Alter your `Player` class to also use the `__repr__` magic function. Construct your `__repr__` magic function such that it displays the name of the player when being displayed. 
3. Now, go back to the `__repr__` magic function that you built in the `Board` class, and alter it so that you have a better looking board. Instead of just displaying the board as a list of lists, I'm imagining something like this: 

 ```
     0   1   2
 0    |   |  
    -----------
 1    |   | 
    -----------
 2    |   | 
```
4. Let's allow the game to be a little bit more dynamic. Alter your `Board` class to take in a `board_size` argument, rather than having it just be `3` all the time. This means that you'll have to alter any of your methods that are reliant on this `board_size`, including the `__repr__` magic function that you just built in `3.` above. **Hint**: This shouldn't be as hard as you think - it should just involve finding all the places that reference the `board_size` (or wherever you've hard coded a `3`), and altering those to now be dynamic. 
5. Dynamic is fun, so let's do even more! Modify your `Game` class to not only play 1 game, but to allow the players to keep playing until they wish to stop. This means that after a win or tie, you'll have to check if the players want to keep playing, and then reinitialize everything if they do (and exit if they don't). To make it a little more interesting, keep track of each players number of wins (use an attribute on the `Player` class) and display the results when the players are all done playing.  
