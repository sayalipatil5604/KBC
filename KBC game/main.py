from tkinter import *

from tkinter.ttk import Progressbar

from pygame import mixer

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
mixer.init()
mixer.music.load("MP3\\kbc.mp3")
mixer.music.play(-1)

# Initialize global timer_running flag and the timerLabel
timer_running = True # Global flag to track if the timer is running
current_timer_id = None
# Function to start the timer
def start_timer():
    global timer_running, current_timer_id

    if timer_running:  # Prevent multiple timers from running simultaneously
        return

    timer_running = True

    def countdown(time_left):
        if time_left > 0:
            global timer_running, current_timer_id
        if time_left > 0:
            timerLabel.config(text=str(time_left))  # Update the label with the time left
            current_timer_id = root.after(1000, countdown, time_left - 1)  # Schedule the next countdown
        else:
            timerLabel.config(text="Time's up!")
            timer_running = False
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                # Reset lifeline buttons and restart the game
                global timer_running
                timer_running = False
                reset_timer()
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])

                # Reset options and amount for the first question
                optionButton1.config(text=first_option[0], bg="black", fg="white")
                optionButton2.config(text=second_option[0], bg="black", fg="white")
                optionButton3.config(text=third_option[0], bg="black", fg="white")
                optionButton4.config(text=fourth_option[0], bg="black", fg="white")

                amountLabel.config(image=amountimage)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black")
            #root1.attributes("-fullscreen",True)
            root1.geometry("1270x652+0+50")
            root1.title("You won 0 pounds")
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(
                root1,
                text="You Lose",
                font=("arial", 40, "bold"),
                bg="black",
                fg="white",
            )
            loseLabel.pack()

            tryagainButton = Button(
                root1,
                text="Try Again",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                activeforeground="white",
                cursor="hand2",
                command=tryagain,
            )
            tryagainButton.pack()

            closeButton = Button(
                root1,
                text="Close",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                activeforeground="white",
                cursor="hand2",
                command=close,
            )
            closeButton.pack()

            sadimage = PhotoImage(file="Images\\sad.png")
            sadLabel = Label(root1, image=sadimage, bg="black")
            sadLabel.place(x=800, y=280)

            sadLabel1 = Label(root1, image=sadimage, bg="black")
            sadLabel1.place(x=400, y=280)
            root1.mainloop()

            timer_running = False  # Reset the timer running flag

    countdown(60)  # Start countdown from 60 seconds

# Reset the timer (call this function after each question)
def reset_timer():
    global timer_running, current_timer_id
    timer_running = False  # Stop the current timer logic
    if current_timer_id:
        root.after_cancel(current_timer_id)  # Cancel the current timer
        current_timer_id = None  # Clear the timer reference
    timerLabel.config(text="60")  # Reset the timer label
    start_timer()  # Start a fresh timer

