from bs4 import BeautifulSoup
import pytest

from src.zulip_comms import get_client, get_posts, send

client = get_client()


@pytest.mark.skip(reason="")
def test_get_posts():
    results = get_posts(num_before=1, client=client)
    assert len(results) > 0


@pytest.mark.skip(reason="")
def test_send():
    send("test send", client)

    results = get_posts(num_before=1, client=client)
    recs = []
    for msg in results["messages"]:
        html = BeautifulSoup(msg["content"])
        text = html.get_text()
        recs.append(text)

    assert text == "test send"
