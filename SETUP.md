
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
* [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler#dyno-hour-costs)

## Development

Push changes
```
heroku login
heroku create # shows GIT_URL_OF_APP
git remote set-url heroku <GIT_URL_OF_APP>
git push heroku main
heroku ps:scale web=1
```

Push config
```
heroku config:set ZULIP_EMAIL=leetcode-test-bot@recurse.zulipchat.com
heroku config:set ZULIP_API_KEY=<API_KEY>
heroku config:set ZULIP_SITE=https://recurse.zulipchat.com
```

Send 1 message
```
# heroku run python main.py
heroku local
```

Install scheduler
```
heroku addons:create scheduler:standard
heroku addons:open scheduler 
# create job then set to daily at 14:00:00 UTC
```

View logs
```
heroku logs --tail
```