import pytest
from src.zulip_comms import get_client, get_posts, send, no_duplicate_posts
from src.problem_sets import Blind75


client = get_client()


def test_get_posts():
    results = get_posts(num_before=1, client=client, _from="staging")
    assert len(results) > 0


def test_send():
    send("test send", client, to="staging")

    recs = get_posts(num_before=1, client=client, _from="staging")

    text = recs[-1]  # latest

    assert text == "test send"


def test_has_duplicate_posts():
    problem_set = Blind75()
    post = problem_set.get_problems(day=1)

    send(post, client, to="staging")

    has_no_duplicate = no_duplicate_posts(
        post, from_latest_x_posts=10, _in="staging"
    )

    assert not has_no_duplicate


def test_no_duplicate_posts():
    unique_string = (
        "[llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch]"
    )

    problem_set = Blind75()
    post = problem_set.get_problems(day=1)
    post = unique_string + post

    has_no_duplicate = no_duplicate_posts(
        post, from_latest_x_posts=10, _in="staging"
    )

    assert has_no_duplicate
