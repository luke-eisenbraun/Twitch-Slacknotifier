import json
import requests

configFile = 'config.json'
statusFile = 'twitchStatus.json'

# Load configs
with open(configFile) as f:
    config_json = json.load(f)
    twitch = config_json['twitch']
    slack = config_json['slack']

    # Set Twitch headers
    twitch['headers'] = {
        'Client-ID': twitch['clientID'],
        'Authorization': twitch['clientSecret'],
    }


# Send message to Slack
def sendSlackAlert(response_json, channel):
    logo = json.loads(response_json)['stream']['channel']['logo']
    data = {
        'text': '{0} is streaming: https://www.twitch.tv/{0}'.format(channel)
    }
    response = requests.post(slack['slackHookUrl'], data=json.dumps(data))


# Read old status in from file
# If file doesn't exist return false to seed it
def getOldStatus(channel):
    with open(statusFile) as f:
        try:
            status_json = json.load(f)
            return status_json[channel]
        except:
            return False


# Save current status to file
def updateLiveStatus(channel, isLive):
    with open(statusFile, 'r') as jsonFile:
        # If file doesnt exist continue, we'll write it later
        try:
            status_json = json.load(jsonFile)
        except:
            status_json = {}

    status_json[channel] = isLive

    # Write all values out to file
    with open(statusFile, 'w') as outFile:
        json.dump(status_json, outFile)


# Loop through all watched channels
def checkTwitch():
    for channel in twitch['channels']:
        # Build chanel URL
        baseUrl = twitch['api'] + channel
        checkTwitchChannel(baseUrl, channel)


# Check channel to see if live
def checkTwitchChannel(url, channel):
    response = requests.get(url, headers=twitch['headers'])
    currentStatus = False
    oldStatus = getOldStatus(channel)

    # Response will contain stream info if active else null
    if json.loads(response.text)['stream']:
        if not oldStatus:
            sendSlackAlert(response.text, channel)
        currentStatus = True
    
    # If saved status doesn't match update it
    if oldStatus is not currentStatus:
        updateLiveStatus(channel, currentStatus)


# Main
if __name__ == '__main__':
    checkTwitch()