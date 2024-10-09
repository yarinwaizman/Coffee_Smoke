import tkinter as tk
import winsound
from playsound import playsound

# Create the window
window = tk.Tk()
window.title("Coffee&Smoke")

# Set background color of the window
window.config(bg="gray")

# Create a label to display the time with white text
timer_label = tk.Label(window, text="25:00", font=("Arial", 48), fg="white", bg="gray")
timer_label.pack(pady=20)

# Input fields for work and break times (white text on gray background)
work_time_input = tk.Entry(window, fg="white", bg="gray")
work_time_input.insert(0, "25")  # Default value
work_time_input.pack()

short_break_input = tk.Entry(window, fg="white", bg="gray")
short_break_input.insert(0, "5")  # Default value
short_break_input.pack()

# Global variables for timer control
is_running = False
paused = False
time_remaining = 0
is_work_time = True  # Track whether it's work or break time

# Start the timer
def start_timer():
    global is_running, time_remaining, paused, is_work_time
    if not is_running:  # Only start if not already running
        if is_work_time:
            work_minutes = int(work_time_input.get())
            time_remaining = work_minutes * 60
        else:
            break_minutes = int(short_break_input.get())
            time_remaining = break_minutes * 60
        
        countdown()
        is_running = True
        paused = False

# Pause or resume the timer
def pause_timer():
    global paused
    paused = not paused  # Toggle the paused state

# Reset the timer
def reset_timer():
    global is_running, paused, is_work_time
    is_running = False
    paused = False
    is_work_time = True  # Reset to work time
    timer_label.config(text="25:00")  # Reset to default

# Countdown function using `after` to avoid blocking the UI
def countdown():
    global time_remaining, is_running, is_work_time
    if time_remaining > 0 and not paused:
        mins, secs = divmod(time_remaining, 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")
        time_remaining -= 1
        window.after(1000, countdown)  # Call countdown again after 1 second
    elif time_remaining == 0:
        play_sound()
        if is_work_time:
            timer_label.config(text="Work's Done! Starting Break...")
            is_work_time = False  # Switch to break time
            start_timer()  # Automatically start break
        else:
            timer_label.config(text="Break's Over! Back to Work...")
            is_work_time = True  # Switch to work time
            is_running = False  # Stop timer, user can start again

# Play sound when the timer ends
def play_sound():
    winsound.Beep(1000, 1000)  # (frequency, duration in milliseconds)
    print("Time's Up!")  # Placeholder for sound

# Create Start, Pause/Resume, and Reset buttons with white text and gray background
start_button = tk.Button(window, text="Start", command=start_timer, fg="white", bg="gray")
start_button.pack()

pause_button = tk.Button(window, text="Pause/Resume", command=pause_timer, fg="white", bg="gray")
pause_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset_timer, fg="white", bg="gray")
reset_button.pack()

# Start the Tkinter loop to show the interface
window.mainloop()
