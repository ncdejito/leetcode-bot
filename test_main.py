from main import main, client
from src.zulip_comms import get_posts, clean_sent, clean_received
from src.scheduling import to_date, now
import time
import pytest


@pytest.mark.skip(reason="")
@pytest.mark.parametrize(
    "time_now, schedule_et, expected",
    [
        (now(), now(), True),
        (to_date("10:00:00"), to_date("10:00:00"), True),
        (to_date("11:00:00"), to_date("10:00:00"), False),
    ],
)
def test_main(time_now, schedule_et, expected):
    post = main(time_now, schedule_et, destination="staging")
    has_content = len(post) > 20
    assert has_content == expected
