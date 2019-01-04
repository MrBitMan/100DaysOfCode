#!python3
#List to string is a scipt that pastes in a list from the clipboard and converts
#it to an actual string.

import pyperclip #Very useful ! 

 
text = "Hi guys. How is it going ? "
pyperclip.copy(text)   # Copy the joined list back to the clipboard
