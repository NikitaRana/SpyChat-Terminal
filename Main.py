# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                             Import packages and python modules
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Spy_details import Spy, spy, STATUS_MESSAGE, friends, ChatMessage,Image
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
import csv
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                            Function to add a status or update a status
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_status_message():

    # to check if the current status message has been set or not
    if spy.current_status_message is not None :
        print("Your current status is"+spy.current_status_message+"\n")
    else:
        print("You don't have any status message currently \n")
    default_value = raw_input("Would you like to set from your older statuses? (Y/N)")

    #The user will add a new status
    if default_value.upper()=='N':
        new_status_message = raw_input("What status message do you want to set")
        if len(new_status_message)>0:
            updated_status_message = new_status_message
            STATUS_MESSAGE.append(updated_status_message)
            print(STATUS_MESSAGE)

    #The user will select from the older statuses
    elif default_value.upper()=='Y':
        item_position = 1

    #Display all the statuses stored in STATUS_MESSAGE list
        for message in STATUS_MESSAGE:
            print(item_position+". "+message)
            item_position = item_position+1
        message_selection = int(raw_input("Choose from the above messages:"))
        if len(STATUS_MESSAGE)>= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1]
    else:
        print("You did not select the correct option. Please select y or n.")

    #if status is updated
    if updated_status_message:
        print("Your updated status message is: %s"%updated_status_message)
    else:
        print("You did not update your current status")

    #updated status message is returned
    return updated_status_message

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                           Function to add a friend
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_friend():
    new_friend = Spy(" "," ",0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age?")
    new_friend.rating = raw_input("Spy rating?")

    #To check the constraints of adding a new friend
    if len ( new_friend.name) > 0 and new_friend.age> 12 and new_friend.rating>= spy.rating:
       if (new_friend.salutation=='ms.' or new_friend.salutation=='mr.' or new_friend.salutation=='Mr.' or new_friend.salutation=='Ms.'):
            friends.append ( new_friend )
            with open ( 'friends.csv', 'a' ) as friends_data:
                writer = csv.writer ( friends_data)
                writer.writerow ( [spy.name, spy.saluation, spy.rating, spy.age, spy.is_online] )
    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len ( friends )

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                           Function to select from a list of spy friends
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def select_friend():
    # indexing the position of a friend
    item_number = 0

    # To select a friend with the indexing
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name, friend.age, friend.rating)

        item_number = item_number + 1

    # Ask the user which friend he want to have a chat with
    friend_choice = raw_input("Choose the index of the friend: ")
    # The friend will be selected
    friend_choice_position = int(friend_choice) - 1

    # Check if the user chooses index out of range
    if friend_choice_position + 1 > len(friends):
        print("Sorry, the selected friend is not present.")
        exit()

    else:
        # returns the selected friend to perform the options
        return friend_choice_position

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for encrypting the message using Caeser Cipher
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def encrypt_caesar(plainText, shift):
  cipherText = ""
  for ch in plainText:
      #if the alphabet is an alphabet
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift
      #if the alphabet is z then return to the starting of the series
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print("Your cipher text is: "+cipherText)
  return cipherText

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for showcasing the encryption menu options
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_encryption_menu(plaintext):
    encypted_words = []
    print("Please select the encryption methods:")
    while show_menu:
        # Taking input choice from the given the set of menu options
        menu_option = int ( raw_input (
            " 1. Encrypt entire text using Ceaser Cipher "
            "\n 2. Encrypt each word in different image file using caeser cipher``") )
        #if user selects caeser ciper for encrypting entire text
        if menu_option == 1:
            return encrypt_caesar(plaintext,3)
        #if user selects word by word ceaser ciper encryption in different images
        elif menu_option == 2:
            #the plain text string is split and converted to a list of substrings
            splitted_text = plaintext.split()
            #looping over each substrings of list
            for word in splitted_text:
                #returning encrypted cipher text of each word to the send_message
                encypted_words = encrypt_caesar(word,3)
            return encypted_words
        else:
            # Choice not selected from the given set of options
            print("Invalid option select from 1 to 2")
            exit ()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for sending the message
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def send_message():
  friend_choice = select_friend()
  ecrypted_words = []
  original_image = raw_input("What is the name of the image?")
  output_image = raw_input("Please name the outfile file : *.jpg")
  text = raw_input("What do you want to say?")
  encrypted_words = show_encryption_menu(text)
  for words in range ( len ( encrypted_words ) ):
    Steganography.encode(original_image, output_image, words)
  new_chat = {
      "message": sender_text,
      "time": datetime.now (),
      "sent_by_me": True
  }
  friends[friend_choice]['chats'].append ( new_chat )
  print "Your secret message is ready!"


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for loading the from the friends
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_friends():
    with open ( 'friends.csv', 'rb' ) as friends_data:
        reader = csv.reader ( friends_data )
        for row in reader:
            spy = Spy (name=row[0], salutation=row[1], rating=float ( row[2] ), age=int ( row[3] ) )
            friends.append ( spy )
            print(friends)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for loading the chats with friends
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_chats():
    with open ( 'chats.csv', 'rb' ) as chats_data:
        reader = csv.reader ( chats_data )
        for row in reader:
            new_chat = ChatMessage (message=row[0], time=row[1], sent_by_me=row[2])
            friends.append ( new_chat )
            print(friends)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for encrypting the message using Caeser Cipher
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decrypt_caesar(cipherText, shift):
  plainText = ""
  for ch in cipherText:
      #if the alphabet is an alphabet
    if ch.isalpha():
      stayInAlphabet = ord(ch) - shift
      #if the alphabet is z then return to the starting of the series
      if stayInAlphabet < ord('a'):
        stayInAlphabet += 26
      finalLetter = chr(stayInAlphabet)
      plainText += finalLetter
  print("Your plain text is: "+plainText)
  return cipherText

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                      Function for reading the message
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def read_message():
    sender = select_friend ()
    output_path = raw_input ( "Please write the name of the file?" )

    # usage of error handling to check if the image contains a hidden text or not
    try:
        secret_text = Steganography.decode ( output_path )
        print("The secret message is ")
        print (secret_text)
        words = secret_text.split ()

        #convert all the words to uppercase and split them
        new_secret_message = (secret_text.upper()).split()

        # calculate the number of words entered by a spy for every message received
        friends[sender].count = friends[sender].count+ len(words)

        #if friends send any emergency words in their message
        if "SOS" in new_secret_message or "SAVE" in new_secret_message or "HELP" in new_secret_message or "RESCUE" in new_secret_message:
            # Emergency alert
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow'))

            # Help your friend by sending him a helping message
            print ( "Your spy friend seems to be in an emergency..")
            print ( "Send him a suitable message")
            print ( "Select that friend to send him a helping message.")

            # Calling the send message help function
            send_emergency_message ()
            # The message is sent successfully
            print( "You have sent a message to help your friend.")

            # Adding the chat with the sender
            new_chat = ChatMessage ( secret_text, False )
            friends[sender].chats.append ( new_chat )

        else:
            # Adding the chat with the sender
            new_chat = ChatMessage ( secret_text, False )
            friends[sender].chats.append ( new_chat )
            print( "Your secret message has been saved!")

        #storing the chat details with each spy
        friends[sender]['chats'].append ( new_chat )

        #storing the chat details with each file to chats.csv
        with open ( 'chats.csv', 'a' ) as chats_data:
            writer = csv.writer ( chats_data )
            #string under the headers: friend, message, time , sent by me(as in the user)
            writer.writerow ( [friends[sender], new_chat.message,new_chat.time,new_chat.sent_by_me] )

        print "Your secret message has been saved!"
        # Print the number of words spoken by your friend
        print("Average words said by"+friends[sender].name+"is"+friends[sender].count)

        # Delete a spy from your list of spies if they are speaking too much
        if len(words) > 100:
            print(friends[sender].name+"removed from the friend\'s list.")
            # Removal of a friend who is speaking way too much
            friends.remove(friends[sender])

    #The image doesnt contain any hidden text
    except TypeError:
        print( "Nothing to decode from the image as it contains no secret message.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Function to read chat history with spy
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def read_chat_history():
    #read_for stores the value returned by select_a_friend()
    read_for = select_friend()

    #iterating through friends chats list
    for chat in friends[read_for].chats:
        if chat.sent_by_me:#when True
            # The date and time is printed
            print(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ","),
            # The message is printed
            print("You said:"+str(chat.message))
        else:#when False
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M","blue"))) + ","),
            # The message is printed in red
            print(colored(str(friends[read_for].name) + " said:","red")),
            # Black color is by default
            print(str(chat.message))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Function to send a message in case of emergency
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to send a message of help in case of an emergency
def send_emergency_message():
    # Select the friend who had sent the emergency message
    friend_choice = select_friend()
    # Send the helping message text to the friend in emergency
    text = "What happended are you alright!! where are you?!?"
    # The message will be added in the chat
    new_chat = ChatMessage(text, True)
    # Add the message to the one who said.
    friends[friend_choice].chats.append(new_chat)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Function to initiate a chat
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start_chat(spy):
    current_status_message = None
    spy.name = spy.salutation + " " + spy.name
    # Age cannot be less than 12 or greater than 50
    if 12 < spy.age < 50:
        # Authentication complete , displaying the spy details
        print"Authentication complete."
        print("Welcome " + str ( spy.name ))
        print("Your age:" + str ( spy.age ))
        print("Your rating:" + str ( spy.rating ))
        print(( "We are happy to have you on board."))
        load_friends()
        load_chats()
    
    while show_menu:

        #Taking input choice from the given the set of menu options
        menu_option = int ( raw_input (
            "What would you like to do "
            "\n 1. Add a status update "
            "\n 2. Add a friend "
            "\n 3. Send a secret message "
            "\n 4. Read a secret message "
            "\n 5. Read chats from a user "
            "\n 6. Close the application" ) )

        if menu_option == 1:
            # Set status update
            current_status_message = add_status_message ()

        elif menu_option == 2:
            # Adding new friends
            number_of_spy_friends = add_friend ()
            print("You have a total of %d spy friends"%(number_of_spy_friends))

        elif menu_option == 3:
            # Sending a secret message
            print("Send a secret message initiated......")
            send_message()

        elif menu_option == 4:
            # Reading a secret message
            print("Read a secret message initiated......")
            read_message()

        elif menu_option == 5:
            # Reading the chat history
            print("Reading chat from user")
            read_chat_history()

        elif menu_option == 6:
            # Closing the menu options
            print("Exiting now.....")
            show_menu = False

        else:
            # Choice not selected from the given set of options
            print("Invalid option select from 1 to 6")
            exit()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                       Code for continuing as a new user
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Hi!%s. %s"%(spy.salutation,spy.name))
user_option = raw_input (
    "Would you like to continue as a default user (default) or create your own (new)? " )  # type of user

# if user creates a new spy entry
if user_option == "new":
    spy = Spy(" ", "",0,0.0)
    spy.name = raw_input ( "Welcome to SpyChat, you must tell me you Spyname first:" )

    # to calculate the length of the string
    if len ( spy.name ) > 0 and spy.name.isdigit()== False:
        #asking for salutation
        print('Welcome ' + spy.name + ' Glad to have you with us.')
        if len(spy.salutation)>0:
            spy.salutation = raw_input ( "What should I call you Mr. or Ms. ?" )
            print('Alright ' + spy.salutation + '.' + spy.name + ' I\'d like to know a little bit more about you before we proceed')

            # asking for the age of spy
            spy.age = int ( input ( 'What is your age? ' ) )  # age of the spy
            if len(spy.age)>0:
                if spy.age > 12 and spy.age < 50:

                    # asking for spy rating
                    spy.rating = float ( raw_input ( 'What is your spy rating? ' ) )
                    if len(spy.rating)>0.0:
                        if spy.rating > 4.5:
                            print('Great Ace!')
                        elif spy.rating > 3.5 and spy.rating <= 4.5:
                            print('You are one of the good ones.')
                        elif spy.rating >= 2.5 and spy.rating <= 3.5:
                            print('You can always do better')
                        else:
                            print('We can always use somebody to help in the office. ')
                        spy_is_online = True
                        print('Changing the status of spy from offline to online ' + str (
                            spy_is_online ))  # bool value to string value for concatenation
                        start_chat ( spy )  # calling menu option
                    else:
                        print("Enter a valid spy rating please")
                else:
                    print('Sorry you are not of the correct age to become a spy.')  # entered age is not between 12 and 50
                print(
                        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name + ", Your sp rating is " + str (
                    spy.rating ))  # float value to string value

            print("Please enter a valid age")
        print("Please enter a valid salutation")
    else:
        print('A spy needs to have a valid name. Please try again.')

#if user continues as a default user
elif user_option == 'default':
    start_chat (spy)  # calling menu option

#if user selects neither new or default user
else:
    print("Please select default user or create a new one.")
    exit()
