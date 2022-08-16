#!/usr/bin/env python3

from src.problem_sets import problem_sets
from src.zulip_comms import send, get_client
from src.scheduling import on_schedule, no_similar_posts


client = get_client()


def main(destination="staging"):

    if on_schedule():

        post = ""

        for problem_set in problem_sets:
            post += problem_set.get_problems() + "\n"

        if no_similar_posts(post=post, from_hours_before=24):
            send(post, client, destination)

    return post


if __name__ == "main":
    # _ = main(destination="prod")
    pass