# Function to be called when a user selects an answer
def select(event):
    # Reset button colors before proceeding with the new question
    optionButton1.config(bg="black", fg="white")
    optionButton2.config(bg="black", fg="white")
    optionButton3.config(bg="black", fg="white")
    optionButton4.config(bg="black", fg="white")

    # Hide the progress bars and labels for the lifelines
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()

    # Get the selected button and its value
    b = event.widget
    value = b["text"]

    # Check if the selected answer is correct
    for i in range(15):
        if value == correct_answers[i]:
            # Highlight the correct answer in green
            b.config(bg="green", fg="white")

            # Schedule the next question after a delay of 2 seconds
            def move_to_next_question():
                # Clear the current question and show the next one
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[i + 1])
                reset_timer()  # Reset the timer before showing the next question
                # Update options for the next question
                optionButton1.config(text=first_option[i + 1], bg="black", fg="white")
                optionButton2.config(text=second_option[i + 1], bg="black", fg="white")
                optionButton3.config(text=third_option[i + 1], bg="black", fg="white")
                optionButton4.config(text=fourth_option[i + 1], bg="black", fg="white")

                # Update the amount label for the new question
                amountLabel.config(image=amountImages[i + 1])

            # Use the after method to delay the transition
            root.after(1000, move_to_next_question)  # 2 seconds delay
            return  # Exit the loop after processing the correct answer

        # Handle incorrect answer logic (highlight the selected wrong option in red)
        if value not in correct_answers:
            # Highlight the wrong answer in red
            if b == optionButton1:
                optionButton1.config(bg="red", fg="white")
            elif b == optionButton2:
                optionButton2.config(bg="red", fg="white")
            elif b == optionButton3:
                optionButton3.config(bg="red", fg="white")
            elif b == optionButton4:
                optionButton4.config(bg="red", fg="white")

            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])

                # Reset options and amount for the first question
                optionButton1.config(text=first_option[0], bg="black", fg="white")
                optionButton2.config(text=second_option[0], bg="black", fg="white")
                optionButton3.config(text=third_option[0], bg="black", fg="white")
                optionButton4.config(text=fourth_option[0], bg="black", fg="white")

                amountLabel.config(image=amountimage)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black")
            root1.geometry("1270x652+0+30")
            root1.title("You won 0 pounds")
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(
                root1,
                text="You Lose",
                font=("arial", 40, "bold"),
                bg="black",
                fg="white",
            )
            loseLabel.pack()

            tryagainButton = Button(
                root1,
                text="Try Again",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                activeforeground="white",
                cursor="hand2",
                command=tryagain,
            )
            tryagainButton.pack()

            closeButton = Button(
                root1,
                text="Close",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                activeforeground="white",
                cursor="hand2",
                command=close,
            )
            closeButton.pack()

            sadimage = PhotoImage(file="Images\\sad.png")
            sadLabel = Label(root1, image=sadimage, bg="black")
            sadLabel.place(x=800, y=280)

            sadLabel1 = Label(root1, image=sadimage, bg="black")
            sadLabel1.place(x=400, y=280)
            root1.mainloop()

            break

def lifeline50():
    lifeline50Button.config(image=image50X, state=DISABLED)
    if questionArea.get(1.0, "end-1c") == questions[0]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[1]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[2]:
        optionButton4.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[3]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[4]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[5]:
        optionButton2.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[6]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[7]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[8]:
        optionButton1.config(text="")
        optionButton2.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[9]:
        optionButton1.config(text="")
        optionButton2.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[10]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[11]:
        optionButton1.config(text="")
        optionButton2.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[12]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[13]:
        optionButton1.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0, "end-1c") == questions[14]:
        optionButton1.config(text="")
        optionButton4.config(text="")


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, "end-1c") == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, "end-1c") == questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=50)

    if questionArea.get(1.0, "end-1c") == questions[2]:
        progressbarA.config(value=80)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=30)

    if questionArea.get(1.0, "end-1c") == questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)

    if questionArea.get(1.0, "end-1c") == questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=50)

    if questionArea.get(1.0, "end-1c") == questions[5]:
        progressbarA.config(value=80)
        progressbarB.config(value=10)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, "end-1c") == questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=50)

    if questionArea.get(1.0, "end-1c") == questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=60)
        progressbarD.config(value=20)

    if questionArea.get(1.0, "end-1c") == questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=40)

    if questionArea.get(1.0, "end-1c") == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=70)

    if questionArea.get(1.0, "end-1c") == questions[10]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=50)
        progressbarD.config(value=80)

    if questionArea.get(1.0, "end-1c") == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=40)
        progressbarC.config(value=90)
        progressbarD.config(value=50)

    if questionArea.get(1.0, "end-1c") == questions[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=80)
        progressbarD.config(value=60)

    if questionArea.get(1.0, "end-1c") == questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=80)
        progressbarD.config(value=20)

    if questionArea.get(1.0, "end-1c") == questions[14]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)


def phoneLifeline():
    mixer.music.load("MP3\\calling.mp3")
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifelineButton.config(image=phoneImageX, state=DISABLED)


def phoneclick():
    for i in range(15):
        if questionArea.get(1.0, "end-1c") == questions[i]:
            engine.say(f"The answer is{correct_answers[i]}")
            engine.runAndWait()

correct_answers = [
    "Russia",
    "366",
    "Heron",
    "Dollar",
    "Python",
    "36",
    "Linux",
    "Lion",
    "7:23PM",
    "MI",
    "Jupiter",
    "7",
    "1000 years",
    "Apple",
    "Bill Gates",
]

