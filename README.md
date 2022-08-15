# leetcode-bot

## Setup

Install
* Heroku CLI 7.62.0
* Python 3.10.6
* PostgreSQL 12.11
* Ubuntu 20.04.1
* Poetry
* [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler#dyno-hour-costs)

## Build
Generate requirements.txt
```
poetry export -f requirements.txt --output requirements.txt
```

Push config
```
heroku config:set ZULIP_EMAIL=leetcode-test-bot@recurse.zulipchat.com
heroku config:set ZULIP_API_KEY=<API_KEY>
heroku config:set ZULIP_SITE=https://recurse.zulipchat.com
```

## Deploy
```
git push heroku main
```

## Schedule
```
https://dashboard.heroku.com/apps/<APP_NAME>/scheduler
```

## Run
Send 1 message
```
heroku run python main.py
```