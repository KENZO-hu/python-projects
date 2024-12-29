from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Step 1: Set up the WebDriver
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed

# Step 2: Go to Google
driver.get("https://www.google.com")
time.sleep(2)

# Step 3: Search for YouTube
search_box = driver.find_element(By.NAME, "q")  # Google's search box
search_box.send_keys("YouTube")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Step 4: Click the YouTube link
youtube_link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube")
youtube_link.click()
time.sleep(3)

# Step 5: Search for "Misaha" on YouTube
search_box = driver.find_element(By.NAME, "search_query")  # YouTube's search bar
search_box.send_keys("Misaha")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Step 6: Click the first video from the Misaha channel
first_video = driver.find_elements(By.ID, "video-title")[0]
first_video.click()

# Wait for a while to watch the video
time.sleep(10)

# Step 7: Close the browser
driver.quit()
