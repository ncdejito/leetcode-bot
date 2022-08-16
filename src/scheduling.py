import arrow
from .zulip_comms import get_posts

now = arrow.utcnow()


def no_similar_posts(post, from_hours_before=24):
    # this_time_yesterday = now.shift(hours=-from_hours_before)
    # posts = get_posts(num_before=10,client)

    return True


def on_schedule(
    schedule=arrow.get("2013-05-11T10:00:00+00:00"),
    acceptable_window_mins=5,
):
    # window_min = (schedule.shift(minute=-acceptable_window_mins),)
    # window_max = (schedule.shift(minute=acceptable_window_mins),)

    # if window_min < now < window_max:
    #     return True

    return True


def get_batch(date):
    # winter spring summer fall, 1-2
    return None


def get_batch_day(date):
    # what day is it in the batch (day1 for f1 2022)
    return None
