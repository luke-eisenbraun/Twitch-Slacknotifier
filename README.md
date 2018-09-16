# Twitch-Slacknotifier
A slack notifier for Twitch written in python

Python3 bot using `requests` for all communication.

# To Run
1. [Register a Twitch app](https://glass.twitch.tv/console/apps/create) to get your clientID.
2. [Create a Slack](https://my.slack.com/apps/A0F7XDUAZ-incoming-webhooks) `incoming-webhook`
3. Add the Twitch channels you want to be notified on to the config.json
4. Rename the example config to `config.json`

Run using `python twitch_bot.py`

It's suggested to run this on a cron or as a scheduled task.
