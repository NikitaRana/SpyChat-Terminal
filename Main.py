#-------------------------------------------------------------------------------------------------
#                                             MODULE 2 Objectives
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
# Code for lecture 1 of Spychat dated 19th March 2018
#-------------------------------------------------------------------------------------------------
print('Spy Chat')
print('Let\'s get started')
spy_name = raw_input("What is your spy name?") #to store the name of the spy
print('Welcome '+spy_name+'. How are you?')

# to check the datatype of the entered spy name
type(spy_name)

spy_salutation = raw_input("What should I call you Mr. or Ms. ?") #salutation for the spyname
print('Alright '+spy_salutation+'.'+spy_name+' I\'d like to know a little bit more about you...')

#-------------------------------------------------------------------------------------------------
# Code for lecture 2 of Spychat dated 21st March 2018
#-------------------------------------------------------------------------------------------------
spy_is_online = False #status of the spy
user_option = raw_input("Would you like to continue as a default user (default) or create your own (new)? ") #type of user
if user_option == "new":
    spy_name = raw_input("Welcome to SpyChat, you must tell me you Spyname first:" )
    if len ( spy_name ) > 0: #to calculate the length of the string
        print('Welcome ' + spy_name + ' Glad to have you with us.')
        spy_salutation = raw_input ( "What should I call you Mr. or Ms. ?" )
        print('Alright ' + spy_salutation + '.' + spy_name + ' I\'d like to know a little bit more about you before we proceed')
    else:
        print('A spy needs to have a valid name. Please try again.')
    spy_age = int(input('What is your age? ')) #age of the spy
    if spy_age>12 and spy_age<50:
        spy_rating = float(raw_input('What is your spy rating? '))
        if spy_rating>4.5:
            print('Great Ace!')
        elif spy_rating>3.5 and spy_rating<=4.5:
            print('You are one of the good ones.')
        elif spy_rating>=2.5 and spy_rating<=3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office. ')
    else:
    print('Sorry you are not of the correct age to become a spy.') #entered age is not between 12 and 50
    print('Authentication Complete. We are glad to have you with us. Welcome '+spy_salutation+'.'+spy_name+","Having age "+str(spy_age)+".Your spy rating is "+str(spy_rating)) #float value to string value
    spy_is_online = True
    print('Changing the status of spy from offline to online '+str(spy_is_online)) #bool value to string value for concatenation
elif user_option=='default':
    print("import spy_details.py objective not covered yet")
else:
    print("Please select default user or create a new one.")










