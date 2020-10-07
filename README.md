# python_djangoGreatNumberGame
Coding Dojo Assignment

Assignment: Great Number Game
Objectives:
Practice using session to store data about a client's history with the web app
Practice clearing a session
Practice having the server use data submitted by a client with a form
I'm thinking of a number between 1 and 100...

Create a site that allows a user to play this guessing game. Upon loading, the server should "pick" a random number between 1-100; store the number in session. Allow the user to guess the number--tell them when they are too high or too low. If they guess the correct number, notify them and offer to play again.

There are many different ways to do this assignment. When you finish the basic functionality, find a peer and compare your code!

Reminder
In order to generate a random number you can use the random Python module:

import random 	                # import the random module
random.randint(1, 100) 		# random number between 1-100


 Create a new Django project called great_number_game
 In the root route, save a random number between 1 and 100 and display a form for the user to guess the number
 Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
 NINJA BONUS: Display the results as shown in the wireframe above (i.e. with appropriate colors and positioning)
 NINJA BONUS: Allow the user to keep guessing until they get it correct
 NINJA BONUS: Let the user know how many attempts they took before guessing the correct number
 SENSEI BONUS: Only allow the user to guess up to 5 times. If they don't guess it on their 5th attempt, display a "You Lose" message and allow them to try again.
 SENSEI BONUS: If they win, allow the user to submit their name. Have a link to a leaderboard page that shows winners' names and how many attempts they took to guess correctly.
