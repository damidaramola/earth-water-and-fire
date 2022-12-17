# Earth Water and Fire
This simple python game is a variation of the game 'rock , paper, scissors'. In this game, the player must pick the option of either Earth , Fire or Water in order to play against the computer and beat it. In order to make the game more unique, I have added my own rules!

## Features
### Import random  
* This python project utilises a random method which is very essential. It allows the player to play with the computer by causing the computer to randomly pick a choice of either Earth , Water and Fire. 
![import random](https://user-images.githubusercontent.com/110638513/208222489-0fe701fa-56f5-492d-9e75-19ce5bb3b0ac.PNG)
![computer choice](https://user-images.githubusercontent.com/110638513/208222579-2be61857-a2bd-461f-a9b8-57fd2b555751.PNG)
### Instructions of Game
* I have included the instructions of the game within my code in order to explain how the user should play. Since the game doesn't use the conventional rules of 'rock , paper , scissors ', I thought it would be very useful. 
![instructions](https://user-images.githubusercontent.com/110638513/208222557-35319b41-468f-4636-a280-74036411dc76.PNG)
### Variables 
* There are a few essential variables that are used to keep track of the score. These are 'computer_wins' , 'you_win' and lastly 'draw' in the case of a tie occuring between the player and the computer. The 'select_option' variable also holds the list of options that the player and computer chooses from.
![variables](https://user-images.githubusercontent.com/110638513/208222567-f5d8f104-bb27-4604-82e2-f983d87ccd1d.PNG)
### Function that checks for the winner
* The 'check_winner' function checks  who, (the player or the computer) wins that round depending on the option that they choose. It is comprised of a series of if/elif/else statements and the possible outcomes in the game.
![check winner function](https://user-images.githubusercontent.com/110638513/208222569-96ea9fbd-c4fc-4336-a1c3-2eb05dbbb5fe.PNG)

### Print Results 
* Lastly , The results are printed to the terminal while the scores add up for each round the user plays against the computer. 
![print results](https://user-images.githubusercontent.com/110638513/208222634-5601596a-47b5-4353-8df0-179ea0ec5217.PNG)
![scores](https://user-images.githubusercontent.com/110638513/208224235-e79e08a6-b518-47c6-bd68-da394a07d61e.PNG)

## Testing 

* I have tested the code in the CI code linter and the only error is that the line is too long on line 77 which I tried to fix with no avail.
![CI python Linter](https://user-images.githubusercontent.com/110638513/208224154-d08396b4-7e58-440c-bd56-14f5931405af.PNG)
### Validation testing for blank space
* At the start of the game where the player is asked to type in their name, a while loop is used for validation to check if the user has put in a blank space/has pressed the 'enter' key without typing anything in. If this error is made, a print statement with declare this issue and will prompt the player to input a correct username.
![validate blank spaces](https://user-images.githubusercontent.com/110638513/208222706-357abe02-5c5a-4e7f-990f-99ed14b8254b.PNG)
![blank validation](https://user-images.githubusercontent.com/110638513/208223026-4e7ed3a8-b1a1-41da-800e-4fe4dcaa6fb8.PNG)

### Validation of chosen option - (Earth , Fire or Water )
* Using another while loop, the answer the player puts in for either 'Earth, Fire or Water' is checked for different variations. These words have been converted into lower case using the .lower() method. If the wrong value is added, this will print an error.
![while loop validator f e w](https://user-images.githubusercontent.com/110638513/208222574-ef0b192f-d236-4537-97ab-e1f957a76c1d.PNG)
![fire water validation](https://user-images.githubusercontent.com/110638513/208223402-4c0dd30c-d69c-4a09-9a38-18e221be689a.PNG)

## Possible Features

* I can add a play again feature at the end next time so the player can rerun the program
* I could Also add features and extentions to make the code look more appealing 

## Deployment
This website was deployed to Heroku.
Steps to deploy:

1. On the landing page, navigate to the right hand side of the page and click the hamburger menu.
2. Click Dashboard.
3. Click the 'create new app' button on the Heroku Dashboard
4. Create a unique name for your project and select your region
5. Go to the the settings header 
6. Click on 'config var' if you have a creds.json file and need to connect and fill in necessary fields.
7. Go to 'Add buildpack' and pick the python buildpack first. Save changes
8. Next, pick the node.js buildpack and save the changes
9. Now go to the Deploy section and click connect to GitHub.
10. Seach for your GitHub repository name and connect Heroku with your GitHub repository code.
11. Choose either Manual Deploy or Automatic Deploy depending on your preference.
12. After your applications has been successfully been deployed. Click 'view' to run your program.

# credits 

* The format used to make this README file was taken from the CI sample project README.md video [README.md example](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CSSE_PAGPPF+2021_Q2/courseware/66cf361c769a41d496f5001fae6f9be7/3b5cd5dc8313462aa5975a3c9b9a1a3c/)
* The tutorial used to make this website was taken from [tutorial](https://www.youtube.com/watch?v=LumFgJxRjP4)
                                                               
