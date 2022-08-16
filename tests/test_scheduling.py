import pytest
from src.scheduling import on_schedule, no_similar_posts


def test_if_on_schedule():
    assert 1 == 0


def test_no_similar_posts():
    assert 1 == 0


@pytest.mark.skip(reason="")
def test_if_all_days_have_batches():
    years = np.arange(2022, 2025, 1)
    assert 1 == 0


@pytest.mark.skip(reason="")
def test_if_all_days_have_batchdays():
    assert 1 == 0
