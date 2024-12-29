import pyautogui
import time
import os

# Step 1: Open Chrome
os.system("start chrome")  # Launch Chrome
time.sleep(5)  # Wait for Chrome to load

# Step 2: Move to the search bar and click
# Find the approximate position of the search bar (adjust based on your screen resolution)
pyautogui.click(x=400, y=80)  # Adjust coordinates as needed
time.sleep(1)

# Step 3: Type "YouTube" and press Enter
pyautogui.typewrite("YouTube")
pyautogui.press("enter")
time.sleep(5)  # Wait for YouTube to load

# Step 4: Move to the YouTube search bar and click
# Find the position of the YouTube search bar
pyautogui.click(x=600, y=150)  # Adjust coordinates as needed
time.sleep(1)

# Step 5: Type "Misaha" and press Enter
pyautogui.typewrite("Misaha")
pyautogui.press("enter")
time.sleep(5)  # Wait for the search results to load

# Step 6: Click the first video
# Find the position of the first video (adjust based on your screen resolution)
pyautogui.click(x=300, y=400)  # Adjust coordinates as needed
time.sleep(10)  # Watch the video for 10 seconds

# Done
print("Process completed!")
