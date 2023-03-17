
# leetcode-bot
<img src="assets/leetcode-bot.png" alt="logo" width="100" height="100" align="right"/>

<p>
    <a href="https://github.com/ncdejito/leetcode-bot/graphs/contributors">
    <img src="assets/coverage.svg" alt="coverage" />
    </a>
</p>


Sends problems daily to Recurse Center's Zulip client.

## Scheduling
Currently sending every day at these times:

* RC NY community - ET 09:00
* flyio server - UTC 14:00
* Developer in PH time - UTC+8 22:00

```
yacron -c crontab.yml
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

## Deployment
1. Create .env
```
ZULIP_API_KEY=$(ZULIP_API_KEY)
ZULIP_EMAIL=$(ZULIP_EMAIL)
ZULIP_SITE=$(ZULIP_SITE)
```
2. Load to environment with `source .env`
3. Create flyio app
```
flyctl launch --dockerfile Dockerfile
```

no to all; 
app name: leetcode-bot; 
region for deployment: lax; 
deploy now: N

```
flyctl secrets set --app leetcode-bot ZULIP_API_KEY=$ZULIP_API_KEY ZULIP_EMAIL=$ZULIP_EMAIL ZULIP_SITE=$ZULIP_SITE
```

4. Deploy to flyio
```
flyctl deploy --dockerfile Dockerfile --app leetcode-bot
```