import tkinter as tk
from tkinter import colorchooser
from datetime import datetime
import time
import winsound
import os

# === GLOBALS ===
POMODORO_MINUTES = 25
BREAK_MINUTES = 5
is_running = False
on_break = False
remaining = 0
LOG_FILE = "log.txt"
was_reset = True 

# === SESSION LOGGING ===
def log_session(minutes):
    with open(LOG_FILE, "a") as f:
        now = datetime.now()
        f.write(f"{now.date()} {minutes}\n")

def get_today_minutes():
    total = 0
    if not os.path.exists(LOG_FILE):
        return total
    today = str(datetime.now().date())
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                date_str, min_str = line.strip().split()
                if date_str == today:
                    total += int(min_str)
            except:
                continue
    return total

# === TIMER ===
def start_timer():
    global is_running, remaining, POMODORO_MINUTES, BREAK_MINUTES, was_reset
    if not is_running:
        is_running = True
        if was_reset or remaining == 0:
            try:
                POMODORO_MINUTES = int(focus_entry.get())
                BREAK_MINUTES = int(break_entry.get())
            except ValueError:
                message_label.config(text="Enter valid numbers.")
                is_running = False
                return
            remaining_minutes = BREAK_MINUTES if on_break else POMODORO_MINUTES
            set_remaining(remaining_minutes * 60)
            was_reset = False
        run_timer()

def pause_timer():
    global is_running
    is_running = False

def reset_timer():
    global is_running, on_break, was_reset
    is_running = False
    on_break = False
    was_reset = True
    set_remaining(POMODORO_MINUTES * 60)
    update_display()
    message_label.config(text="Ready to focus?")

def set_remaining(seconds):
    global remaining
    remaining = seconds
    update_display()

def run_timer():
    global remaining, is_running
    if is_running and remaining > 0:
        remaining -= 1
        update_display()
        root.after(1000, run_timer)
    elif remaining == 0 and is_running:
        handle_cycle_complete()

def handle_cycle_complete():
    global on_break, was_reset
    if not on_break:
        log_session(POMODORO_MINUTES)
        on_break = True
        message_label.config(text="Break time! 🍵")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    else:
        on_break = False
        message_label.config(text="Back to focus! 💻")

    was_reset = True 
    update_display()
    start_timer()


# === UI FUNCTIONS ===
def update_display():
    mins = remaining // 60
    secs = remaining % 60
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    today_total = get_today_minutes()
    today_label.config(text=f"Today: {today_total} min")
    update_plant(today_total)

def update_plant(minutes):
    if minutes < 25:
        plant = "🌱"
    elif minutes < 50:
        plant = "🌿"
    elif minutes < 100:
        plant = "🌳"
    else:
        plant = "🌲🌲"
    plant_label.config(text=plant)

def choose_color():
    color = colorchooser.askcolor(title="Choose background color")[1]
    if color:
        root.configure(bg=color)
        for widget in root.winfo_children():
            try:
                widget.configure(bg=color)
                with open("settings.txt", "w") as f:
                    f.write(color)
            except:
                pass
            
# === UI SETUP ===
root = tk.Tk()
root.title("StudyPud 🍮")
root.geometry("320x440")
root.resizable(False, False)

# Input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

focus_label = tk.Label(input_frame, text="Focus (min):")
focus_label.grid(row=0, column=0, padx=5)

focus_entry = tk.Entry(input_frame, width=5)
focus_entry.insert(0, "25")
focus_entry.grid(row=0, column=1, padx=5)

break_label = tk.Label(input_frame, text="Break (min):")
break_label.grid(row=0, column=2, padx=5)

break_entry = tk.Entry(input_frame, width=5)
break_entry.insert(0, "5")
break_entry.grid(row=0, column=3, padx=5)

# Timer and messages
timer_label = tk.Label(root, text="25:00", font=("Courier", 48))
timer_label.pack(pady=20)

message_label = tk.Label(root, text="Ready to focus?", font=("Helvetica", 12))
message_label.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start", command=start_timer, width=8, background="#4CAF50")
start_btn.config(text="Resume" if not was_reset else "Start")
start_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(btn_frame, text="Pause", command=pause_timer, width=8, background="#4CAF50")
pause_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", command=reset_timer, width=8, background="#4CAF50")
reset_btn.grid(row=0, column=2, padx=5)

color_btn = tk.Button(root, text="🎨 Theme", command=choose_color, width=20, background="#4CAF50")
color_btn.pack(side="bottom", pady=10)
# Daily total + plant animation
today_label = tk.Label(root, text="Today: 0 min", font=("Helvetica", 10))
today_label.pack(pady=2)

plant_label = tk.Label(root, text="🌱", font=("Helvetica", 40))
plant_label.pack(pady=20)


try:
    with open("settings.txt", "r") as f:
        saved_color = f.read().strip()
        if saved_color:
            root.configure(bg=saved_color)
            for widget in root.winfo_children():
                try:
                    widget.configure(bg=saved_color)
                except:
                    pass
except FileNotFoundError:
    pass

# Start
set_remaining(POMODORO_MINUTES * 60)
update_display()
root.mainloop()
