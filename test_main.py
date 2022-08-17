from main import main, client
from src.zulip_comms import get_posts, clean_sent, clean_received
from src.scheduling import to_date
import time


def test_main_on_schedule():
    # TODO: fix state-dependence - if you run once, the uploaded text persists on zulip

    # send post
    post = main(time_now=to_date("10:00:00"), destination="staging")

    time.sleep(1)
    recs = get_posts(num_before=1, client=client)
    text = recs[-1]  # latest

    sent = clean_sent(post)

    received = clean_received(text)

    assert sent == received


def test_main_not_on_schedule():

    # send post
    post = main(time_now=to_date("11:00:00"), destination="staging")

    time.sleep(1)
    recs = get_posts(num_before=1, client=client)
    text = recs[-1]  # latest

    sent = clean_sent(post)

    received = clean_received(text)

    assert sent != received
