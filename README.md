# leetcode-bot

## Setup

Install
* Heroku CLI 7.62.0
* Python 3.10.6
* PostgreSQL 12.11
* Ubuntu 20.04.1
* Poetry

Create a `.env` file
```
export ZULIP_EMAIL=leetcode-test-bot@recurse.zulipchat.com
export ZULIP_API_KEY=<API_KEY>
export ZULIP_SITE=https://recurse.zulipchat.com
```

Generate requirements.txt
```
poetry export -f requirements.txt --output requirements.txt
```

## Run
Send 1 message
```
heroku run python main.py
```