This is a game for Mental Anguish and the following explains how the game works.
In order to start the game, the "Question_pool" text file must be loaded in the IDE directory along with the py charm
file. When that is loaded and the run command is hit, the GUI will appear. Under the edit menu button in the top left
corner of the GUI, the following menu options are listed:
Add Question:
    Add question is a function used to add a question to the preexisting text file. The user will enter the information
    that is provided by the GUI such as, question, choices, feedback and points. After they are finished they hit the
    submit button

Edit Question:
    Edit question is used to edit a certain question and it's components. The user double clicks the question they want
    edit from the listbox (In order to see more questions from the listbox, the user can scroll using their mouse), and
    the question field will prepopulate with the question they double clicked. The user will then edit the rest of the
    information in the entry boxes, and after they are finished they hit the submit button.

Delete Question:
    This function only shows the listbox of the questions and as the user double clicks on the question they want to
    delete, the listbox will remove the question from the view. The file updates and the question and components are
    removed from the file.

Start 1 Person Quiz:
    This is the game mode for the GUI. The user has three questions where the must answer the correct answer. In the
    entry box, the user will type in their guess (word for word) and then click on the button. The GUI will display a
    pop up with feedback in correlation if the guess was correct or not. Then the GUI loops to the next question and the
    game repeats until three times. The button will be disabled and the question list will be viewed again.

View List of Questions:
    This is a simple action that the user clicks in order to view the list of questions in the file in a listbox format

Search Question:
    This section allows the user to search for a question, either by a partial string match or by a point value. If any
    matches appear, the GUI will print to itself all the following information matching that search