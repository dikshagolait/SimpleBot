from rasa_nlu.model import Metadata, Interpreter
import json

def pprint(o):
 # small helper to make dict dumps a bit prettier
    print(json.dumps(o, indent=2))

interpreter = Interpreter.load('./models/current/nlu')

for x in range(100):
    text = input("Enter string to parse:")
    pprint(interpreter.parse(text))