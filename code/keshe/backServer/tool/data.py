import json

def test():
    mydata=None
    with open('~/keshe/backServer/tool/data.json') as f:
        mydata=json.load(f)
    return mydata
    