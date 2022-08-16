import pandas as pd
from abc import ABC


class ProblemSet(ABC):
    def init(self, csv, name, description):
        pass

    def get_problems(self, date=None) -> str:
        return ""


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
