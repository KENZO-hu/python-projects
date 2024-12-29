import pyautogui
import os
import time
# le contenu de article
article="""The History of Morocco

Morocco, located in the northwestern corner of Africa, has a rich and diverse history that spans thousands of years. The region was originally inhabited by Berbers, also known as Amazigh people, who have lived there for over 5,000 years. 

In the 8th century, Islam was introduced to Morocco by Arab invaders, and the region became part of the Islamic world. The establishment of the Idrisid dynasty in 788 marked the beginning of Morocco's status as an independent state. Over the centuries, Morocco saw the rise and fall of powerful dynasties such as the Almoravids, Almohads, and Saadians, which expanded the country's influence across North Africa and even into Spain.

During the late 19th and early 20th centuries, Morocco came under increasing European influence and became a French protectorate in 1912, while Spain controlled northern and southern regions. After years of resistance and nationalist movements, Morocco regained its independence in 1956.

Today, Morocco is a constitutional monarchy with a rich cultural heritage influenced by Berber, Arab, and European traditions. Its historic cities, such as Marrakech, Fes, and Rabat, and landmarks like the Hassan II Mosque and the ancient Roman ruins of Volubilis, reflect the country's vibrant history."""
# donne le nom de article 
fill_name="History_of_morrocco.txt"
# ouvre notpad
pyautogui.hotkey("win","r")
time.sleep(1)
pyautogui.typewrite("Notepad++",interval=0.1)
pyautogui.press("enter")
time.sleep(2)
# ecrire l'article
pyautogui.typewrite(article,interval=0.05)
time.sleep(1)
# engistrer le dossier
pyautogui.hotkey("ctrl","S")
time.sleep(1)
pyautogui.typewrite(fill_name,interval=0.1)
pyautogui.press("enter")
time.sleep(1)
# quitter notpad
pyautogui.hotkey("alt","f4")
# done 
os.system("Notepad++{fill_name}")