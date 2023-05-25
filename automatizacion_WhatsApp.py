import pywhatkit
import time
from pynput.keyboard import Key, Controller

# instantly of Controller()
keyboard = Controller()
# we define the values to enter: I number, message and if we want that the window closes
# the code of the country is defined first
number = "+57123456789" # example 
message = ["hello", "I am name ", "Bye"] # List of messages
try:
    # Sending a message to a contact on WhatsApp
    for i in range(3): # you decide that all the times he wants that it repeats itself and to iterate on the list of messages

    	# it is called to the method sendwhatmsg_instantly () to deposit the corresponding values
    	pywhatkit.sendwhatmsg_instantly(number, message[i], tab_close= False)

    	# Wait for 10 seconds to ensure that the message is sent
    	time.sleep(10)

    	# Use pynput library to simulate the "Enter" key press
    	keyboard.press(Key.enter)
    	keyboard.release(Key.enter)
    	time.sleep(30) # you can choose more time or less

    print("Message sent successfully!")
except Exception as e:
    print(str(e))