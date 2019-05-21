import datetime
import calendar
import webbrowser
import time
count_yes=0
count_no=0
questions=["why?","what?","where?","when?","who?","how?"]
Help="Arithmetic Calculations can be performed here.provide space between operand and operator while typing. Begin with open keyword to open any application specifying it.For example open calendar,open google.com"
print()
print("##############################################################")
print("                        SMVBOT                                ")
print("##############################################################")
print(Help)
print("##############################################################")
print()
print("Type something...")
while True:
    print("-->",end="")
    chat=input().casefold()
    if("hi" in chat or "hello" in chat):
        print("Hi! Please go on. What do you want me to do?")
    elif("name" in chat):
        print("I do no care about names! Please continue.")
    elif("time" in chat and "now" in chat):
        print(datetime.datetime.now(),"is the current date and time")
    elif("exit" in chat or "bye" in chat):
        print("Goodbye. It was nice talking to you. I am looking forward to our next session.")
        break
    elif("+" in chat or "*" in chat or "-" in chat or "/" in chat):
        if(" " not in chat):
            print("syntax error! provide space between operand and operator.")
        elif(any(c.isalpha() for c in chat)):
            print("operator symbols with sentences do not convey any meaning!")
        else:    
            exp=chat.split(" ")
            try:
                if(exp[2]!=0):
                    print(eval(chat))
            except ZeroDivisionError:
                print("Division by zero Error!")
    elif("yes" in chat or "yeah" in chat):
        count_yes+=1
        if(count_yes>4):
            print("You seem to be quite positive.")
        else:
            print("I understand.")
    elif(chat=="no" or "nope" in chat):
        count_no+=1
        if(count_no>4):
            print("You seem to be quite negative.")
        else:
            print("okay!")
    elif("kill" in chat or "murder" in chat):
        print("Do you always talk like this?")
    elif("thanks" in chat or "thank" in chat):
        print("You are Welcome.")
    elif("calendar" in chat):
        print("CALENDAR")
        year=int(input("Enter year(YYYY):"))
        month=int(input("Enter month(MM):"))
        print(calendar.month(year, month))
    elif("how are you?" in chat):
        print("Fine.")
    elif("you" in chat and "doing" in chat):
        print("Talking to you.")
    elif("you" in chat and "like" in chat):
        print("I like chatting!")
    elif(chat=="okay" or "oh" in chat or chat=="ok"):
        print("yes. please continue.")
    elif("open" in chat):
        string=chat.split(" ")
        if("google" in string[1]):
            webbrowser.open("http://google.com")
        elif("youtube" in string[1]):
            webbrowser.open('http://youtube.com')
        else:
            webbrowser.open(string[1])
    elif("help" in chat):
        print(Help)

    elif("boredom" in chat or "bored" in chat or "facts" in chat):
        print("Reading facts is one of the ways for kicking out boredom! Here they are! Go for it!")
        print("LOADING...",end=" ")
        time.sleep(2)
        print("...")
        time.sleep(5)
        webbrowser.open('http://scoopwhoop.com/30-Amazing-Facts-From-Around-The-World-That-You-Wont-Believe-Are-True/#.m93entpyj')
    elif(chat in questions):
        print("Have you asked anyone else?")
    elif("sleepy" in chat or "sleep" in chat or "sleeping" in chat):
        print("Be brisk! Talk to me.")
    elif("tired" in chat or "good night" in chat):
        print("Take rest. Sweet dreams. Good night!")
    elif("you" in chat and "good" in chat):
        print("You do not want me to be good! Eh?")
    elif("haha" in chat):
        print("Why are you laughing?")
    elif("like" in chat and "that" in chat):
        print("Okay!")
    elif("you" in chat and "see" in chat):
        print("Why do you care about what I am seeing!")
    elif("love" in chat and "you" in chat):
        print("But I hate you!")
    elif(len(chat.split())==3 and "what" in chat):
        print("Okay! Collecting results...")
        webbrowser.open(chat.split()[2]+'')
    elif("you" in chat and "not" in chat and "understand" in chat):
        print("Do ask about me!")
    elif ("intelligent" in chat or "nice" in chat or "good" in chat):
        print("Thanks!")
    elif "sorry" in chat:
        print("It is okay!")
    else:
        print("I do not understand what you are speaking!")
