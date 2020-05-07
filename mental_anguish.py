#Naramsin Marokeel, CIS345, 12pm, Project
from tkinter import *
import random
from tkinter import messagebox


class Question:
    """Question class to hold all the information for a question"""

    def __init__(self, question, answer1, answer2, answer3, answer4, correct, points, correctFeed, incorrect):
        self.__question = question
        self.__label = Label(window, text=question)
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct = correct
        self.__points = points
        self.__correctFeed = correctFeed
        self.__incorrect = incorrect

    @property
    def question(self):
        return self.question

    @question.setter
    def question(self, question):
        self.__question = question


def display_question():
    """Used to display the question, answer choices, and points in the frame, as well as being able to enter your
    answer and click another button for the next question"""
    global one_person_quiz_frame, file, split, detail, tries

    add_question_Frame.grid_forget()
    quiz_frame.grid_forget()
    one_person_quiz_frame.grid_forget()
    question_list_frame.grid_forget()
    select_question_frame.grid_forget()
    search_question_frame.grid_forget()
    one_person_quiz_frame.grid(row=0, column=0, rowspan=7, columnspan=5, sticky=N + E + S + W)

    if tries < 3:
        print(tries)
        file = open('Question_pool.txt', 'r')
        split = random.choice(file.readlines())
        detail = split.split(',')
        Label(one_person_quiz_frame, text='Question').grid(row=0, column=0)
        question = Entry(one_person_quiz_frame, textvariable=new,state=DISABLED, fg='black', width=100)
        new.set(detail[0])
        question.grid(row=0, column=1, columnspan=5)

        Label(one_person_quiz_frame, text='Points:').grid(row=6, column=2, sticky=W)
        Label(one_person_quiz_frame,text=detail[6]).grid(row=6,column=3)

        Label(one_person_quiz_frame,text='Number of Questions Asnwered out of 3').grid(row=7,column=1)
        Label(one_person_quiz_frame,text="{}".format(tries)).grid(row=7,column=2,sticky=W)

        Label(one_person_quiz_frame, text='Answer Choices').grid(row=1, column=0,sticky=W)

        answer1 = Entry (one_person_quiz_frame, text=choice1,state=DISABLED, fg='black')
        choice1.set(detail[1])
        answer1.grid(row=2, column=0,sticky=W)

        answer2 = Entry (one_person_quiz_frame, text=choice2,state=DISABLED, fg='black')
        choice2.set(detail[2])
        answer2.grid(row=3, column=0,sticky=W)

        answer3 = Entry (one_person_quiz_frame, text=choice3,state=DISABLED, fg='black')
        choice3.set(detail[3])
        answer3.grid(row=4, column=0,sticky=W)

        answer4 = Entry (one_person_quiz_frame, text=choice4,state=DISABLED)
        choice4.set(detail[4])
        answer4.grid(row=5, column=0,sticky=W)

        submit_button = Button(one_person_quiz_frame, text='Submit', command=check_answer)
        submit_button.grid(row=6, column=1)

        c1 = Label(one_person_quiz_frame, text='Enter Answer ')
        c1.grid(row=8)

        choice.grid(row=7, column=1)


def question_frame():
    """A frame to hole the Questions to list"""
    global question_list_frame, add_question_Frame, quiz_frame

    # Forgetting these frames so they don't overlap and make things hard to read
    add_question_Frame.grid_forget()
    quiz_frame.grid_forget()
    one_person_quiz_frame.grid_forget()
    question_list_frame.grid_forget()

    # Creating the label and printing on the main gui the questions
    Label(question_list_frame, text="Question Pool").grid(row=0,column=0)
    question_list_frame.grid(row=0, column=0, rowspan=7, columnspan=5, sticky=W)


def question_list():
    """Displays the questions in the text file as the main application opens"""
    question_frame()
    list_box = Listbox(question_list_frame,width=100)
    # automatically opens and closes the file when not in use
    with open('Question_pool.txt', 'r') as fp:
        line = fp.readline()
        count = 1
        while line:
            list_box.insert(END,"{}) {}".format(count, line.split(',')[0]))
            list_box.grid(sticky=W)
            line = fp.readline()
            count += 1


def save_data():
    """Used for when the submit button is clicked, the following attributes are added to the text file"""
    global new, point, choice1, choice2, choice3, choice4, correct, correctFeedback, incorrectFeed, edit_index,edit_mode

    # opening file as append to add to it
    file = open('Question_pool.txt', 'a')

    # getting the values put in to append to text file
    new = '\n' + new.get() + ','
    choice1 = choice1.get() + ','
    choice2 = choice2.get() + ','
    choice3 = choice3.get() + ','
    choice4 = choice4.get() + ','
    correct = choice1
    point = str(point.get()) + ','
    correctFeedback = correctFeedback.get() + ','
    incorrectFeed = incorrectFeed.get() + ','

    # writing the values to the text file
    file.write(new)
    file.write(choice1)
    file.write(choice3)
    file.write(choice2)
    file.write(choice4)
    file.write(correct)
    file.write(str(point))
    file.write(correctFeedback)
    file.write(incorrectFeed)
    file.close()

    # Forgetting the frame
    add_question_Frame.grid_forget()

    # # setting the entry boxes to blank so when the user wants to add another question, the old data doesn't interfere
    new = ''
    choice1 = ''
    choice2 = ''
    choice3 = ''
    choice4 = ''
    correct = ''
    point = ''
    correctFeedback = ''
    incorrectFeed = ''


