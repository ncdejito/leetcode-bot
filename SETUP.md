
## Scheduling
Add a job in Heroku Scheduler Dashboard
```
https://dashboard.heroku.com/apps/<APP_NAME>/scheduler
```

Heroku Scheduler is on UTC (i.e. ET + 4 = UTC)

## Setup

Install
* Heroku CLI 7.62.0
* Python 3.10.6
* PostgreSQL 12.11
* Ubuntu 20.04.1
* Poetry
* [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler#dyno-hour-costs)

## Deploy
Push config
```
heroku config:set ZULIP_EMAIL=leetcode-test-bot@recurse.zulipchat.com
heroku config:set ZULIP_API_KEY=<API_KEY>
heroku config:set ZULIP_SITE=https://recurse.zulipchat.com
```

Push changes
```
git push heroku main
```

## Run
Send 1 message
```
heroku run python main.py
```