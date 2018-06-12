import time
import find_meaning
while True:

    user_input=input("What do you want to be done:")

    try:
        find_meaning.find_meaning(user_input)
        time.sleep(2)
        #print("----------------------------------------------------")
        print("press y for asking again any other button otherwise")
        ask_again=input("Do you want to ask again")
        if ask_again=="y":
            pass
        else:
            break
    except:
        print("Unable to understand")
        time.sleep(2)
        print("----------------------------------------------------")
        print("press y for asking again any other button otherwise")
        ask_again=input("Do you want to ask again")
        if ask_again=="y":
            pass
        else:
            break
