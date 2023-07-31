import json, unittest, datetime

# loading the json files:
with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):

    result = {}
    result["deviceID"] = jsonObject["deviceID"]
    result["deviceType"] = jsonObject["deviceType"]
    result["timestamp"] = jsonObject["timestamp"]

    # converting the location object:
    getLocationObject = jsonObject["location"].split("/")
    location = {
        "country": getLocationObject[0],
        "city": getLocationObject[1],
        "area": getLocationObject[2],
        "factory": getLocationObject[3],
        "section": getLocationObject[4],
    }
    result["location"] = location

    # converting data object:
    data = {"status": jsonObject["operationStatus"], "temperature": jsonObject["temp"]}
    result["data"] = data

    return result


def convertFromFormat2(jsonObject):
    result = {}
    result["deviceID"] = jsonObject["device"]["id"]
    result["deviceType"] = jsonObject["device"]["type"]
    # converting timestamp to epoch millisec:
    timestamp_str = jsonObject["timestamp"]
    timestamp_obj = datetime.datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp_ms = int(timestamp_obj.timestamp() * 1000)
    result["timestamp"] = timestamp_ms
    # converting the location array:
    location = {
        "country": jsonObject["country"],
        "city": jsonObject["city"],
        "area": jsonObject["area"],
        "factory": jsonObject["factory"],
        "section": jsonObject["section"],
    }
    result["location"] = location
    # converting the data array:
    data = {
        "status": jsonObject["data"]["status"],
        "temperature": jsonObject["data"]["temperature"],
    }
    result["data"] = data

    return result


def main(jsonObject):
    result = {}
    if jsonObject.get("device") == None:
        result = convertFromFormat1(jsonObject)

    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, "Converting from Type 1 failed")

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, "Converting from Type 2 failed")

    if __name__ == "__main__":
        unittest.main()
