import requests
import json
import time

def getCurrentEpoch():
    return round(time.time())

def getRecentScrobbleCount(username, api_key, startEpoch, endEpoch):
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={username}&api_key={api_key}&format=json&from={startEpoch}&page=1&to={endEpoch}"
    response = requests.request("GET", url)

    jsonFormat = json.loads(response.text)
    return jsonFormat['toptracks']['@attr']['total']
    
print(getRecentScrobbleCount('tjallo', '06199ca5111af01e6844cabe763ebf87', '1582239600', getCurrentEpoch()))