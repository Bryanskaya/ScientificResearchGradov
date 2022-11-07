import json

fileName = "results.json"


def writeData(dataDict):
    with open(fileName, 'w') as f:
        json.dump(dataDict, f, indent=4, separators=(',', ': '))


def loadData():
    try:
        with open(fileName, "r") as f:
            data = json.load(f)
    except:
        data = {}
    return data
