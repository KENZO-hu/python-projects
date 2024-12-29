import os
import pywhatkit
import time
import webbrowser

# Step 1: Write the article into a file
article = """
The History of Morocco

Morocco, located in the northwestern corner of Africa, has a rich and diverse history that spans thousands of years. The region was originally inhabited by Berbers, also known as Amazigh people, who have lived there for over 5,000 years. 

In the 8th century, Islam was introduced to Morocco by Arab invaders, and the region became part of the Islamic world. The establishment of the Idrisid dynasty in 788 marked the beginning of Morocco's status as an independent state. Over the centuries, Morocco saw the rise and fall of powerful dynasties such as the Almoravids, Almohads, and Saadians, which expanded the country's influence across North Africa and even into Spain.

During the late 19th and early 20th centuries, Morocco came under increasing European influence and became a French protectorate in 1912, while Spain controlled northern and southern regions. After years of resistance and nationalist movements, Morocco regained its independence in 1956.

Today, Morocco is a constitutional monarchy with a rich cultural heritage influenced by Berber, Arab, and European traditions. Its historic cities, such as Marrakech, Fes, and Rabat, and landmarks like the Hassan II Mosque and the ancient Roman ruins of Volubilis, reflect the country's vibrant history.
"""

file_name = "History_of_Morocco.txt"

try:
    # Write the article to a file
    with open(file_name, "w") as file:
        file.write(article)
    print(f"File '{file_name}' has been created.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# Step 2: Open WhatsApp Web in the browser
webbrowser.open('https://web.whatsapp.com')
time.sleep(5)  # Wait a moment for WhatsApp Web to load

# Step 3: Send the message via WhatsApp using pywhatkit
phone_number = "+212608618981"# Replace with the correct phone number, including country code
message = article  # Sending the article content directly as a message
# Get the current time and add a 2-minute delay for sending the message
current_time = time.localtime()
send_hour = current_time.tm_hour
send_minute = current_time.tm_min + 2
try:
    # Open WhatsApp Web and schedule the message (2 minutes later)
    pywhatkit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 2)
    print("Message scheduled successfully.")
except Exception as e:
    print(f"An error occurred while sending the message: {e}")

# Optional: Delete the file if it was created temporarily
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"Temporary file '{file_name}' deleted.")

