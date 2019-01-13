import wikipedia
import random

def actionGreet(entitiesDict):
    greets = ["Hi!", "Hey!", "Hey there!", "Hi, how are you doing", "Hello there"]
    randomNo = random.randint(0, len(greets) - 1)
    return greets[randomNo]

def actionBye(entitiesDict):
    byes = ["Bye!", "See you soon", "Good talking to you", "Have a nice day!", "Goodbye!"]
    randomNo = random.randint(0, len(byes) - 1)
    return byes[randomNo]
    
def actionAcknowledgeAffirm(entitiesDict):
    ackAffirms = ["Happy to help", "Great!", "Perfect!"]
    randomNo = random.randint(0, len(ackAffirms) - 1)
    return ackAffirms[randomNo]

def actionSearchWiki(entitiesDict):
    if("searchtext" in  entitiesDict):
        queryText = entitiesDict["searchtext"]
        originalSummary = wikipedia.summary(queryText)
        summaryLines = originalSummary.split('. ')

        finalSummary = ''
        summaryLen = 0
        index = 0
        while(summaryLen < 50):
            finalSummary = finalSummary + ' ' +     summaryLines[index]
            summaryLen += len(summaryLines[index])
            index +=1

        finalSummary = finalSummary.strip()
        summaryFound = True if finalSummary else False
        return summaryFound, finalSummary
    else:
        return False, ""


def actionTellJoke(entitiesDict):
    jokesFile = open("Actions/data/jokes.txt","r", encoding="utf8") 
    allJokes = jokesFile.readlines()
    noOfJokes = len(allJokes)/2
    randomNo = random.randint(0, noOfJokes)
    return allJokes[randomNo*2] + allJokes[randomNo*2 + 1] 

def actionIntroduction(entitiesDict):
    intro = ["I am Mustie, a humanoid", "My name is Mustie. I'm a humanoid, built on open sources stack"]
    randomNo = random.randint(0, len(intro) - 1)
    return intro[randomNo]

def actionNotFound(entitiesDict):
    notFoundReplies = ["Sorry I didnt get that", "Sorry, could you try something else", "Sorry, I cant help you in this"]
    randomNo = random.randint(0, len(notFoundReplies) - 1)
    return notFoundReplies[randomNo]

actions = {
    'greet': actionGreet,
    'goodbye': actionBye,
    'thankyou': actionAcknowledgeAffirm,
    'search': actionSearchWiki,
    'affirm': actionAcknowledgeAffirm,
    'joke': actionTellJoke,
    'introduce': actionIntroduction,
    'None': actionNotFound
}