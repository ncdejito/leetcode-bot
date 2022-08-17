#!/usr/bin/env python3

from src.problem_sets import problem_sets
from src.zulip_comms import send, get_client, no_duplicate_posts
from src.scheduling import get_batch_day, on_schedule, now


client = get_client()


def main(time_now, schedule_et, destination):

    post = ""

    if on_schedule(time_now, schedule_et=schedule_et):

        current_batch_day = get_batch_day(time_now)

        for problem_set in problem_sets:
            post += problem_set.get_problems(day=current_batch_day) + "\n"

        if no_duplicate_posts(
            post=post, from_latest_x_posts=10, _in=destination
        ):
            send(post, client, destination)

    return post


if __name__ == "main":
    send("test send", client, to="staging")
    post = main(
        time_now=now(),
        schedule_et="07:10:00",  # "10:00:00"
        destination="staging",  # "prod"
    )
    print("Post:")
    print(post)