def add_question():
    """Used to add questions and their attributes to the text file"""
    global file, add_question_Frame, question_list_frame, new, edit_mode,edit_index
    # Forgetting frame so it doesn't interfere
    add_question_Frame.grid_forget()
    quiz_frame.grid_forget()
    one_person_quiz_frame.grid_forget()
    question_list_frame.grid_forget()
    select_question_frame.grid_forget()
    search_question_frame.grid_forget()

    add_question_Frame.grid(row=0, column=0, rowspan=10, columnspan=10, sticky=N + E + S + W)

    # New question entry form
    newQuestion = Label(add_question_Frame, text='Enter a new Question ')
    newQuestion.grid(row=0, column=0)
    new_question_entry = Entry(add_question_Frame, textvariable=new,width=80)
    new.get()
    new_question_entry.grid(row=0, column=1, columnspan=1)

    # answer choice one entry form
    answer1 = Label(add_question_Frame, text='Enter the correct answer ')
    answer1.grid(row=1, column=0)
    answer1_entry = Entry(add_question_Frame, textvariable=choice1,width=80)
    choice1.get()
    answer1_entry.grid(row=1, column=1)

    # answer choice two entry form
    answer2 = Label(add_question_Frame, text='Enter an incorrect answer  ')
    answer2.grid(row=2, column=0)
    answer2_entry = Entry(add_question_Frame, textvariable=choice2,width=80)
    choice2.get()
    answer2_entry.grid(row=2, column=1)

    # answer choice three entry form
    answer3 = Label(add_question_Frame, text='Enter an incorrect answer ')
    answer3.grid(row=3, column=0)
    answer3_entry = Entry(add_question_Frame, textvariable=choice3,width=80)
    choice3.get()
    answer3_entry.grid(row=3, column=1)

    # answer choice four entry form
    answer4 = Label(add_question_Frame, text='Enter an incorrect answer ')
    answer4.grid(row=4, column=0)
    answer4_entry = Entry(add_question_Frame, textvariable=choice4,width=80)
    choice4.get()
    answer4_entry.grid(row=4, column=1)

    # point entry form
    points = Label(add_question_Frame, text='Enter point values')
    points.grid(row=0, column=3)
    points_entry = Entry(add_question_Frame, textvariable=point)
    point.get()
    points_entry.grid(row=0, column=4)

    # correct feedback entry form
    correctFeed = Label(add_question_Frame, text='Enter correct feedback')
    correctFeed.grid(row=5, column=0)
    correctFeed_entry = Entry(add_question_Frame, textvariable=correctFeedback,width=80)
    correctFeedback.get()
    correctFeed_entry.grid(row=5, column=1)

    # incorrect feedback entry form
    incorrect = Label(add_question_Frame, text='Enter witty incorrect feedback')
    incorrect.grid(row=6, column=0)
    incorrect_entry = Entry(add_question_Frame, textvariable=incorrectFeed,width=80)
    incorrectFeed.get()
    incorrect_entry.grid(row=6, column=1)

    # button to submit all the forms
    submit = Button(add_question_Frame, command=save_data, text='Submit')
    submit.grid(row=7, column=3)

    with open('Question_pool.txt', 'r') as fp:
        line = fp.readline()
        while line:
            list_box.insert(END,line.split(',')[0])
            line = fp.readline()
            list_box.grid()
            Scrollbar(add_question_Frame,orient="vertical")


def check_answer():
    """Used to make sure the entered answer is correct or not, and also keeping track of total points"""
    global choice, answer_choice, tries, submit_button, total, point, file, split, detail
    # getting the answer being submitted and comparing them to the text file
    answer = answer_choice.get()
    total = 0
    points = int(detail[6])
    if answer == detail[5]:
        results = detail[7]
        messagebox.showinfo('Correct', results)
        display_question()
        total = total + points
        number = "{} points out of {}".format(points,total)
        Label(window,text=number).grid(row=7,column=5)
        tries +=1
    else:
        # if it doesnt match index[5], then print results for index[8] which is the incorrect feedback
        results = detail[8]
        messagebox.showinfo('Wrong', results)
        display_question()
        points = points + 2
        number = "{} points out of {}".format(total, points)
        Label(window, text=number).grid(row=7, column=5)
        tries +=1
    if tries > 3:
        one_person_quiz_frame.grid_forget()
        question_list_frame.grid_forget()
        choice.grid_forget()
        question_frame()


