import pandas as pd
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
        self.problems = (
            pd.read_csv(csv)
            .sample(frac=1, random_state=42)
            .reset_index(drop=True)
        )
        self.covered_problems = []

    def get_problems(self, day=99) -> str:
        # when day exceeds problems available, start again from 1
        ind = day % len(self.problems)
        # get 2 problems at a time
        problems = self.problems.loc[2 * (ind - 1) : 2 * (ind - 1) + 1, :]
        self.covered_problems += problems.index.tolist()
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
        dates = self.problems.date.unique().tolist()
        # when day exceeds problems available, start again from 1
        ind = day % len(dates)
        problems = self.problems[self.problems.date == dates[ind]]
        self.covered_problems += problems.index.tolist()
        category = problems["Category"].tolist()[0]
        text = self.description + "\n" + f"Theme is {category}:\n"
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
