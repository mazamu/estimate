import json

def test():
    mydata=None
    with open('~/课设/backServer/tool/data.json') as f:
        mydata=json.load(f)
    return mydata
    