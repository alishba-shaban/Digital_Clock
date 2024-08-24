import tkinter as tk  # Import the tkinter module for GUI applications
from time import strftime  # Import the strftime function to format the time

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")  # Set the title of the window

def time():
    # Get the current time and date in the format 'Hour:Minute:Second AM/PM\nMonth/Day/Year'
    string = strftime('%H:%M:%S %p\n%D')
    
    # Update the label with the current time
    label.config(text=string)
    
    # Call the time function again after 1000 milliseconds (1 second)
    label.after(1000, time)

# Create a label to display the time, with specific font, background, and foreground color
label = tk.Label(root, font=("calibri", 50, 'bold'), background="yellow", foreground="black")

# Pack the label into the window, centered
label.pack(anchor="center")

# Call the time function to initialize the clock
time()

# Run the Tkinter event loop to keep the window open and responsive
root.mainloop()
