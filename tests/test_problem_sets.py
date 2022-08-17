import pytest
from src.problem_sets import problem_sets, Blind75, Enjeck322


def has_content(text):
    return len(text) > 20


def test_get_problems_from_blind75():
    problem_set = Blind75()
    text = problem_set.get_problems(1)
    assert has_content(text)


def test_get_problems_from_enjeck322():
    problem_set = Enjeck322()
    text = problem_set.get_problems(1)
    assert has_content(text)


def test_if_all_batchdays_have_problems():
    for problem_set in problem_sets:

        for batch_day in range(1, 200):
            text = problem_set.get_problems(batch_day)
            assert has_content(text)


def test_if_batch_covers_whole_curriculum():
    for problem_set in problem_sets:
        for batch_day in range(1, 200):
            text = problem_set.get_problems(batch_day)
        not_covered = set(problem_set.problems.index.tolist()).difference(
            set(problem_set.covered_problems)
        )
        assert len(not_covered) == 0


def test_if_beginner_friendly():
    problem_set = Blind75()
    # day1-10 have easy problems
    for batch_day in range(1, 120):
        text = problem_set.get_problems(batch_day)
        assert "easy" in text.lower()


def test_if_problems_change_per_day():
    for problem_set in problem_sets:
        for batch_day in range(1, 11):
            previous_problems = problem_set.get_problems(batch_day)
            current_problems = problem_set.get_problems(batch_day + 1)
            assert previous_problems != current_problems


def test_if_problem_generation_is_deterministic():
    for problem_set in problem_sets:
        run1 = problem_set.get_problems(day=10)
        run2 = problem_set.get_problems(day=10)
        assert run1 == run2