questions = [
    "1) Which is the largest country in the world?",
    "2) How many days are there in a leap year?",
    "3) Which one of these four birds has the longest beak and feet?",
    "4) What is the national currency of the United States of America(USA)?",
    "5) Guido van Rossum in 1991 designed which language?",
    "6) Finish the sequence:9,18,27,_?",
    "7) Which one is the first fully supported 64-bit operating system?",
    "8) Which animal is called the king of the jungle?",
    "9) What time corresponds to 23:23 hours ?",
    "10) Which team has won most number of IPL matches?",
    "11) Which is the largest planet in our Solar system?",
    "12) How many continents are there in the world?",
    "13) How many years are there in one Millenium?",
    "14) ipad is manufactured by?",
    "15) Who founded Microsoft?",
]

first_option = [
    "India",
    "354",
    "Heron",
    "Euro",
    "Javascript",
    "36",
    "Windows 7",
    "Elephant",
    "11:23PM",
    "KKR",
    "Earth",
    "8",
    "100 years",
    "Google",
    "Monty Ritz",
]

second_option = [
    "USA",
    "366",
    "Parrot",
    "Peso",
    "Python",
    "34",
    "Linux",
    "Lion",
    "11:11PM",
    "CSK",
    "Uranus",
    "5",
    "50 years",
    "Microsoft",
    "Danis Lio",
]

third_option = [
    "China",
    "365",
    "Crow",
    "Dollar",
    "Java",
    "30",
    "Mac",
    "Tiger",
    "7:23PM",
    "MI",
    "Mars",
    "7",
    "500 years",
    "Amazon",
    "Bill Gates",
]

fourth_option = [
    "Russia",
    "420",
    "Pigeon",
    "Yen",
    "C++",
    "37",
    "Windows XP",
    "cow",
    "9:11PM",
    "RCB",
    "Jupiter",
    "6",
    "1000 years",
    "Apple",
    "Jeff Bezos",
]

# Initialize root window
root = Tk()
root.geometry("1270x652+0+0")  # Set window size
root.title("KBC")  # Set window title
root.config(bg="black")  # Set background color

# Left Frame for Lifelines, Logo, and Layout
leftframe = Frame(root, bg="black", padx=90)
leftframe.grid(row=0, column=0, rowspan=2)

# Top Frame for Lifeline Buttons (inside leftframe)
topLifelineFrame = Frame(leftframe, bg="black", pady=20)
topLifelineFrame.grid(row=0, column=0)

# Lifeline Buttons
image50 = PhotoImage(file="Images\\50-50.png")
image50X = PhotoImage(file="Images\\50-50-X.png")

lifeline50Button = Button(
    topLifelineFrame,
    image=image50,
    bg="black",
    bd=0,
    activebackground="black",
    width=180,
    height=80,
    command=lifeline50,
)
lifeline50Button.grid(row=0, column=0, padx=10)

audiencePole = PhotoImage(file="Images\\audiencePole.png")

audiencePoleX = PhotoImage(file="Images\\audiencePoleX.png")

audiencePoleButton = Button(
    topLifelineFrame,
    image=audiencePole,
    bg="black",
    bd=0,
    activebackground="black",
    width=180,
    height=80,
    command=audiencePoleLifeline,
)
audiencePoleButton.grid(row=0, column=1, padx=10)

phoneImage = PhotoImage(file="Images\\phoneAFriend.png")
phoneImageX = PhotoImage(file="Images\\phoneAFriendX.png")
phoneLifelineButton = Button(
    topLifelineFrame,
    image=phoneImage,
    bg="black",
    bd=0,
    activebackground="black",
    width=180,
    height=80,
    command=phoneLifeline,
)
phoneLifelineButton.grid(row=0, column=2, padx=10)

callimage = PhotoImage(file="Images\\phone.png")
callButton = Button(
    root,
    image=callimage,
    bd=0,
    bg="black",
    activebackground="black",
    cursor="hand2",
    command=phoneclick,
)
# Center Frame for Logo
centerFrame = Frame(leftframe, bg="black", pady=20)
centerFrame.grid(row=1, column=0)

centerImage = PhotoImage(file="Images\\center.png")
logoLabel = Label(centerFrame, image=centerImage, bg="black", width=300, height=200)
logoLabel.grid(row=0, column=0)


bottomFrame = Frame(leftframe, bg="black", pady=10)
bottomFrame.grid(row=2, column=0)

# Right Frame for Amount Display
rightframe = Frame(root, pady=25, padx=50, bg="black")
rightframe.grid(row=0, column=1, rowspan=2)

