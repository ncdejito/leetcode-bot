import pandas as pd
import arrow
from abc import ABC


class ProblemSet(ABC):
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


class Blind75(ProblemSet):
    def __init__(
        self,
        csv="data/blind75.csv",
        name="Blind 75",
        description="`Blind75` at neetcode.io",
    ):
        self.description = description
        self.problems = pd.read_csv(csv)
        self.covered_problems = []

    def get_problems(self, day=99) -> str:

        ind = day % len(self.problems)

        # get 1 problem from easy
        easy_problems = self.problems.query(
            "Difficulty == 'Easy'"
        ).reset_index()
        # when day exceeds problems available, start again from 1
        easy_ind = day % len(easy_problems)
        easy_problem = easy_problems.loc[[easy_ind]].set_index("index")

        # get 1 problem from medium/hard
        hard_problems = self.problems[
            self.problems["Difficulty"].isin(["Medium", "Hard"])
        ].reset_index()
        # when day exceeds problems available, start again from 1
        hard_ind = day % len(hard_problems)
        hard_problem = hard_problems.loc[[hard_ind]].set_index("index")

        # get 2 problems at a time
        problems = pd.concat([easy_problem, hard_problem], axis=0)
        self.covered_problems += problems.index.tolist()

        # write post
        text = self.description + "\n"
        for _, row in problems.reset_index(drop=True).iterrows():
            text += (
                "1. ("
                + row["Difficulty"]
                + ") ["
                + row["Problem"]
                + "]("
                + row["Link"]
                + ")\n"
            )
        return text


class Enjeck322(ProblemSet):
    def __init__(
        self,
        csv="data/enjeck.csv",
        name="Enjeck's List",
        description="`Enjeck's list`",
    ):

        self.description = description
        self.problems = pd.read_csv(csv)
        self.covered_problems = []

    def get_problems(self, day=99) -> str:
        # cycle through enjeck's zulip posts in order
        dates = self.problems.date.unique().tolist()

        # when day input exceeds days available, start again from 1
        ind = day % len(dates)

        # get problems for dates
        problems = self.problems[self.problems.date == dates[ind]]
        self.covered_problems += problems.index.tolist()

        # write post
        category = problems["Category"].tolist()[0]
        weekday = arrow.utcnow().shift(hours=-4).format("dddd")
        text = (
            self.description
            + "\n"
            + f"Problems for {weekday}, theme is {category}:\n"
        )
        for _, row in problems.reset_index(drop=True).iterrows():
            text += (
                "1. ("
                + row["Difficulty"]
                + ") ["
                + row["Problem"]
                + "]("
                + row["Link"]
                + ")\n"
            )
        return text


problem_sets = [Blind75(), Enjeck322()]
