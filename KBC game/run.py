from tkinter import *
import os


def start_game():
    """Function to start the game by running main.py."""
    os.system("python main.py")


# Initialize the root window
root = Tk()
root.geometry("1270x652+0+0")
root.title("KBC - Welcome")

# Load and set the background image
try:
    # Use the correct file path for the converted PNG image
    background_image = PhotoImage(file="Images/kbcimage.png")
    bg_label = Label(root, image=background_image)
    bg_label.place(relwidth=1, relheight=1)  # Make the image fill the screen
except Exception as e:
    print(f"Error loading background image: {e}")
    bg_label = Label(root, bg="black")  # Fallback to a black background
    bg_label.place(relwidth=1, relheight=1)

# Title Label
title_label = Label(
    root,
    text="Welcome to Kaun Banega Crorepati",
    font=("arial", 36, "bold"),
    bg="black",  # Background matches the fallback color of the screen
    fg="gold",
)
title_label.place(relx=0.5, rely=0.1, anchor="center")  # Positioned at the top center

# Start Button
start_button = Button(
    root,
    text="Start Game",
    font=("arial", 24, "bold"),
    bg="gold",
    fg="black",
    activebackground="darkgoldenrod",
    activeforeground="white",
    cursor="hand2",
    command=start_game,
)
start_button.place(relx=0.51, rely=0.62, anchor="center")  # Positioned in the middle

# Exit Button
exit_button = Button(
    root,
    text="Exit",
    font=("arial", 20, "bold"),
    bg="blue",
    fg="white",
    activebackground="darkred",
    activeforeground="white",
    cursor="hand2",
    command=root.quit,
)
exit_button.place(relx=0.51, rely=0.78, anchor="center")  # Positioned below the start button

# Run the main loop
root.mainloop()
