

## Wordle in Python

------

This project is a fully functioning python wordle replica, in which players have 6 attempts to find 
a random 5 letter word. The user will type in a guess, hints will be visually displayed depending on the guess, and the player will try to get closer and closer to the game word. 


The link to the deployed app can be found [here.](https://wordle-in-python.herokuapp.com//)

The link to the Github repository can be found [here.](https://github.com/FranciscoBarreira/python-project/)


![mockup site generator image](/images/mockup-image.png "mockup preview")

## Table of Contents 

[User Experience](#user-experience)

   - [User Requirements](#user-requirements)
   - [User Stories](#user-stories)



[Technologies Used](#technologies-used) 

[Features](#features)   

   - [Let's Play Wordle Screen](#lets-play-wordle-screen)
   - [Instructions](#instructions) 
   - [Play The Game](#play-the-game)
   - [End Game](#end-game)

[Program Diagram](#program-diagram)    


[Testing](#testing)   

   - [General Testing](#general-testing)
   - [Validator Testing](#validator-testing)


[Site Deployment](#site-deployment) 

[Credits](#credits)   

   - [Content](#content) 
  


## User Experience 
<a name="user-experience"></a>

------


### User Requirements 
<a name="user-requirements"></a>

- The app should have clear instructions on how to play the game
- The app should have an option to play again
- The letters should be coloured to provide hints on the word
- The word_bank should have enough words for replayability



### User Stories
 <a name="user-stories"></a>

- I want to be able to see the correct word if I lose
- I want to be able to play the game as many times a I want
- I want to be provided visual hints after each guess




## Technologies Used
<a name="technologies-used"></a>

------



-Heroku for the app deployment

-Python to build the program

-GitHub for software hosting

-GitPod for development hosting

-app.diagrams.net for the diagram

-fsymbols.com for the emojis and ascii art

-termcolor for coloring the letters


## Features  
<a name="features"></a>

------

### Let's Play Wordle Screen
<a name="lets-play-wordle-screen"></a>
  
This is the first screen that prompts once the program is running. It displays a welcome 
message and a menu that gives the player the choice to play, see the instructions or quit.

![wordle image](/images/wordle-screen.png "wordle")



### Instructions
<a name="instructions"></a>

If the player types 2, this set of prints will show, explaining in detail the rules of the game.

![instructions image](/images/instructions-image.png "instructions")


### Play The Game
<a name="play-the-game"></a>

This is when the game starts to unfold. After the user types a 5 letter word, that same word will be presented on screen with possibly some of the letters coloured. This works as a visual hint for
the player. If the word is coloured yellow, they'll know that said letter is a part of the game word, but is in the wrong place. In the image below, we can see that n is not the last letter of the game word, so it must be somewhere else. If the letter is coloured green, then it is in the right place. For instance, using that same example, St are the first two letters of that word.

![game image](/images/game-image.png "game")


### End Game
<a name="end-game"></a>

If you get the word right, a congratulatory message will be displayed, followed by the possibility to play again. If the player can't guess the word in six attempts, another message shows to let them know they didn't get the word right. The play again prompt still appears in this case.  

![endgame image](/images/endgame-image.png "endgame")



## Program Diagram
<a name="program-diagram"></a>

------



A diagram that breaks down the way the program works can be found in the image below.

![diagram image](/images/diagram.png "diagram")


## Testing
<a name="testing"></a>

------

### General Testing
<a name="general-testing"></a>

To make sure the game is played properly, two validation blocks were included in the code. 
The first one ensures that, when the options menu appears, the only valid inputs are 1,2 or 3. Any other input will lead to a valueError and the user will be asked to input one of the available options.

![menu-error image](/images/menu-error.png "menu-error")

The second validation block was put in place to make sure the word a player inputs is 5 letters long. If there was no limit to the number of letters, the player could just write the entire alphabet and find immediately which 5 letters are in the word. If a word of different lenght is input by the player, a valueError will be raised and they will be asked to type a 5 letter word.

![word-error image](/images/word-error.png "word-error")



### Validator Testing
<a name="validator-testing"></a>

Pep8- No errors were shown when put through the pep8 requirements test.

![pep8 image](/images/pep8.png "pep8")



## Site Deployment
<a name="site-deployment"></a>

------

This site was deployed to Heroku. The steps to deploy it were:

-Create a new app in Heroku 

-In Settings, added PORT 8000 to config vars

-In Settings, press BuildPack, and add Python and Node.js 

-In the Deploy tab, select the deployment method (github was used in this case)

-Click the connect button

-Choose manual or automatic deploy (manual was used in this ocasion)



## Credits
<a name="credits"></a>

------


### Content
 <a name="content"></a>

For this project, the following sources of information were used:

-Stackoverflow and w3schools for various code related doubts

-Youtube Python Tutorials


