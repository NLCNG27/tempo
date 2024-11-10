import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tempo Timer")
        self.root.geometry("300x200+1400+0")
        self.root.attributes("-topmost", True)

        self.time_left = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.time_frame = tk.Frame(root)
        self.time_frame.pack()

        self.hour_entry = tk.Entry(self.time_frame, width=3)
        self.hour_entry.insert(0, "00")
        self.hour_entry.pack(side=tk.LEFT)

        self.minute_entry = tk.Entry(self.time_frame, width=3)
        self.minute_entry.insert(0, "00")
        self.minute_entry.pack(side=tk.LEFT)

        self.second_entry = tk.Entry(self.time_frame, width=3)
        self.second_entry.insert(0, "00")
        self.second_entry.pack(side=tk.LEFT)

        self.set_button = tk.Button(root, text="Set Time", command=self.set_time)
        self.set_button.pack(pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

    def set_time(self):
        try:
            hours = int(self.hour_entry.get())
            minutes = int(self.minute_entry.get())
            seconds = int(self.second_entry.get())
            self.time_left = hours * 3600 + minutes * 60 + seconds
            self.label.config(text=time.strftime("%H:%M:%S", time.gmtime(self.time_left)))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for hours, minutes, and seconds.")

    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=time.strftime("%H:%M:%S", time.gmtime(self.time_left)))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.running = False
            messagebox.showinfo("Time's up", "The timer has finished!")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()