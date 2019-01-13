#ignore warnings
import warnings
warnings.simplefilter(action='ignore')
from colorama import Fore, Back, Style

import os
import tensorflow as tf
import sys
import time
from Intents.Intents import *
from Actions.Actions import *
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def startConversation():
    #always on
    while True:
        #continue a session unless someone says bye
        print(Style.RESET_ALL)
        print("\n\nNew session started:\n")
        intent = ""
        while (not "bye" in intent):
            
            userInput = input("Listening..\nUser: ")  
            startTime = time.time()
            intent, entitiesDict = getIntent(userInput)

            if intent in actions:
                actionFunction = actions[intent](entitiesDict)
                print("Mustie: " + str(actionFunction))
            else:
                print("Mustie: Sorry couldnt understand that")

            endTime = time.time()
            print(Fore.LIGHTBLACK_EX + "<<Debugging mode: ")
            print("<<intent identified: " + intent)
            print("<<entities identified: " + str(entitiesDict))
            print("<<entities identified: " + str(entitiesDict))
            print("<<time taken to identify: " + str(endTime - startTime) + " seconds")
            print(Style.RESET_ALL)
 
startConversation()
