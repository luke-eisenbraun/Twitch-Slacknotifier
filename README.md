# Twitch-Slacknotifier
A slack notifier for Twitch written in python

Python3 bot using `requests` for all communication.

# To Run
1. Create a Twitch App to create your clientID and clientSecret.
2. Create a Slack `incoming-webhook`
3. Add the channels you want to be notified on to the config.json
4. Rename the example config to `config.json`

Run using `python twitch_bot.py`

It's suggested to run this on a cron or as a scheduled task.
