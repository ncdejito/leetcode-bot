# leetcode-bot

Sends problems daily to Recurse Center's Zulip

## Scheduling
Add a job in Heroku Scheduler Dashboard
```
https://dashboard.heroku.com/apps/<APP_NAME>/scheduler
```

Heroku Scheduler is on UTC (i.e. ET + 4 = UTC)

## Custom ProblemSet
1. CSV file of problem sets (see `data/blind75.csv` for example)
* should have columns ["Category","Difficulty","Problem","Link"]
1. Add PSet to `src/problem_sets.py`
```
class CustomProblemSet(ProblemSet):
    def __init__(
        self,
        csv="path/to/file.csv",
        name="Custom",
        description="This is a cool set",
    ):
        self.description = description
        self.problems = pd.read_csv(csv)
        self.covered_problems = []

    def get_problems(self, day=None) -> str:
        return """
`Blind75` at neetcode.io
1. (Easy) [Problem 1](https://link.to.problem)
1. (Medium) [Problem 2](https://link.to.problem)
1. (Hard) [Problem 3](https://link.to.problem)

        """
```

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