#------------------------------------------------------------------------------------
#  The Spy_details.py file is meant for a Default user and shall be imported when the
# user is given the option to continue as a default user or create a new spy user.
#------------------------------------------------------------------------------------
from datetime import datetime
class Spy:

        def __init__(self, name, salutation, age, rating):
                self.name = name
                self.salutation = salutation
                self.age = age
                self.rating = rating
                self.is_online = True
                self.chats = []
                self.current_status_message = None
class ChatMessage():
        def __init__(self, message, time, sent_by_me):
                self.message = message
                self.time = datetime.now()
                self.sent_by_me = sent_by_me
spy = Spy('Nikita', 'Ms.', 20, 4.7)

