import pytest
from src.scheduling import on_schedule, to_date, now


@pytest.mark.parametrize(
    "time_now, schedule_et, acceptable_window_mins, expected",
    [
        (now(), now(), 5, True),
        (to_date("10:00:00"), to_date("10:00:00"), 5, True),
        (to_date("11:00:00"), to_date("10:00:00"), 5, False),
    ],
)
def test_if_on_schedule(
    time_now, schedule_et, acceptable_window_mins, expected
):
    assert (
        on_schedule(time_now, schedule_et, acceptable_window_mins) == expected
    )


@pytest.mark.skip(reason="")
def test_if_all_days_have_batches():
    years = np.arange(2022, 2025, 1)
    assert 1 == 0


@pytest.mark.skip(reason="")
def test_if_all_days_have_batchdays():
    assert 1 == 0
