from rasa_nlu.model import Metadata, Interpreter
import json

def pprint(o):
    print(json.dumps(o, indent=2))

def getIntent(query):
    interpreter = Interpreter.load('Intents/RasaNLUModel/models/current/nlu')
    modelOutput = interpreter.parse(query)
    entitiesDict = {}
    for entity in modelOutput["entities"]:
        entitiesDict[entity["entity"]] = entity["value"]

    intent = modelOutput["intent"]["name"]
    return intent, entitiesDict

getIntent("Can you get me information about artificial intelligence")