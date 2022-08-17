import arrow
from .zulip_comms import get_posts
from arrow.arrow import Arrow


def now():
    return arrow.utcnow().to("US/Eastern")


def to_date(schedule_et) -> Arrow:
    if type(schedule_et) is Arrow:
        return schedule_et
    else:
        # make compliant to ISO 8601
        parts = now().format("YYYY-MM-DD HH:mm:ss ZZ").split(" ")
        schedule_text = parts[0] + "T" + schedule_et + parts[2]
        return arrow.get(schedule_text)


def on_schedule(
    time_now,
    schedule_et="10:00:00",  # can also be time of type Arrow
    acceptable_window_mins=5,
):
    schedule = to_date(schedule_et)
    window_min = schedule.shift(minutes=-acceptable_window_mins)
    window_max = schedule.shift(minutes=acceptable_window_mins)

    if time_now < window_max and time_now > window_min:
        return True
    else:
        return False


def get_batch(date):
    # winter spring summer fall, 1-2
    return None


def get_batch_day(date):
    # TODO: what day is it in the batch (day1 for f1 2022)
    # CURRENTLY: count progression of days, problem set will be based on modulo on problem_sets.get_problems
    _now = date
    day0 = arrow.get("1970-01-01")
    return (_now - day0).days
