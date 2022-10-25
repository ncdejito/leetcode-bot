
# leetcode-bot
<img src="assets/leetcode-bot.png" alt="logo" width="100" height="100" align="right"/>

<p>
    <a href="https://github.com/ncdejito/leetcode-bot/graphs/contributors">
    <img src="assets/coverage.svg" alt="coverage" />
    </a>
</p>


Sends problems daily to Recurse Center's Zulip client.

## Scheduling
Currently sending every 10AM ET on ET weekdays.

```
yacron -c /app/crontab.yml &
```

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
1. run pytest

## Other Notes
Heroku app migrated to Fly.io, crontab using yacron