def populate_entry_boxes(event):
    """Used to populate the entry box for the question selected from the list box"""
    with open('Question_pool.txt', 'r+') as fp:
        w = event.widget
        value = w.get(ANCHOR)
        if edit_mode == FALSE:
            list_box.delete(ANCHOR)
            new.set(value)
        list_box.insert(ANCHOR)


def edit_question():
    """Edits the question by calling add_question()"""
    global new, point, edit_index,edit_mode
    add_question_Frame.grid_forget()
    quiz_frame.grid_forget()
    one_person_quiz_frame.grid_forget()
    question_list_frame.grid_forget()
    search_question_frame.grid_forget()

    select_question_frame.grid(row=0, column=0, rowspan=10, columnspan=10, sticky=N + E + S + W)

    add_question()


def delete_selection():
    """Selection screen to delete the question"""
    add_question_Frame.grid_forget()
    quiz_frame.grid_forget()
    one_person_quiz_frame.grid_forget()
    question_list_frame.grid_forget()
    search_question_frame.grid_forget()

    select_question_frame.grid(row=0, column=0, rowspan=10, columnspan=10, sticky=N + E + S + W)

    with open('Question_pool.txt', 'r') as fp:
        line = fp.readline()
        while line:
            list_delete.insert(END,line.split(',')[0])
            line = fp.readline()
            list_delete.grid()
            Scrollbar(add_question_Frame,orient="vertical")


def delete_question(event):
    """Deletes the selected question"""
    with open('Question_pool.txt', 'r+') as fp:
        w = event.widget
        value = w.get(ANCHOR)
        if edit_mode == FALSE:
            list_delete.delete(ANCHOR)


def search_string():
    """The string search to find any results matching to user input"""
    global file, split, detail, search
    result = search.get()

    file = open('Question_pool.txt','r')
    for line in file.readlines():
        answer = line.split(',')
        if result in answer[0] or result in answer[1] or result in answer[2] or result in answer[3] or result in \
                answer[4] or result in answer[5] or result in answer[6] or result in answer[7] or result in answer[8]:
            Label(search_question_frame, text=answer[0:9]).grid()


def search_frame():
    """Frame to hold the searhc results and input"""
    global file, split, detail, search_question_frame, search

    add_question_Frame.grid_forget()
    quiz_frame.grid_forget()
    one_person_quiz_frame.grid_forget()
    question_list_frame.grid_forget()
    search_question_frame.grid_forget()
    select_question_frame.grid_forget()

    search_question_frame.grid(row=0, column=0, rowspan=7, columnspan=5, sticky=N + E + S + W)

    Label(search_question_frame, text='Search for question').grid()
    search_entry = Entry(search_question_frame, text=search)
    search.get()
    search_entry.grid()

    search_button.grid()


# Creating the main window and the frames associated with the functions above
window = Tk()
add_question_Frame = Frame(window)
quiz_frame = Frame(window)
one_person_quiz_frame = Frame(window)
question_list_frame = Frame(window)
question_list()
select_question_frame = Frame(window)
search_question_frame = Frame(window)
Scrollbar(window,orient='vertical')

list_box= Listbox(add_question_Frame,width=100,height=10)
list_box.bind('<Double-Button-1>',populate_entry_boxes)
list_delete = Listbox(select_question_frame,width=100,height=10)
list_delete.bind('<Double-Button-1>',delete_question)

# variables used for the attributes
new = StringVar()
point = IntVar()
choice1 = StringVar()
choice2 = StringVar()
choice3 = StringVar()
choice4 = StringVar()
correct = StringVar()
correctFeedback = StringVar()
incorrectFeed = StringVar()
answer_choice = StringVar()
search = StringVar()
tries = 1

edit_mode = FALSE

file = open('Question_pool.txt', 'r')
split = random.choice(file.readlines())
detail = split.split(',')
file.close()

# menu file system to edit, add, delete, and start quiz
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label='Edit', menu=filemenu)
filemenu.add_command(label='Add Question', command=add_question)
filemenu.add_command(label='Edit Question', command=edit_question)
filemenu.add_command(label='Delete Question', command=delete_selection)
filemenu.add_command(label='Start 1 person Quiz', command=display_question)
filemenu.add_command(label='View List of Questions', command=question_frame)
filemenu.add_command(label='Search Question', command=search_frame)

# choice entry to be used by multiple functions/frames
choice = Entry(window, textvariable=answer_choice)

# submit to be used by multiple functions/frames
submit_button = Button(window, command=save_data, text='Submit')
search_button = Button(window,command=search_string, text='Search')

edit_question_Button = Button(select_question_frame,command=add_question,text='Edit Question')
delete_button = Button(select_question_frame,command=delete_question, text='Delete')

# run main gui
window.mainloop()