amountimage = PhotoImage(file="Images\\Picture0.png")
amountimage1 = PhotoImage(file="Images\\Picture1.png")
amountimage2 = PhotoImage(file="Images\\Picture1.png")
amountimage3 = PhotoImage(file="Images\\Picture2.png")
amountimage4 = PhotoImage(file="Images\\Picture3.png")
amountimage5 = PhotoImage(file="Images\\Picture4.png")
amountimage6 = PhotoImage(file="Images\\Picture5.png")
amountimage7 = PhotoImage(file="Images\\Picture6.png")
amountimage8 = PhotoImage(file="Images\\Picture7.png")
amountimage9 = PhotoImage(file="Images\\Picture8.png")
amountimage10 = PhotoImage(file="Images\\Picture9.png")
amountimage11 = PhotoImage(file="Images\\Picture10.png")
amountimage12 = PhotoImage(file="Images\\Picture11.png")
amountimage13 = PhotoImage(file="Images\\Picture12.png")
amountimage14 = PhotoImage(file="Images\\Picture13.png")
amountimage15 = PhotoImage(file="Images\\Picture14.png")

amountImages = [
    amountimage1,
    amountimage2,
    amountimage3,
    amountimage4,
    amountimage5,
    amountimage6,
    amountimage7,
    amountimage8,
    amountimage9,
    amountimage10,
    amountimage11,
    amountimage12,
    amountimage13,
    amountimage14,
    amountimage15,
]

amountLabel = Label(rightframe, image=amountimage, bg="black")
amountLabel.grid(row=0, column=0)

layoutImage = PhotoImage(file="Images\\lay.png")
layoutLabel = Label(bottomFrame, image=layoutImage, bg="black")
layoutLabel.grid(row=0, column=0, pady=10)

# Question Area
questionArea = Text(
    bottomFrame,
    font=("arial", 18, "bold"),
    width=34,
    height=2,
    wrap="word",
    bg="black",
    fg="white",
    bd=0,
)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])

labelA = Label(
    bottomFrame, text="A:", bg="black", fg="white", font=("arial", 16, "bold")
)
labelA.place(x=60, y=110)
optionButton1 = Button(
    bottomFrame,
    text=first_option[0],
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    bd=0,
    activebackground="black",
    activeforeground="white",
    cursor="hand2",
)
optionButton1.place(x=100, y=100)

labelB = Label(
    bottomFrame, text="B:", bg="black", fg="white", font=("arial", 16, "bold")
)
labelB.place(x=330, y=110)
optionButton2 = Button(
    bottomFrame,
    text=second_option[0],
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    bd=0,
    activebackground="black",
    activeforeground="white",
    cursor="hand2",
)
optionButton2.place(x=370, y=100)

labelC = Label(
    bottomFrame, text="C:", bg="black", fg="white", font=("arial", 16, "bold")
)
labelC.place(x=60, y=190)
optionButton3 = Button(
    bottomFrame,
    text=third_option[0],
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    bd=0,
    activebackground="black",
    activeforeground="white",
    cursor="hand2",
)
optionButton3.place(x=100, y=180)

labelD = Label(
    bottomFrame, text="D:", bg="black", fg="white", font=("arial", 16, "bold")
)
labelD.place(x=330, y=190)
optionButton4 = Button(
    bottomFrame,
    text=fourth_option[0],
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    bd=0,
    activebackground="black",
    activeforeground="white",
    cursor="hand2",
)
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

progressbarLabelA = Label(
    root, text="A", font=("arial", 20, "bold"), bg="black", fg="white"
)
progressbarLabelB = Label(
    root, text="B", font=("arial", 20, "bold"), bg="black", fg="white"
)
progressbarLabelC = Label(
    root, text="C", font=("arial", 20, "bold"), bg="black", fg="white"
)
progressbarLabelD = Label(
    root, text="D", font=("arial", 20, "bold"), bg="black", fg="white"
)
timerLabel = Label(root, text="60", font=("arial", 24, "bold"), bg="black", fg="white")
timerLabel.place(x=375, y=350)

optionButton1.bind("<Button-1>", select)
optionButton2.bind("<Button-1>", select)
optionButton3.bind("<Button-1>", select)
optionButton4.bind("<Button-1>", select)

# Run the main loop
root.mainloop()